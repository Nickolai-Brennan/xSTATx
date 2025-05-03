Absolutely. Here's a **detailed color scheme and typography section** tailored for your projects (e.g., xSTATx, FBCS by Strik3, Alligrator), with visual clarity and brand consistency in mind.

---

# 🎨 Project Style Guide  
## Section 1: Color Scheme & Typography

---

## 🎨 Color Scheme

| Color Role         | Hex Code   | RGB Values          | Use Case                                                        |
|--------------------|------------|----------------------|------------------------------------------------------------------|
| **Primary Dark**   | `#121212`  | `rgb(18, 18, 18)`    | Page background, cards, containers, body elements                |
| **Accent Gold**    | `#f6b003`  | `rgb(246, 176, 3)`   | Highlights, badges, buttons, active tabs, leaderboard headings   |
| **Secondary Gray** | `#1f1f1f`  | `rgb(31, 31, 31)`    | Table rows, panel background, code blocks                        |
| **Text Light**     | `#ffffff`  | `rgb(255, 255, 255)` | Main body and headline text on dark backgrounds                  |
| **Text Muted**     | `#aaaaaa`  | `rgb(170, 170, 170)` | Subtext, label elements, hint text                               |
| **Table Highlight**| `#2e2e2e`  | `rgb(46, 46, 46)`    | Hover rows, card emphasis                                        |
| **Positive Green** | `#00c853`  | `rgb(0, 200, 83)`    | Metrics: Elite score badges, positive value swings               |
| **Warning Red**    | `#ff5252`  | `rgb(255, 82, 82)`   | Injury flags, trade rumor icons, score drop alerts               |
| **Neutral Blue**   | `#03a9f4`  | `rgb(3, 169, 244)`   | Player links, interaction highlights, clickable icons            |
| **Badge Silver**   | `#d4d4d4`  | `rgb(212, 212, 212)` | Outlines for Top 5% badges, tooltip borders                      |

### 🔁 Suggested Gradients
- **Header Gradient:** `linear-gradient(135deg, #1f1f1f, #121212)`
- **Gold Accent Hover:** `linear-gradient(90deg, #f6b003, #ffd95a)`

---

## ✍️ Typography

### Font Stack
```css
font-family: 'Inter', 'Barlow Condensed', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;
```

---

### 🔤 Primary Fonts

| Font Family         | Role                  | Weight(s) Used | Google Fonts URL                                                                 |
|---------------------|------------------------|----------------|----------------------------------------------------------------------------------|
| **Barlow Condensed**| Headers / Display Text | 600 (SemiBold) | [https://fonts.google.com/specimen/Barlow+Condensed](https://fonts.google.com/specimen/Barlow+Condensed) |
| **Inter**           | Body / Labels          | 400, 500, 600  | [https://fonts.google.com/specimen/Inter](https://fonts.google.com/specimen/Inter) |

---

### 🧱 Typography Hierarchy

| Element            | Font            | Weight | Size        | Line Height | Usage Example                        |
|--------------------|------------------|--------|-------------|-------------|--------------------------------------|
| H1 / Main Titles   | Barlow Condensed | 600    | 32–36px     | 1.2         | “Reliever Reliability Index 2025”    |
| H2 / Section Header| Barlow Condensed | 600    | 24–28px     | 1.3         | “Team Performance Metrics”           |
| H3 / Subheader     | Inter            | 600    | 20–22px     | 1.3         | “Spin Rate Leaders”                  |
| Body Text          | Inter            | 400    | 14–16px     | 1.6         | Descriptions, Stats, Player Notes    |
| Captions / Labels  | Inter            | 400    | 12–13px     | 1.4         | Tooltip Text, Stat Column Labels     |
| Buttons / Badges   | Inter            | 600    | 14px (all-caps) | 1.2     | “View Profile”, “Top 5%”, “Injury”   |

---

### 🧩 Font Usage Rules
- **Never mix** Barlow Condensed in body paragraphs – reserve it for headlines or emphasis.
- Use **uppercase and tighter letter-spacing** (`letter-spacing: 0.05em`) for leaderboard/table headers and buttons.
- Stick to **monospace or Inter** for code, formulas, or numbers if used in documentation or analytics.
- Avoid font overload. Two primary families is the cap.

---

Would you like this exported as a reusable HTML+CSS block or GitHub markdown theme snippet?
