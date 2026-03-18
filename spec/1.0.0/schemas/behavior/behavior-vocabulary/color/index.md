Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0
Editor: Charles F. Munat

# Behavior Vocabulary — Color

This specification defines the **Color operator family** for the Behavior Vocabulary.

This document is **Normative**.

---

## 1. Purpose

This specification defines comprehensive color operations for Behavior Programs, including:

- Color construction and decomposition
- Color space conversion
- Color manipulation (lightening, darkening, mixing)
- Color analysis (contrast, luminance)
- Color harmonies and palettes

---

## 2. Color Types

As defined by §7 (Behavior Dialect), the following color representations are supported:

- `HexColor` — `#RGB`, `#RGBA`, `#RRGGBB`, `#RRGGBBAA`
- `RgbColor` — RGB with optional alpha
- `HslColor` — HSL with optional alpha
- `LabColor` — CIE Lab
- `LchColor` — CIE LCH
- `OklabColor` — Oklab
- `OklchColor` — Oklch
- `ColorFunction` — Wide gamut in specified color space

All operations work on any color type. Conversions are performed internally as needed.

---

## 3. Color Construction (Normative)

### 3.1 RGB Construction

```
MakeRgbColor(red, green, blue) -> RgbColor
MakeRgbColor(red, green, blue, alpha) -> RgbColor
```

Parameters:
- `red`, `green`, `blue`: 0-255 (Integer) or 0.0-1.0 (RealNumber)
- `alpha`: 0.0-1.0

Error behavior:
- If any component is outside its valid range (red/green/blue: 0–255 integer or 0.0–1.0 real; alpha: 0.0–1.0): `Invalid(...)` with code `Color::COMPONENT_OUT_OF_RANGE`.

### 3.2 HSL Construction

```
MakeHslColor(hue, saturation, lightness) -> HslColor
MakeHslColor(hue, saturation, lightness, alpha) -> HslColor
```

Parameters:
- `hue`: 0-360 degrees
- `saturation`: 0-100%
- `lightness`: 0-100%

Error behavior:
- If saturation, lightness, or alpha is outside its valid range (saturation: 0–100; lightness: 0–100; alpha: 0.0–1.0): `Invalid(...)` with code `Color::COMPONENT_OUT_OF_RANGE`. Hue values outside 0–360 are wrapped modulo 360.

### 3.3 Lab Construction

```
MakeLabColor(lightness, a, b) -> LabColor
MakeLabColor(lightness, a, b, alpha) -> LabColor
```

Parameters:
- `lightness`: 0-100
- `a`: typically -128 to 127
- `b`: typically -128 to 127

Error behavior:
- If lightness is outside 0–100 or alpha is outside 0.0–1.0: `Invalid(...)` with code `Color::COMPONENT_OUT_OF_RANGE`.

### 3.4 LCH Construction

```
MakeLchColor(lightness, chroma, hue) -> LchColor
MakeLchColor(lightness, chroma, hue, alpha) -> LchColor
```

Error behavior:
- If lightness is outside 0–100 or alpha is outside 0.0–1.0: `Invalid(...)` with code `Color::COMPONENT_OUT_OF_RANGE`.

### 3.5 Oklab Construction

```
MakeOklabColor(lightness, a, b) -> OklabColor
MakeOklabColor(lightness, a, b, alpha) -> OklabColor
```

Parameters:
- `lightness`: 0-1
- `a`, `b`: typically -0.4 to 0.4

Error behavior:
- If lightness is outside 0–1 or alpha is outside 0.0–1.0: `Invalid(...)` with code `Color::COMPONENT_OUT_OF_RANGE`.

### 3.6 Oklch Construction

```
MakeOklchColor(lightness, chroma, hue) -> OklchColor
MakeOklchColor(lightness, chroma, hue, alpha) -> OklchColor
```

Error behavior:
- If lightness is outside 0–1 or alpha is outside 0.0–1.0: `Invalid(...)` with code `Color::COMPONENT_OUT_OF_RANGE`.

