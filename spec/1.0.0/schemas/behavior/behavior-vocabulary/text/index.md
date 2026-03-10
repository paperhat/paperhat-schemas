Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0
Editor: Charles F. Munat

# Behavior Vocabulary — Text

This specification defines the **Text operator family** for the Behavior Vocabulary.

This document is **Normative**.

---

## 1. Purpose

This specification defines comprehensive text operations for Behavior Programs, including:

- Text construction and manipulation
- Character operations
- Searching and pattern matching
- Case transformation
- Unicode operations
- Encoding/decoding

---

## 2. Basic Operations (Normative)

### 2.1 Length and Size

```
TextLength(text) -> Integer
```

Returns: number of Unicode scalar values.

```
TextByteLength(text, encoding) -> Integer
```

Returns: byte length in specified encoding ("utf-8", "utf-16", "utf-32").

Error behavior for `TextByteLength`:
- If encoding is not a recognized encoding name: `Invalid(...)` with code `TextByteLength::INVALID_ENCODING_NAME`.

```
IsEmptyText(text) -> Boolean
IsNotEmptyText(text) -> Boolean
IsBlankText(text) -> Boolean
```

`IsBlankText` returns true if empty or contains only whitespace.

### 2.2 Concatenation

```
ConcatenateText(text1, text2) -> Text
ConcatenateText(text1, text2, ...) -> Text
JoinText(texts, separator) -> Text
```

### 2.3 Repetition

```
RepeatText(text, count) -> Text
```

### 2.4 Substring

```
Substring(text, startIndex) -> Text
Substring(text, startIndex, endIndex) -> Text
SubstringByLength(text, startIndex, length) -> Text
```

Indices are zero-based. Negative indices count from end.

### 2.5 Padding

```
PadStart(text, targetLength, padString) -> Text
PadEnd(text, targetLength, padString) -> Text
PadBoth(text, targetLength, padString) -> Text
```

### 2.6 Trimming

```
Trim(text) -> Text
TrimStart(text) -> Text
TrimEnd(text) -> Text
TrimCharacters(text, characters) -> Text
```

`TrimCharacters` removes specified characters from both ends.

### 2.7 Access

```
CharacterAt(text, index) -> Character
FirstCharacter(text) -> Character
LastCharacter(text) -> Character
```

Returns `<Absent/>` if index out of bounds.

---

## 3. Searching (Normative)

### 3.1 Index Finding

```
IndexOf(text, search) -> Integer
IndexOf(text, search, startIndex) -> Integer
LastIndexOf(text, search) -> Integer
LastIndexOf(text, search, startIndex) -> Integer
```

Returns -1 if not found.

```
IndicesOf(text, search) -> List<Integer>
```

Returns all occurrence positions.

### 3.2 Containment

```
ContainsSubstring(text, search) -> Boolean
StartsWithSubstring(text, prefix) -> Boolean
EndsWithSubstring(text, suffix) -> Boolean
```

### 3.3 Counting

```
CountOccurrences(text, search) -> Integer
```

---

## 4. Replacement (Normative)

### 4.1 Basic Replacement

```
ReplaceFirst(text, search, replacement) -> Text
ReplaceLast(text, search, replacement) -> Text
ReplaceAll(text, search, replacement) -> Text
```

### 4.2 Pattern Replacement

```
ReplaceFirstPattern(text, pattern, replacement) -> Text
ReplaceAllPattern(text, pattern, replacement) -> Text
```

Pattern is a regular expression per §7.0 (Regular Expression Profile).

Error behavior:
- If pattern is not a valid regular expression: `Invalid(...)` with code `Text::INVALID_PATTERN`.

### 4.3 Character Replacement

```
ReplaceCharacters(text, fromChars, toChars) -> Text
```

Character-by-character translation (like tr).

Error behavior:
- If `fromChars` and `toChars` have different lengths: `Invalid(...)` with code `ReplaceCharacters::LENGTH_MISMATCH`.

### 4.4 Removal

