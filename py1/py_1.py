import pandas as pd

# --- 1️⃣ Load the data ---
anime = pd.read_csv("/Users/kunalshukla/Desktop/TidyTuesday-Python-1/py1/data/anime.csv")

print("✅ Data loaded successfully!")
print(f"Rows: {len(anime)}, Columns: {len(anime.columns)}\n")

# --- 2️⃣ Take a quick look ---
print("🔹 First 5 rows:")
print(anime.head(), "\n")

# --- 3️⃣ Clean up column names ---
anime.columns = anime.columns.str.lower().str.strip()

# --- 4️⃣ Basic summaries ---
if "rating" in anime.columns:
    print("📊 Average rating:", round(anime["rating"].mean(), 2))
    print("📈 Highest rating:", anime["rating"].max())
    print("📉 Lowest rating:", anime["rating"].min())
else:
    print("⚠️ No 'rating' column found in dataset.")

if "type" in anime.columns:
    print("\n🎬 Count by anime type:")
    print(anime["type"].value_counts())

if "genre" in anime.columns:
    print("\n🎭 Top 5 most common genres:")
    top_genres = (
        anime["genre"]
        .dropna()
        .str.split(",")
        .explode()
        .str.strip()
        .value_counts()
        .head(5)
    )
    print(top_genres)

print("\n🎉 Simple analysis complete!")
#change