### 3.7 Hex Construction

```
MakeHexColor(hexString) -> HexColor
```

Parameters:
- `hexString`: "#RGB", "#RGBA", "#RRGGBB", or "#RRGGBBAA"

Error behavior:
- If `hexString` is not a valid hex color format: `Invalid(...)` with code `Color::INVALID_HEX_STRING`.

### 3.8 Wide Gamut Construction

```
MakeColorInSpace(colorSpace, c1, c2, c3) -> ColorFunction
MakeColorInSpace(colorSpace, c1, c2, c3, alpha) -> ColorFunction
```

Color spaces:
- `srgb`, `srgb-linear`
- `display-p3`
- `a98-rgb`
- `prophoto-rgb`
- `rec2020`
- `xyz`, `xyz-d50`, `xyz-d65`

Error behavior:
- If `colorSpace` is not a recognized color space: `Invalid(...)` with code `Color::UNKNOWN_COLOR_SPACE`.

### 3.9 Named Color

```
NamedColor(name) -> RgbColor
```

Parameters:
- `name`: CSS named color (e.g., "red", "rebeccapurple")

Error behavior:
- If name is not recognized: `Invalid(...)` with code `Color::UNKNOWN_COLOR_NAME`.

---

## 4. Color Decomposition (Normative)

### 4.1 RGB Components

```
RedComponent(color) -> Integer
GreenComponent(color) -> Integer
BlueComponent(color) -> Integer
AlphaComponent(color) -> RealNumber
```

Returns components in 0-255 range (RGB) or 0-1 range (alpha).

### 4.2 HSL Components

```
HueComponent(color) -> RealNumber
SaturationComponent(color) -> RealNumber
LightnessComponent(color) -> RealNumber
```

Returns: hue 0-360, saturation 0-100, lightness 0-100.

### 4.3 Lab Components

```
LabLightnessComponent(color) -> RealNumber
LabAComponent(color) -> RealNumber
LabBComponent(color) -> RealNumber
```

### 4.4 LCH Components

```
LchLightnessComponent(color) -> RealNumber
LchChromaComponent(color) -> RealNumber
LchHueComponent(color) -> RealNumber
```

### 4.5 Oklab Components

```
OklabLightnessComponent(color) -> RealNumber
OklabAComponent(color) -> RealNumber
OklabBComponent(color) -> RealNumber
```

### 4.6 Oklch Components

```
OklchLightnessComponent(color) -> RealNumber
OklchChromaComponent(color) -> RealNumber
OklchHueComponent(color) -> RealNumber
```

---

## 5. Color Space Conversion (Normative)

### 5.1 Convert To Specific Space

```
ConvertToRgb(color) -> RgbColor
ConvertToHsl(color) -> HslColor
ConvertToLab(color) -> LabColor
ConvertToLch(color) -> LchColor
ConvertToOklab(color) -> OklabColor
ConvertToOklch(color) -> OklchColor
ConvertToHex(color) -> HexColor
```

### 5.2 Convert To Color Space

```
ConvertToColorSpace(color, colorSpace) -> ColorFunction
```

Error behavior:
- If `colorSpace` is not recognized: `Invalid(...)` with code `Color::UNKNOWN_COLOR_SPACE`.

### 5.3 Gamut Mapping

```
MapToGamut(color, colorSpace) -> Color
```

Semantics:
- Maps out-of-gamut colors to the nearest in-gamut color.

```
IsInGamut(color, colorSpace) -> Boolean
```

Error behavior (`MapToGamut`, `IsInGamut`):
- If `colorSpace` is not recognized: `Invalid(...)` with code `Color::UNKNOWN_COLOR_SPACE`.

---

## 6. Color Manipulation (Normative)

### 6.1 Lightness Adjustment

```
Lighten(color, amount) -> Color
```

Parameters:
- `amount`: 0-100 (percentage to lighten)

```
Darken(color, amount) -> Color
```

```
SetLightness(color, lightness) -> Color
```

### 6.2 Saturation Adjustment