```
RemoveSubstring(text, search) -> Text
RemoveAllSubstrings(text, search) -> Text
RemoveCharacters(text, characters) -> Text
```

---

## 5. Splitting and Joining (Normative)

### 5.1 Splitting

```
Split(text, separator) -> List<Text>
SplitByPattern(text, pattern) -> List<Text>
SplitByLength(text, length) -> List<Text>
SplitLines(text) -> List<Text>
SplitWords(text) -> List<Text>
```

Error behavior for `SplitByPattern`:
- If pattern is not a valid regular expression: `Invalid(...)` with code `Text::INVALID_PATTERN`.

### 5.2 Partitioning

```
Partition(text, separator) -> Tuple<Text, Text, Text>
PartitionLast(text, separator) -> Tuple<Text, Text, Text>
```

Returns: (before, separator, after). If not found, returns (text, "", "").

---

## 6. Case Transformation (Normative)

### 6.1 Standard Case

```
ToUpperCase(text) -> Text
ToLowerCase(text) -> Text
ToTitleCase(text) -> Text
```

### 6.2 Programming Case

```
ToCamelCase(text) -> Text
ToPascalCase(text) -> Text
ToSnakeCase(text) -> Text
ToKebabCase(text) -> Text
ToScreamingSnakeCase(text) -> Text
```

### 6.3 Sentence Case

```
ToSentenceCase(text) -> Text
Capitalize(text) -> Text
Uncapitalize(text) -> Text
```

`Capitalize` uppercases first character.
`Uncapitalize` lowercases first character.

### 6.4 Case Predicates

```
IsUpperCase(text) -> Boolean
IsLowerCase(text) -> Boolean
IsTitleCase(text) -> Boolean
IsMixedCase(text) -> Boolean
```

### 6.5 Case-Insensitive Comparison

```
EqualsIgnoreCase(text1, text2) -> Boolean
CompareIgnoreCase(text1, text2) -> Integer
```

`CompareIgnoreCase` returns -1, 0, or 1.

---

## 7. Pattern Matching (Normative)

### 7.0 Regular Expression Profile

All pattern-matching operators in this section accept regular expression patterns conforming to the following profile.

Allowed syntax:

- Literal characters and character escapes (`\.`, `\n`, `\t`, `\\`, etc.)
- Character classes (`[abc]`, `[^abc]`, `[a-z]`)
- Unicode character classes (`\p{Letter}`, `\p{Script=Greek}`, `\P{...}`)
- Shorthand classes (`\d`, `\D`, `\w`, `\W`, `\s`, `\S`)
- Quantifiers (`*`, `+`, `?`, `{n}`, `{n,}`, `{n,m}`) and their lazy variants (`*?`, `+?`, `??`)
- Alternation (`|`)
- Grouping (`(...)`) and non-capturing groups (`(?:...)`)
- Named capture groups (`(?P<name>...)` or `(?<name>...)`)
- Anchors (`^`, `$`, `\b`, `\B`)
- Dot (`.`) matching any character except newline (unless single-line mode is active)

Prohibited syntax:

- Backreferences (`\1`, `\k<name>`) MUST NOT be supported. Backreferences make the matching problem NP-hard, violating Lexis's resource-boundedness guarantees.
- Lookahead and lookbehind assertions (`(?=...)`, `(?!...)`, `(?<=...)`, `(?<!...)`) MUST NOT be supported in v1. These constructs introduce implementation-dependent matching behavior that can break determinism.

Requirements:

- All matching MUST be deterministic: for any input text and valid pattern, the match result MUST be identical across conformant implementations.
- Patterns MUST operate on Unicode scalar values (not bytes).
- Pattern compilation failure MUST produce `Invalid(...)` with code `Text::INVALID_PATTERN`.
- A pattern that uses prohibited syntax MUST be rejected at compilation with `Text::INVALID_PATTERN`.

### 7.1 Regular Expression Matching

```
MatchesPattern(text, pattern) -> Boolean
DoesNotMatchPattern(text, pattern) -> Boolean
```

Error behavior:
- If pattern is not a valid regular expression: `Invalid(...)` with code `Text::INVALID_PATTERN`.

