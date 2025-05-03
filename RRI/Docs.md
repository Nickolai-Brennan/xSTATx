# 📘 RRI (Reliever Reliability Index) – Knowledge Base

Welcome to the **RRI Knowledge Base**, your centralized documentation for everything related to the **Reliever Reliability Index**, a proprietary bullpen evaluation system developed by **xSTATx / Strik3**.

---

## 📌 What is RRI?

The **Reliever Reliability Index (RRI)** is a dynamic score (0–125+) that evaluates MLB and MiLB relievers based on performance, role, team context, and advanced analytics. It is used for fantasy baseball projections, scouting, and real-time bullpen tracking.

RRI = **(0.25 × Previous Year Score) + (0.50 × Current Season Score) + (0.25 × Non-Playing Score)**

It accounts for both quantitative production and qualitative context to produce a reliability score that scales with role security, consistency, and team demand.

---

## 🎯 Use Cases

- 🧢 Fantasy Baseball Rankings
- 📊 Bullpen Depth Chart Creation
- 🔁 Trade Value Estimation
- 🔮 Prospect Projection (MiLB ➜ MLB)
- ⚙️ Scouting and Team Fit Analysis
- 📈 In-Season Tracking and Role Monitoring
- 📉 Historical Decay and Injury Trend Evaluations

---

## 🔍 Key Formula Components

### 🔹 RRI_Current_Season (50%)
This is the most dynamic and weighty portion of the RRI, reflecting how a pitcher is currently performing and being used.

- **Performance Metrics (30%)**
  - ERA, xFIP, WHIP, K/9, BB/9, K%, BB%, K-BB%
  - Scaled using league percentiles with strong bonuses for elite ratios (e.g., ERA < 2.50)

- **Leverage & Usage (20%)**
  - Avg_LI, pLI, gmLI, inLI, leverage zone counts
  - Contextual roles derived from real game pressure situations

- **Saves & Holds (15%)**
  - Save %, Hold %, Inherited Runners %, usage with lead/tie
  - SVH3 Score = (SV × 1.5 + HLD × 1.0) capped at 10 pts

- **Stuff Quality (15%)**
  - Stuff+, Location+, Pitching+, Pitch-Specific Spin Rate
  - Weighted toward elite percentile tiers with compound bonuses for Top 5% results

- **Batted Ball / Plate Discipline (10%)**
  - CSW%, Barrel%, Soft%, Hard%, SwStr%, Contact%
  - Lower Barrel/HardHit% boosts consistency grade

- **Clutch & Inherited Runners (10%)**
  - Performance in tight late-game scenarios
  - Preventing IR scoring and excelling in 1-run or tie games

### 🔹 RRI_Previous_Season (25%)
Carries over historical reliability. Prevents extreme one-week swings and helps stabilize elite pitchers with track records.

- Frozen at final RRI score from previous year
- Greatly benefits consistent setup men and closers

### 🔹 RRI_NonPlaying_Score (25%)
Evaluates off-field, developmental, and context-based data:

- **Prospect Status (5%)**
  - Based on MLB Pipeline, Fangraphs, and internal xSTATx scores
- **Injury History (5%)**
  - Tracks recurring IL trends, arm injuries, elbow flags, and full season losses
- **Team Contention Tier (5%)**
  - Uses win %, division standing, and playoff odds
- **Trade Rumor Activity (1%)**
  - Deducts reliability due to uncertainty
- **Pitcher Type / Role (5%)**
  - Reliever classification: Closer, Setup, HL, Mid, Long
- **Age Scaling Penalty (4–5%)**
  - Begins at age 34, increases with each year over 36

---

## 🎖️ RRI Tier Definitions

| Score Range | Tier Description |
|-------------|------------------|
| 95–125+     | God Tier / Untouchable Closers 🐉 |
| 85–94       | Elite Multi-Use Relievers 🛡️ |
| 75–84       | High-Leverage, Reliable Setup Arms 🔒 |
| 60–74       | Mid-Tier / Matchup / Aging Veterans ⚖️ |
| 45–59       | Fringe Role / Blowout Arms 🚨 |
| 25–44       | Call-Ups / Risky / Likely to Be Demoted ⛓️ |

---

## 🧩 Adjustments and Bonuses

- **Prospect Boost**: Top 10 = +5, Top 100 = +2.5, Team Top 10 = +1
- **Injury Penalty**: 2+ IL stints = -3, full season = -3, recurring = -1 to -4
- **Team Standings**:
  - Top Division = +4, Contender = +3, Avg = 0, Seller = -1, Tanking = -5
- **Role Versatility**:
  - 10+ appearances = +3, 15+ appearances = +5
- **Elite Spin Rate**:
  - Top 5% = +2.5 per pitch, Top 10% = +1.0
- **Stuff+ / Location+ / Pitching+ Tier Bonuses**:
  - >100 = +0.25, >110 = +0.5, >120 = +2.0, >135 = +5.0, >140 = +6.0

---

## 📈 RRI Data Tables

Data is refreshed **weekly** via Python + Google Sheets + Databricks integration. Tables include:

- 🔹 Player Identity (Name, ID, Team, Hand, Role)
- 🔹 Pitching Stats (ERA, xFIP, WHIP, K%, BB%, CSW%)
- 🔹 Usage Metrics (IP, aLI, gmLI, SV/HLD, IR%)
- 🔹 Stuff Scores (Stuff+, Spin Rate, Location+, Pitching+)
- 🔹 Fantasy Projections ($Value Cap = $20)

Interactive HTML Leaderboards with filters, icons, and badges are hosted via WordPress.

---

## 🧠 Machine Learning Roadmap

- **RRI Projection Model**:
  - Predict initial MLB RRI for MiLB pitchers using stuff, age, usage, org depth

- **Decay Tracking Module**:
  - Analyzes long-term drop-off risk via stuff fade, injury spikes, command regression

- **Role Prediction Engine**:
  - Classifies relievers by current usage, LI windows, team need, and velocity trends

---

## 🤝 Contact & Contribution

- GitHub: [Projxbyme – RRI Module](https://github.com/Nickolai-Brennan/Projx2025)
- Maintained by: **@Nickolai-Brennan**
- Suggest improvements, open issues, or submit pull requests for:
  - ⚗️ Formula Tuning
  - 🎨 Leaderboard UI Enhancements
  - 📦 Data Table Integration

---

*RRI is a flagship tool within the xSTATx Advanced Bullpen Analytics System. Trusted by fantasy analysts, scouts, and data professionals.*

