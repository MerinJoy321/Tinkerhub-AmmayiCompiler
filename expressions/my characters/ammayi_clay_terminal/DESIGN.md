---
name: Ammayi Clay Terminal
colors:
  surface: '#fff8f6'
  surface-dim: '#f9d2c2'
  surface-bright: '#fff8f6'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fff1ec'
  surface-container: '#ffeae1'
  surface-container-high: '#ffe2d7'
  surface-container-highest: '#ffdbcc'
  on-surface: '#2b160d'
  on-surface-variant: '#544342'
  inverse-surface: '#422b20'
  inverse-on-surface: '#ffede6'
  outline: '#867272'
  outline-variant: '#d9c1c0'
  surface-tint: '#93484a'
  primary: '#93484a'
  on-primary: '#ffffff'
  primary-container: '#e78c8d'
  on-primary-container: '#672529'
  inverse-primary: '#ffb3b3'
  secondary: '#795900'
  on-secondary: '#ffffff'
  secondary-container: '#fece65'
  on-secondary-container: '#755700'
  tertiary: '#50643d'
  on-tertiary: '#ffffff'
  tertiary-container: '#96ac7e'
  on-tertiary-container: '#2e401c'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad9'
  primary-fixed-dim: '#ffb3b3'
  on-primary-fixed: '#3d060c'
  on-primary-fixed-variant: '#763134'
  secondary-fixed: '#ffdf9f'
  secondary-fixed-dim: '#efc058'
  on-secondary-fixed: '#261a00'
  on-secondary-fixed-variant: '#5b4300'
  tertiary-fixed: '#d3eab8'
  tertiary-fixed-dim: '#b7ce9e'
  on-tertiary-fixed: '#0f2002'
  on-tertiary-fixed-variant: '#394c27'
  background: '#fff8f6'
  on-background: '#2b160d'
  surface-variant: '#ffdbcc'
typography:
  display-lg:
    fontFamily: Bricolage Grotesque
    fontSize: 48px
    fontWeight: '800'
    lineHeight: 56px
    letterSpacing: -0.03em
  display-lg-mobile:
    fontFamily: Bricolage Grotesque
    fontSize: 34px
    fontWeight: '800'
    lineHeight: 42px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Bricolage Grotesque
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Bricolage Grotesque
    fontSize: 26px
    fontWeight: '700'
    lineHeight: 34px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Bricolage Grotesque
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
  headline-sm:
    fontFamily: Bricolage Grotesque
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '500'
    lineHeight: 28px
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 15px
    fontWeight: '500'
    lineHeight: 24px
  body-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 20px
  label-lg:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
  label-md:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 18px
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '500'
    lineHeight: 16px
  code-block:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 22px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1.25rem
  margin: 1.75rem
  space-xs: 0.375rem
  space-sm: 0.625rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.25rem
---

## Brand & Style
This design system pairs the warmth, wit, and expressive domestic nostalgia of a traditional Kerala household matriarch ("Ammayi") with modern, playful developer tooling. The aesthetic is Claymorphic and tactilely cartoonish: plump, inflated surfaces, friendly pillowy containers, glossy top rims, and organic warm earth-and-spice tones. 

The interface should feel tangible and cushiony rather than cold and clinical—transforming technical tasks like debugging, API testing, terminal logging, and schema editing into an affectionate, encouraging interaction. It deliberately rejects sterile dark-mode monochromes in favor of baked-clay warmth, rounded chunkiness, and friendly editorial character.

## Colors
The palette is rooted in Kerala spice tones, warm clay tiles, and sunlit verandas:

- **Canvas & Backgrounds:** Base canvas uses Warm Cream (`#FFF1D6`), layering upwards with Soft Peach (`#F4B6A6`) for soft structural trays and tinted sidebars.
- **Primary Accent (Ammayi Pink - `#E78C8D`):** Primary interactions, focused tags, active tabs, and key operational states. Paired with a deep accent of Playful Maroon (`#873F4B`) for elevated depth, outlines, and text contrast.
- **Secondary Accent (Chunky Mustard Yellow - `#F2C35B`):** Tactile call-to-action buttons, action highlights, warnings, and code search tags.
- **Tertiary Accent (Kerala Green - `#8EA477`):** Success indicators, runtime health, active connections, and environment tags (reminiscent of lush plantain leaves).
- **Text & Terminal (Warm Brown - `#62473B` & Deep Cocoa - `#392A27`):** Primary reading, code blocks, terminal output, and inset editor panes. Code consoles leverage Deep Cocoa backgrounds with Warm Cream and Mustard syntax highlighting for high-readability warmth without generic neon glow.

## Typography
The typographic hierarchy balances characterful warmth with technical precision:

- **Display & Headlines:** `Bricolage Grotesque` delivers an expressive, idiosyncratic, slightly compressed structure that feels human, warm, and distinctly editorial.
- **Body & Paragraphs:** `Plus Jakarta Sans` provides soft, friendly rounded geometry that keeps long explanations, error traces, and documentation easily digestible and approachable.
- **Developer Labels & Code:** `JetBrains Mono` handles all key-value pairings, JSON viewports, parameters, terminal consoles, and pill metrics, rooting the whimsical clay styling firmly in serious technical utility.