### 7.2 Finding Matches

```
FindFirstMatch(text, pattern) -> Record { match, index, groups }
FindAllMatches(text, pattern) -> List<Record { match, index, groups }>
```

`groups` is a List of captured group strings.

Error behavior:
- If pattern is not a valid regular expression: `Invalid(...)` with code `Text::INVALID_PATTERN`.

### 7.3 Testing

```
TestPattern(text, pattern) -> Boolean
```

Equivalent to `MatchesPattern`.

Error behavior:
- If pattern is not a valid regular expression: `Invalid(...)` with code `Text::INVALID_PATTERN`.

### 7.4 Extraction

```
ExtractFirstMatch(text, pattern) -> Text
ExtractAllMatches(text, pattern) -> List<Text>
ExtractGroups(text, pattern) -> List<Text>
```

Error behavior:
- If pattern is not a valid regular expression: `Invalid(...)` with code `Text::INVALID_PATTERN`.

---

## 8. Character Classification (Normative)

### 8.1 Content Predicates

```
ContainsOnlyDigits(text) -> Boolean
ContainsOnlyLetters(text) -> Boolean
ContainsOnlyLettersAndDigits(text) -> Boolean
ContainsOnlyWhitespace(text) -> Boolean
ContainsOnlyAscii(text) -> Boolean
ContainsOnlyPrintable(text) -> Boolean
```

### 8.2 Character Type Counts

```
DigitCount(text) -> Integer
LetterCount(text) -> Integer
WhitespaceCount(text) -> Integer
UpperCaseCount(text) -> Integer
LowerCaseCount(text) -> Integer
```

---

## 9. Character Operations (Normative)

### 9.1 Construction

```
MakeCharacter(codePoint) -> Character
```

Error behavior:
- If code point is not a valid Unicode scalar value: `Invalid(...)` with code `Text::INVALID_CODE_POINT`.

```
CharacterFromText(text) -> Character
```

Error behavior:
- If text length is not exactly 1: `Invalid(...)` with code `CharacterFromText::NEED_SINGLE_CHARACTER`.

### 9.2 Code Point

```
CodePoint(character) -> Integer
CharacterFromCodePoint(codePoint) -> Character
```

Error behavior for `CharacterFromCodePoint`:
- If code point is not a valid Unicode scalar value: `Invalid(...)` with code `Text::INVALID_CODE_POINT`.

### 9.3 Classification

```
IsLetter(character) -> Boolean
IsDigit(character) -> Boolean
IsLetterOrDigit(character) -> Boolean
IsWhitespace(character) -> Boolean
IsUpperCaseLetter(character) -> Boolean
IsLowerCaseLetter(character) -> Boolean
IsTitleCaseLetter(character) -> Boolean
IsPunctuation(character) -> Boolean
IsSymbol(character) -> Boolean
IsControl(character) -> Boolean
IsAscii(character) -> Boolean
IsPrintable(character) -> Boolean
```

### 9.4 Case Conversion

```
CharacterToUpperCase(character) -> Character
CharacterToLowerCase(character) -> Character
CharacterToTitleCase(character) -> Character
```

### 9.5 Character to Text

```
CharacterToText(character) -> Text
```

### 9.6 Type Guard

```
IsCharacter(value) -> Boolean
```

---

## 10. Unicode Operations (Normative)

### 10.1 Normalization

```
NormalizeNfc(text) -> Text
NormalizeNfd(text) -> Text
NormalizeNfkc(text) -> Text
NormalizeNfkd(text) -> Text
IsNormalized(text, form) -> Boolean
```

Forms: "NFC", "NFD", "NFKC", "NFKD".

Error behavior for `IsNormalized`:
- If form is not a recognized normalization form: `Invalid(...)` with code `IsNormalized::INVALID_NORMALIZATION_FORM`.

### 10.2 Code Points

```
CodePoints(text) -> List<Integer>
TextFromCodePoints(codePoints) -> Text
```

