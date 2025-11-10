import pandas as pd

# --- 1️⃣ Load the data ---
anime = pd.read_csv("/Users/kunalshukla/Desktop/TidyTuesday-Python-1/py1/data/anime.csv")
animelist = pd.read_csv("/Users/kunalshukla/Desktop/TidyTuesday-Python-1/py1/data/animelist.csv")
anime_with_synopsis = pd.read_csv("/Users/kunalshukla/Desktop/TidyTuesday-Python-1/py1/data/anime_with_synopsis.csv")
anime_rating = pd.read_csv("/Users/kunalshukla/Desktop/TidyTuesday-Python-1/py1/data/rating_complete.csv")
anime_watching_status = pd.read_csv("/Users/kunalshukla/Desktop/TidyTuesday-Python-1/py1/data/watching_status.csv")

print("✅ Data loaded successfully!")
print(f"Rows: {len(anime)}, Columns: {len(anime.columns)}\n")

# --- 2️⃣ Quick look ---
print("🔹 anime:")
print(anime.head(), "\n")
print("🔹 animelist:")
print(animelist.head(), "\n")
print("🔹 anime_rating:")
print(anime_rating.head(), "\n")
print("🔹 anime_watching_status:")
print(anime_watching_status.head(10), "\n")

anime["Score"] = pd.to_numeric(anime["Score"], errors = "coerce")
anime["Episodes"] = pd.to_numeric(anime["Episodes"], errors = "coerce")

# --- 3️⃣ Aggregate example ---
# Group by anime name and summarize key metrics
watch_agg = anime.groupby("Name").agg(
    avg_score=("Score", "mean"),
    num_genres=("Genres", "nunique"),
    total_episodes=("Episodes", "sum")
).reset_index()

# Optional derived metric: score per genre
watch_agg["score_per_genre"] = watch_agg["avg_score"] / watch_agg["num_genres"]

print("✅ Aggregation complete!")
print(watch_agg.head(10))