```
Saturate(color, amount) -> Color
Desaturate(color, amount) -> Color
SetSaturation(color, saturation) -> Color
Grayscale(color) -> Color
```

`Grayscale` is equivalent to `Desaturate(color, 100)`.

### 6.3 Hue Adjustment

```
RotateHue(color, degrees) -> Color
SetHue(color, hue) -> Color
```

### 6.4 Alpha Adjustment

```
SetAlpha(color, alpha) -> Color
Opacify(color, amount) -> Color
Transparentize(color, amount) -> Color
```

`Opacify` increases opacity; `Transparentize` decreases it.

### 6.5 Inversion

```
InvertColor(color) -> Color
```

Semantics:
- Inverts RGB values. Alpha is preserved.

```
ComplementaryColor(color) -> Color
```

Semantics:
- Rotates hue by 180 degrees.

---

## 7. Color Mixing (Normative)

### 7.1 Basic Mixing

```
MixColors(color1, color2) -> Color
MixColors(color1, color2, weight) -> Color
```

Parameters:
- `weight`: 0-1, proportion of color1 (default 0.5)

Semantics:
- Mixes in Oklab color space for perceptual uniformity.

### 7.2 Mix In Specific Space

```
MixColorsInSpace(color1, color2, weight, colorSpace) -> Color
```

Color spaces for mixing:
- `rgb`, `hsl`, `lab`, `lch`, `oklab`, `oklch`

Error behavior:
- If `colorSpace` is not recognized: `Invalid(...)` with code `Color::UNKNOWN_COLOR_SPACE`.

### 7.3 Blend Modes

```
BlendColors(base, blend, mode) -> Color
```

Blend modes:
- `normal`
- `multiply`
- `screen`
- `overlay`
- `darken`
- `lighten`
- `color-dodge`
- `color-burn`
- `hard-light`
- `soft-light`
- `difference`
- `exclusion`
- `hue`
- `saturation`
- `color`
- `luminosity`

Error behavior:
- If `mode` is not a recognized blend mode: `Invalid(...)` with code `Color::UNKNOWN_BLEND_MODE`.

---

## 8. Color Analysis (Normative)

### 8.1 Luminance

```
RelativeLuminance(color) -> RealNumber
```

Semantics:
- Returns WCAG relative luminance (0-1).

```
PerceivedLightness(color) -> RealNumber
```

Semantics:
- Returns Oklab lightness (0-1).

### 8.2 Contrast

```
ContrastRatio(color1, color2) -> RealNumber
```

Semantics:
- Returns WCAG 2.1 contrast ratio (1:1 to 21:1).

```
MeetsContrastRequirement(color1, color2, level) -> Boolean
```

Parameters:
- `level`: "AA", "AAA", "AA-large", "AAA-large"

WCAG 2.1 requirements:
- AA: 4.5:1 (3:1 for large text)
- AAA: 7:1 (4.5:1 for large text)

Error behavior (`MeetsContrastRequirement`):
- If `level` is not a recognized WCAG level: `Invalid(...)` with code `Color::INVALID_CONTRAST_LEVEL`.

```
AppcaContrast(textColor, backgroundColor) -> RealNumber
```

Semantics:
- Returns APCA (Accessible Perceptual Contrast Algorithm) value.

### 8.3 Color Difference

```
ColorDifference(color1, color2) -> RealNumber
```

Semantics:
- Returns Delta E 2000 (CIE color difference).

```
ColorDifferenceEuclidean(color1, color2, colorSpace) -> RealNumber
```

Semantics:
- Euclidean distance in specified color space.

Error behavior (`ColorDifferenceEuclidean`):
- If `colorSpace` is not recognized: `Invalid(...)` with code `Color::UNKNOWN_COLOR_SPACE`.

### 8.4 Color Properties

```
IsLightColor(color) -> Boolean
IsDarkColor(color) -> Boolean
```

Semantics:
- Based on perceived lightness threshold (0.5 in Oklab).

```
IsCoolColor(color) -> Boolean
IsWarmColor(color) -> Boolean
```

