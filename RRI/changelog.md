# 📘 Reliever Reliability Index (RRI) – Changelog

> **Project**: [xSTATx ⚾ Advanced Bullpen Analytics]  
> **Component**: RRI (Reliever Reliability Index)  
> **Maintainer**: [Strik3 | Projxbyme](https://github.com/Nickolai-Brennan/Projx2025)

---

## 📌 Version History

---

### ⚙️ `v1.0.0` – **Initial Release**
**Date**: `2024-03-15`

- 🚀 Introduced core **RRI tiers and scoring ranges** (0–100).
- ✅ Created baseline role classifications (Closers, Setup, Mid Relief, Mop-up).
- 🧠 Scoring driven by:
  - ERA
  - WHIP
  - K/BB
  - Saves & Holds
  - Leverage Index
- 🧪 Introduced **first RRI certification rule** for rookie call-ups.

---

### ⚙️ `v1.1.0` – **Metric Expansion Update**
**Date**: `2024-03-22`

- ➕ Added `xFIP`, `SIERA`, `CSW%` to performance metrics.
- 🧮 Built-in **Prospect Boost System** (+8 for Top 50).
- 🛑 ERA scaling penalties added for 5.00+ ERA.
- 🎯 Added "Trade Rumors Badge" with tiered penalty logic.

---

### ⚙️ `v1.2.0` – **Role & Usage Calibration**
**Date**: `2024-04-01`

- 🔁 Replaced fixed roles with dynamic role tiers based on `Avg_LI`.
- 📈 Added `pLI`, `gmLI`, `inLI` to track real-world leverage usage.
- 🧰 Role Versatility Bonus added:
  - 10+ multi-role appearances: +3
  - 15+: +5
- 🧩 Integrated "High-Leverage Relief" role classification.

---

### ⚙️ `v1.3.0` – **Stuff Quality Module**
**Date**: `2024-04-10`

- 🎯 Incorporated:
  - `Stuff+`
  - `Location+`
  - `Pitching+`
- 📊 Tiered scoring logic:
  - >130 = +4.0
  - >140 = +6.0
- 🌪️ Added Pitch-Specific Spin Rate bonuses for Top 5% / Top 10%.

---

### ⚙️ `v1.4.0` – **Clutch & Team Context Logic**
**Date**: `2024-04-14`

- 🧠 Added:
  - `Clutch Score`
  - `Inherited Runners` % & impact
- 🔄 Team Standing Bonus:
  - 1st Place = +4
  - 5th = -1
- 🔥 “RRI_Standings” tier system finalized.

---

### ⚙️ `v1.5.0` – **RRI Fantasy $Value Model**
**Date**: `2024-04-18`

- 💰 Scaled fantasy value with:
  - SV × 1.5
  - HLD × 1.0
  - +CSW%, stranded runners, xwOBA
- 🎖️ Introduced `$20 cap` and top 5% elite valuation badge.

---

### ⚙️ `v2.0.0` – **Weighted Formula Revamp**
**Date**: `2024-04-22`

- 🧪 Full RRI breakdown:
  - 25% Previous Year
  - 50% Current Season
  - 25% Non-Playing Stats
- 📐 Current Season RRI:
  - 30% Performance
  - 20% Leverage
  - 15% SV/HLD
  - 15% Stuff/Pitch Quality
  - 10% Batted Ball (CSW%)
  - 10% Clutch & IR
- 🎭 Non-Playing Stats:
  - Prospect Rank, Injury, Trade Rumors, Age, Role

---

### ⚙️ `v2.1.0` – **Decay & Trends Integration**
**Date**: `2024-04-27`

- 📉 Added **Decay Over Time** for long-term regressions.
- 📈 Highlighted Notable Metric Trends (+/- over rolling 30-day span).
- 🧠 Initiated **Decay Factor Memory** for prior injuries and role demotions.

---

### ⚙️ `v2.2.0` – **Dashboard + Export Tools**
**Date**: `2025-04-29`

- 🧾 Live RRI Table with:
  - Sorting, search, elite filters
  - Team logos, role type icons
- 📤 CSV + HTML export formats enabled.
- 🎨 Full leaderboard with badge and shadow visuals deployed.

---

### ⚙️ `v2.3.0` – **Master Player Table Integration**
**Date**: `2025-05-01`

- 🔗 Unified identity system via:
  - `xSTATx_ID`, `Fangraphs_ID`, `MLB_ID`, `BR_ID`
- 🗂️ Created lookup-matching protocol for historical consistency.
- 📌 Integrated into GitHub + Databricks pipeline.

---

## 🔮 Coming Soon

- `v2.4.0` – **Machine Learning Prospect Projection**  
  - Predict call-up RRI based on MiLB stuff metrics & team opportunity

- `v3.0.0` – **RRI Auto-Predictive Simulator**  
  - Automate weekly projections & role change alerts

---

## 🛠️ Core Component Legend

| Component | Description |
|----------|-------------|
| `RRI_Current_Season` | 6-part weighted formula (performance to clutch) |
| `RRI_Prev_Season` | Prior year end RRI score |
| `RRI_NonPlaying` | Contextual factors: prospect, injuries, role, age |
| `RRI_StuffScore` | Blend of Stuff+, Pitching+, Location+, Spin Rates |
| `RRI_Leverage` | Based on Avg_LI + real game usage |
| `RRI_SVH` | Role reliability through SV%, HLD%, IR% |
| `RRI_BattedBall` | CSW%, Barrel%, Soft/Hard contact |
| `RRI_ClutchIR` | Clutch index and inherited runners scored |
| `RRI_Standings` | Team ranking boost/penalty |