## Layout & Spacing
The layout leverages generous, breathable padding inside inflated surfaces to complement the soft clay volume.

- **Grid Model:** A flexible 12-column desktop grid for multi-pane developer workflows (Side Navigation, Workspace Canvas / Inspector, and Bottom Console Tray).
- **Breakpoints:**
  - **Desktop (≥ 1024px):** 3-panel layout with collapsible tool palettes, fixed margin of `1.75rem`, and gutter spacing of `1.25rem`.
  - **Tablet (768px – 1023px):** 2-panel configuration with off-canvas logs and inspector drawers.
  - **Mobile (< 768px):** Single-column stacked cards with bottom-docked clay action buttons and horizontal pill bars. Margins reduce to `1rem`.
- **Rhythm:** Inner component gaps maintain a chunkier baseline (`space-md` = 16px) to avoid crowded, pinched edges against thick rounded borders.

## Elevation & Depth
Depth is modeled after physical, squishy clay forms resting on a cushioned surface. Rather than traditional sharp drop shadows or flat minimalism, surfaces use dual-layered lighting:

1. **Clay Base (Puffy Resting State):**
   - Soft directional under-shadow: `0 8px 16px -2px rgba(98, 71, 59, 0.16)`.
   - Subtle outer ambient glow: `0 2px 6px 0 rgba(135, 63, 75, 0.08)`.
   - Inner top-lit highlight: `inset 0 2px 3px rgba(255, 255, 255, 0.65)`.
   - Inner bottom compression shadow: `inset 0 -3px 4px rgba(98, 71, 59, 0.12)`.
2. **Elevated Clay (Hover & Active Modals):**
   - Shadow extends to `0 14px 24px -4px rgba(98, 71, 59, 0.22)`.
   - Upward lift of `-2px` on hover.
3. **Depressed / Inset Surface (Terminal Viewports, Text Inputs, Pressed Buttons):**
   - Inner carve shadow: `inset 0 4px 6px rgba(57, 42, 39, 0.2), inset 0 -1px 2px rgba(255, 255, 255, 0.5)`.
   - Pressed buttons physically collapse downward by `+2px` with removed bottom rim shadow to simulate real clay squish.
4. **Borders:**
   - 2px to 3px solid borders in tinted tonal strokes (e.g., `#873F4B` at 18% opacity) to hold silhouette integrity without harsh black lines.

## Shapes
Forms are chunky, inflated, and organically pillowy. Components embrace a pronounced rounded aesthetic where standard containers use `1rem` (16px) to `1.5rem` (24px) corners, while interactive badges, pills, and primary CTAs use fully rounded capsules (`rounded-full`). Sharp 90-degree corners are strictly avoided across all interactive elements, terminal chrome, and dialog frames.

## Components

### Buttons
- **Primary (Chunky Mustard Yellow & Ammayi Pink):**
  - Baked-clay treatment: `background: #F2C35B`, text `color: #392A27`, font `JetBrains Mono` or `Plus Jakarta Sans` semi-bold.
  - Border: 2.5px solid `#873F4B` (25% opacity).
  - Highlights: `inset 0 3px 0 rgba(255,255,255,0.7), inset 0 -3px 0 rgba(98,71,59,0.18)`.
  - Hover: Subtle scale `1.02` with an expanded warm shadow.
  - Active: `transform: translateY(2px)`, inner bottom shadow flattens.
- **Secondary / Ghost:** Soft Peach (`#F4B6A6`) surface with warm maroon border and inset pillowy highlight.

### Chips & Badges
- Status pills use fully-rounded capsule borders (`border-radius: 9999px`) with Kerala Green (`#8EA477`), Soft Peach, or Mustard backgrounds.
- Text rendered in `JetBrains Mono` uppercase with high letter-spacing.
- 1.5px soft border with an inset top highlight for a micro-clay pebble appearance.

### Input Fields & Textareas
- Deeply scooped "carved-clay" look: Warm Cream tinted with 4% Deep Cocoa or pure `#FFFDF7`.
- Shadow: `inset 0 3px 5px rgba(98, 71, 59, 0.12)`.
- Border: 2px solid `#F4B6A6`. Focus shifts border to `#E78C8D` with an outer soft peach ring.
- Placeholder text in Warm Brown at 50% opacity.

### Developer Terminal / Console Pane
- Background: Deep Cocoa (`#392A27`).
- Text: Warm Cream (`#FFF1D6`), Mustard Yellow (`#F2C35B`), and Kerala Green (`#8EA477`) syntax.
- Window Chrome: Puffy top bar styled in Soft Peach with three pillowy clay circle control pegs (Deep Maroon, Mustard, Green).
- Corner radius: `1.5rem` outer radius with subtle inset shadow.

### Cards & Container Panels
- Surface: Cream base with Soft Peach inner sections.
- Border: 2px puffy borders with `1.5rem` corner radius.
- Padding: `space-lg` (24px) to preserve physical clay padding around dense payloads and request inspectors.

### Checkboxes & Radio Toggles
- Custom chunky shapes with 2.5px borders.
- Checkboxes feature rounded 6px corners; radios are full circles.
- Checked state fills with Ammayi Pink (`#E78C8D`) and a glossy white check glyph, presenting a satisfying tactile bounce on toggle.