Semantics:
- Based on hue ranges.

```
IsNeutralColor(color) -> Boolean
```

Semantics:
- True if saturation/chroma is below threshold.

---

## 9. Color Harmonies (Normative)

### 9.1 Harmony Generation

```
ComplementaryColors(color) -> Tuple<Color, Color>
```

Returns: original and 180° rotated.

```
TriadicColors(color) -> Tuple<Color, Color, Color>
```

Returns: original, +120°, +240°.

```
TetradicColors(color) -> Tuple<Color, Color, Color, Color>
```

Returns: original, +90°, +180°, +270°.

```
SplitComplementaryColors(color) -> Tuple<Color, Color, Color>
```

Returns: original, +150°, +210°.

```
AnalogousColors(color, count, angle) -> List<Color>
```

Parameters:
- `count`: number of colors
- `angle`: degrees between adjacent colors

Error behavior:
- If `count` is less than 1: `Invalid(...)` with code `Color::COUNT_NOT_POSITIVE`.

### 9.2 Shade and Tint Generation

```
Shades(color, count) -> List<Color>
```

Semantics:
- Generates progressively darker versions.

```
Tints(color, count) -> List<Color>
```

Semantics:
- Generates progressively lighter versions.

```
Tones(color, count) -> List<Color>
```

Semantics:
- Generates progressively more gray versions.

Error behavior (`Shades`, `Tints`, `Tones`):
- If `count` is less than 1: `Invalid(...)` with code `Color::COUNT_NOT_POSITIVE`.

---

## 10. Palette Operations (Normative)

### 10.1 Palette Generation

```
GenerateScale(color1, color2, steps) -> List<Color>
```

Semantics:
- Generates evenly spaced colors between two endpoints.

```
GenerateScaleInSpace(color1, color2, steps, colorSpace) -> List<Color>
```

Error behavior:
- If `steps` is less than 1: `Invalid(...)` with code `Color::COUNT_NOT_POSITIVE`.
- If `colorSpace` is not recognized (`GenerateScaleInSpace`): `Invalid(...)` with code `Color::UNKNOWN_COLOR_SPACE`.

### 10.2 Palette Analysis

```
AverageColor(colors) -> Color
```

Semantics:
- Computes average in Oklab space.

```
DominantColors(colors, count) -> List<Color>
```

Semantics:
- Returns most distinct colors using k-means clustering.

Error behavior:
- If `count` is less than 1: `Invalid(...)` with code `Color::COUNT_NOT_POSITIVE`.

### 10.3 Accessibility Palette

```
ContrastingTextColor(backgroundColor) -> Color
```

Semantics:
- Returns black or white, whichever has better contrast.

```
ContrastingColor(color, minimumRatio) -> Color
```

Semantics:
- Adjusts lightness to achieve minimum contrast ratio.

```
AdjustForContrast(foreground, background, targetRatio) -> Color
```

Semantics:
- Adjusts foreground to achieve target contrast with background.

---

## 11. Color Format Conversion (Normative)

### 11.1 To String

```
ColorToHexString(color) -> Text
ColorToRgbString(color) -> Text
ColorToHslString(color) -> Text
```

Examples:
- `ColorToHexString(...)` -> `"#ff8800"`
- `ColorToRgbString(...)` -> `"rgb(255 136 0)"`
- `ColorToHslString(...)` -> `"hsl(32 100% 50%)"`

### 11.2 From String

```
ParseColor(text) -> Color
```

Semantics:
- Parses any valid CSS color string.

Error behavior:
- If invalid format: `Invalid(...)` with code `Color::INVALID_COLOR_STRING`.

---

## 12. Interpolation (Normative)

```
InterpolateColors(color1, color2, t) -> Color
InterpolateColorsInSpace(color1, color2, t, colorSpace) -> Color
```

Error behavior (`InterpolateColorsInSpace`):
- If `colorSpace` is not recognized: `Invalid(...)` with code `Color::UNKNOWN_COLOR_SPACE`.

