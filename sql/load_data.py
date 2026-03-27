import pandas as pd
import sqlite3
import os

# ── 1. LOAD RAW DATA ──────────────────────────────────────────────
print("Loading raw data...")
df = pd.read_csv("data/raw/ipl.csv", low_memory=False)
print(f"Raw shape: {df.shape}")

# ── 2. CLEAN COLUMN NAMES ─────────────────────────────────────────
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("'", "")
    .str.replace("/", "_")
)

# Remove duplicate/unnamed columns
df = df.loc[:, ~df.columns.str.startswith("unnamed")]
df = df.loc[:, ~df.columns.duplicated()]
print(f"After column cleanup: {df.shape}")

# ── 3. FIX DATA TYPES ─────────────────────────────────────────────
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["season"] = df["date"].dt.year

int_cols = [
    "innings", "over", "ball", "ball_no", "runs_batter",
    "balls_faced", "runs_extras", "runs_total", "runs_bowler",
    "valid_ball", "team_balls", "team_wicket",
    "batter_runs", "batter_balls", "bowler_wicket"
]
for col in int_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)

bool_cols = ["striker_out"]
for col in bool_cols:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip().str.lower().map(
            {"true": True, "false": False, "1": True, "0": False}
        )

# ── 4. HANDLE MISSING VALUES ──────────────────────────────────────
df["wicket_kind"]  = df["wicket_kind"].fillna("none")
df["player_out"]   = df["player_out"].fillna("none")
df["fielders"]     = df["fielders"].fillna("none")
df["extra_type"]   = df["extra_type"].fillna("none")

# ── 5. REMOVE JUNK ROWS ───────────────────────────────────────────
before = len(df)
df = df.dropna(subset=["match_id", "batter", "bowler"])
print(f"Dropped {before - len(df)} junk rows. Clean shape: {df.shape}")

# ── 6. SAVE CLEANED CSV ───────────────────────────────────────────
os.makedirs("data/processed", exist_ok=True)
df.to_csv("data/processed/ipl_clean.csv", index=False)
print("✅ Saved: data/processed/ipl_clean.csv")

# ── 7. LOAD INTO SQLITE DATABASE ──────────────────────────────────
print("\nLoading into SQLite database...")
conn = sqlite3.connect("data/ipl.db")

# Main deliveries table
df.to_sql("deliveries", conn, if_exists="replace", index=False)
print("✅ Table created: deliveries")

# ── 8. CREATE SUMMARY VIEWS ───────────────────────────────────────

# Batting summary per player per season
conn.execute("DROP VIEW IF EXISTS batting_stats")
conn.execute("""
    CREATE VIEW batting_stats AS
    SELECT
        batter,
        season,
        batting_team,
        COUNT(DISTINCT match_id)            AS matches,
        SUM(runs_batter)                    AS total_runs,
        SUM(valid_ball)                     AS balls_faced,
        SUM(CASE WHEN runs_batter = 4 THEN 1 ELSE 0 END) AS fours,
        SUM(CASE WHEN runs_batter = 6 THEN 1 ELSE 0 END) AS sixes,
        MAX(batter_runs)                    AS highest_score,
        ROUND(
            CAST(SUM(runs_batter) AS FLOAT) /
            NULLIF(SUM(valid_ball), 0) * 100, 2
        )                                   AS strike_rate
    FROM deliveries
    WHERE innings IN (1, 2)
    GROUP BY batter, season, batting_team
""")
print("✅ View created: batting_stats")

# Bowling summary per player per season
conn.execute("DROP VIEW IF EXISTS bowling_stats")
conn.execute("""
    CREATE VIEW bowling_stats AS
    SELECT
        bowler,
        season,
        bowling_team,
        COUNT(DISTINCT match_id)            AS matches,
        SUM(valid_ball)                     AS balls_bowled,
        ROUND(SUM(valid_ball) / 6.0, 1)    AS overs_bowled,
        SUM(runs_bowler)                    AS runs_given,
        SUM(bowler_wicket)                  AS wickets,
        ROUND(
            CAST(SUM(runs_bowler) AS FLOAT) /
            NULLIF(SUM(valid_ball) / 6.0, 0), 2
        )                                   AS economy_rate,
        ROUND(
            CAST(SUM(valid_ball) AS FLOAT) /
            NULLIF(SUM(bowler_wicket), 0), 2
        )                                   AS bowling_average
    FROM deliveries
    WHERE innings IN (1, 2)
    GROUP BY bowler, season, bowling_team
""")
print("✅ View created: bowling_stats")

# Match-level summary
conn.execute("DROP VIEW IF EXISTS match_summary")
conn.execute("""
    CREATE VIEW match_summary AS
    SELECT
        match_id,
        date,
        season,
        match_type,
        event_name,
        batting_team,
        innings,
        SUM(runs_total)     AS total_runs,
        SUM(team_wicket)    AS total_wickets,
        MAX(over) + 1       AS overs_played
    FROM deliveries
    GROUP BY match_id, date, season, match_type, event_name, batting_team, innings
""")
print("✅ View created: match_summary")

conn.commit()
conn.close()

print("\n🎉 Phase 1 Complete!")
print("   → Cleaned CSV : data/processed/ipl_clean.csv")
print("   → SQLite DB   : data/ipl.db  (tables: deliveries | views: batting_stats, bowling_stats, match_summary)")
print("\nNext step: open notebooks/01_eda.ipynb")