Error behavior for `TextFromCodePoints`:
- If any code point is not a valid Unicode scalar value: `Invalid(...)` with code `Text::INVALID_CODE_POINT`.

### 10.3 Grapheme Clusters

```
GraphemeClusters(text) -> List<Text>
GraphemeClusterCount(text) -> Integer
GraphemeClusterAt(text, index) -> Text
```

### 10.4 Unicode Properties

```
UnicodeCategory(character) -> Text
UnicodeName(character) -> Text
UnicodeBlock(character) -> Text
UnicodeScript(character) -> Text
```

---

## 11. Comparison (Normative)

### 11.1 Basic Comparison

```
TextEquals(text1, text2) -> Boolean
TextCompare(text1, text2) -> Integer
```

`TextCompare` returns -1, 0, or 1 using Unicode code point order.

### 11.2 Alphabetical Comparison

```
IsAlphabeticallyBefore(text1, text2) -> Boolean
IsAlphabeticallyAfter(text1, text2) -> Boolean
IsAlphabeticallyEqual(text1, text2) -> Boolean
```

Uses NFC normalization then code point comparison.

### 11.3 Natural Sort Comparison

```
NaturalSortCompare(text1, text2) -> Integer
```

Treats embedded numbers as numeric values (e.g., "file2" < "file10").

---

## 12. Length Predicates (Normative)

```
HasLengthEqualTo(text, n) -> Boolean
HasLengthAtLeast(text, n) -> Boolean
HasLengthAtMost(text, n) -> Boolean
HasLengthBetween(text, min, max) -> Boolean
```

---

## 13. Encoding (Normative)

### 13.1 Base64

```
ToBase64(text) -> Text
FromBase64(base64Text) -> Text
ToBase64Url(text) -> Text
FromBase64Url(base64Text) -> Text
```

Error behavior:
- If input to `FromBase64` is not valid base64: `Invalid(...)` with code `FromBase64::INVALID_FORMAT`.
- If input to `FromBase64Url` is not valid base64url: `Invalid(...)` with code `FromBase64Url::INVALID_FORMAT`.

### 13.2 Hex

```
ToHex(text) -> Text
FromHex(hexText) -> Text
```

Error behavior for `FromHex`:
- If input is not valid hexadecimal: `Invalid(...)` with code `FromHex::INVALID_FORMAT`.

### 13.3 URL Encoding

```
UrlEncode(text) -> Text
UrlDecode(text) -> Text
UrlEncodeComponent(text) -> Text
UrlDecodeComponent(text) -> Text
```

Error behavior:
- If input to `UrlDecode` contains invalid percent-encoding: `Invalid(...)` with code `UrlDecode::INVALID_FORMAT`.
- If input to `UrlDecodeComponent` contains invalid percent-encoding: `Invalid(...)` with code `UrlDecodeComponent::INVALID_FORMAT`.

### 13.4 HTML Encoding

```
HtmlEncode(text) -> Text
HtmlDecode(text) -> Text
```

---

## 14. Formatting (Normative)

### 14.1 Number Formatting

```
FormatInteger(n) -> Text
FormatNumber(n, decimalPlaces) -> Text
FormatNumberWithSeparator(n, decimalPlaces, thousandsSeparator, decimalSeparator) -> Text
```

### 14.2 Template Interpolation

```
InterpolateTemplate(template, values) -> Text
```

Template uses `{key}` or `{0}`, `{1}` placeholders.
`values` is a Record or List.

---

## 15. Validation (Normative)

### 15.1 Format Validation

```
IsValidEmail(text) -> Boolean
IsValidUrl(text) -> Boolean
IsValidIpv4(text) -> Boolean
IsValidIpv6(text) -> Boolean
IsValidUuid(text) -> Boolean
IsValidJson(text) -> Boolean
```

### 15.2 Type Guard

```
IsText(value) -> Boolean
```

---

## 16. Miscellaneous (Normative)

### 16.1 Reversing

```
ReverseText(text) -> Text
ReverseGraphemeClusters(text) -> Text
```

`ReverseText` reverses code points.
`ReverseGraphemeClusters` reverses grapheme clusters (correct for user-perceived characters).