Parameters:
- `t`: 0-1, interpolation position

```
InterpolatePath(colors, t) -> Color
```

Semantics:
- Interpolates along a path through multiple colors.

---

## 13. Type Guards (Normative)

```
IsColor(value) -> Boolean
IsHexColor(value) -> Boolean
IsRgbColor(value) -> Boolean
IsHslColor(value) -> Boolean
IsLabColor(value) -> Boolean
IsLchColor(value) -> Boolean
IsOklabColor(value) -> Boolean
IsOklchColor(value) -> Boolean
```

---

## 14. Conformance Appendix (Informative)

See [conformance-appendix/index.md](conformance-appendix/index.md).

---

## 15. Diagnostic Code Table (Normative)

| Code | Operators | Expected | Message | Suggestion |
|------|-----------|----------|---------|------------|
| `Color::COMPONENT_OUT_OF_RANGE` | `MakeRgbColor`, `MakeHslColor`, `MakeLabColor`, `MakeLchColor`, `MakeOklabColor`, `MakeOklchColor` | component within valid range | "Lexis expected a color component within its valid range, but found a value outside the allowed bounds." | "Please check the component values — each must be within the range specified for its color space." |
| `Color::INVALID_HEX_STRING` | `MakeHexColor` | valid hex color format | "Lexis expected a valid hex color string (#RGB, #RGBA, #RRGGBB, or #RRGGBBAA), but failed to parse the value provided." | "Please provide a hex color string in one of the recognized formats: #RGB, #RGBA, #RRGGBB, or #RRGGBBAA." |
| `Color::UNKNOWN_COLOR_NAME` | `NamedColor` | recognized CSS color name | "Lexis expected a recognized CSS color name, but did not recognize the value provided." | "Please provide a valid CSS named color (e.g., \"red\", \"rebeccapurple\", \"cornflowerblue\")." |
| `Color::UNKNOWN_COLOR_SPACE` | `MakeColorInSpace`, `ConvertToColorSpace`, `MapToGamut`, `IsInGamut`, `MixColorsInSpace`, `ColorDifferenceEuclidean`, `GenerateScaleInSpace`, `InterpolateColorsInSpace` | recognized color space identifier | "Lexis expected a recognized color space identifier, but did not recognize the value provided." | "Please use one of the recognized color spaces: \"srgb\", \"srgb-linear\", \"display-p3\", \"a98-rgb\", \"prophoto-rgb\", \"rec2020\", \"xyz\", \"xyz-d50\", \"xyz-d65\"." |
| `Color::INVALID_COLOR_STRING` | `ParseColor` | valid CSS color string | "Lexis expected a valid CSS color string, but failed to parse the value provided." | "Please provide a valid CSS color string (e.g., \"#ff8800\", \"rgb(255 136 0)\", \"hsl(32 100% 50%)\")." |
| `Color::UNKNOWN_BLEND_MODE` | `BlendColors` | recognized blend mode | "Lexis expected a recognized blend mode, but did not recognize the value provided." | "Please use one of the recognized blend modes: \"normal\", \"multiply\", \"screen\", \"overlay\", \"darken\", \"lighten\", \"color-dodge\", \"color-burn\", \"hard-light\", \"soft-light\", \"difference\", \"exclusion\", \"hue\", \"saturation\", \"color\", \"luminosity\"." |
| `Color::INVALID_CONTRAST_LEVEL` | `MeetsContrastRequirement` | recognized WCAG contrast level | "Lexis expected a recognized WCAG contrast level, but did not recognize the value provided." | "Please use one of the recognized levels: \"AA\", \"AAA\", \"AA-large\", \"AAA-large\"." |
| `Color::COUNT_NOT_POSITIVE` | `AnalogousColors`, `Shades`, `Tints`, `Tones`, `GenerateScale`, `GenerateScaleInSpace`, `DominantColors` | positive integer count | "Lexis expected a positive integer for the count, but found a value less than 1." | "Please provide a count of at least 1." |

---

**End of Behavior Vocabulary — Color v1.0.0**