### 16.2 Wrapping

```
WrapText(text, width) -> Text
WrapTextPreserveWords(text, width) -> Text
```

Inserts line breaks.

### 16.3 Squeezing

```
CollapseWhitespace(text) -> Text
SqueezeCharacter(text, character) -> Text
```

`CollapseWhitespace` replaces runs of whitespace with single space.
`SqueezeCharacter` replaces runs of specified character with single occurrence.

### 16.4 Conversion

```
TextToCharacterList(text) -> List<Character>
CharacterListToText(characters) -> Text
```

---

## 17. Diagnostic Code Table (Normative)

This table consolidates all diagnostic codes defined in the Text operator family.

| Code | Operators | Expected | Message | Suggestion |
|------|-----------|----------|---------|------------|
| `Text::INVALID_PATTERN` | MatchesPattern, DoesNotMatchPattern, FindFirstMatch, FindAllMatches, TestPattern, ExtractFirstMatch, ExtractAllMatches, ExtractGroups, ReplaceFirstPattern, ReplaceAllPattern, SplitByPattern | Valid regular expression | "Lexis expected a valid regular expression, but the pattern could not be parsed." | "Please check the regular expression syntax — it must conform to §7.0 (Regular Expression Profile)." |
| `Text::INVALID_CODE_POINT` | MakeCharacter, CharacterFromCodePoint, TextFromCodePoints | Valid Unicode scalar value | "Lexis expected a valid Unicode scalar value, but found {received}." | "Unicode scalar values range from 0 to D7FF and E000 to 10FFFF — please provide a value in this range." |
| `TextByteLength::INVALID_ENCODING_NAME` | TextByteLength | Recognized encoding name | "Lexis expected a recognized encoding name, but found {received}." | "Please use one of the supported encoding names: \"utf-8\", \"utf-16\", or \"utf-32\"." |
| `CharacterFromText::NEED_SINGLE_CHARACTER` | CharacterFromText | Text of length 1 | "Lexis expected text containing exactly one character, but found text of length {received}." | "Please provide a single-character text value." |
| `ReplaceCharacters::LENGTH_MISMATCH` | ReplaceCharacters | Equal-length character strings | "Lexis expected fromChars and toChars to have the same length, but they differ." | "Please provide character strings of equal length for the replacement mapping." |
| `IsNormalized::INVALID_NORMALIZATION_FORM` | IsNormalized | Recognized normalization form | "Lexis expected a recognized normalization form, but found {received}." | "Please use one of the supported forms: \"NFC\", \"NFD\", \"NFKC\", or \"NFKD\"." |
| `FromBase64::INVALID_FORMAT` | FromBase64 | Valid base64 string | "Lexis expected valid base64-encoded text, but the input could not be decoded." | "Please check that the input contains only valid base64 characters (A-Z, a-z, 0-9, +, /) with correct padding." |
| `FromBase64Url::INVALID_FORMAT` | FromBase64Url | Valid base64url string | "Lexis expected valid base64url-encoded text, but the input could not be decoded." | "Please check that the input contains only valid base64url characters (A-Z, a-z, 0-9, -, _)." |
| `FromHex::INVALID_FORMAT` | FromHex | Valid hexadecimal string | "Lexis expected valid hexadecimal text, but the input could not be decoded." | "Please check that the input contains only valid hex characters (0-9, A-F, a-f) with even length." |
| `UrlDecode::INVALID_FORMAT` | UrlDecode | Valid percent-encoded string | "Lexis expected valid percent-encoded text, but found malformed encoding." | "Please check that all percent-encoded sequences (e.g., %20) use valid two-digit hexadecimal values." |
| `UrlDecodeComponent::INVALID_FORMAT` | UrlDecodeComponent | Valid percent-encoded string | "Lexis expected valid percent-encoded text, but found malformed encoding." | "Please check that all percent-encoded sequences (e.g., %20) use valid two-digit hexadecimal values." |

---

**End of Behavior Vocabulary — Text v1.0.0**
