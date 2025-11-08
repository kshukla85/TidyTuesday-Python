# Anime Dataset Analysis with Python Pandas

This project demonstrates comprehensive data analysis of an anime dataset using Python and the pandas library. The analysis includes data exploration, statistical analysis, and visualization of anime trends, ratings, popularity, and more.

## Dataset

The dataset contains information about 50 popular anime titles, including:
- **anime_id**: Unique identifier for each anime
- **name**: Title of the anime
- **genre**: Genre(s) of the anime
- **type**: Format (TV series or Movie)
- **episodes**: Number of episodes
- **rating**: User rating (out of 10)
- **members**: Number of community members
- **year**: Release year
- **studios**: Production studio

The dataset was created using `create_anime_dataset.py` and includes a diverse selection of popular anime from different decades and genres.

## Files

- `create_anime_dataset.py` - Script to generate the anime dataset
- `anime.csv` - The anime dataset (generated)
- `analyze_anime.py` - Main analysis script using pandas
- `plots/` - Directory containing generated visualizations
- `README.md` - This file

## Requirements

Install the required Python packages:

```bash
pip install -r ../requirements.txt
```

Required packages:
- pandas >= 2.0.0
- numpy >= 1.24.0
- matplotlib >= 3.7.0
- seaborn >= 0.12.0
- requests >= 2.31.0

## Usage

### 1. Generate the Dataset (if needed)

```bash
python create_anime_dataset.py
```

This creates `anime.csv` with 50 anime entries.

### 2. Run the Analysis

```bash
python analyze_anime.py
```

This script performs:
- **Data Loading**: Reads the CSV file
- **Data Exploration**: Displays dataset structure, statistics, and info
- **Rating Analysis**: Analyzes rating distributions and top-rated anime
- **Type Analysis**: Compares TV series vs Movies
- **Temporal Analysis**: Examines trends over time
- **Studio Analysis**: Identifies top studios and their performance
- **Popularity Analysis**: Analyzes member counts and correlations
- **Genre Analysis**: Breaks down genre distributions
- **Visualization**: Creates 5 plots saved to `plots/` directory

## Analysis Results

The analysis provides insights into:

### Key Findings

- **Dataset Size**: 50 anime titles spanning 1989-2022
- **Average Rating**: 8.44/10
- **Highest Rated**: Fullmetal Alchemist: Brotherhood (9.1/10)
- **Most Popular**: Death Note (2.5M members)
- **Most Prolific Studio**: Madhouse (7 titles)
- **Most Common Genre**: Action (25 occurrences)

### Visualizations

The analysis generates 5 visualization plots:

1. **rating_distribution.png** - Histogram showing the distribution of anime ratings
2. **rating_vs_members.png** - Scatter plot comparing ratings with popularity
3. **anime_by_year.png** - Bar chart showing anime count by release year
4. **rating_by_type.png** - Average ratings for TV vs Movie format
5. **top_studios.png** - Top 10 animation studios by number of titles

## Pandas Operations Demonstrated

This project showcases various pandas functionalities:

- **Data Loading**: `pd.read_csv()`
- **Data Exploration**: `.head()`, `.info()`, `.describe()`, `.dtypes`
- **Data Cleaning**: `.isnull()`, `.sum()`
- **Aggregation**: `.groupby()`, `.agg()`
- **Sorting**: `.sort_values()`, `.nlargest()`, `.nsmallest()`
- **Statistical Analysis**: `.mean()`, `.median()`, `.std()`, `.corr()`
- **Data Transformation**: `pd.cut()`, string manipulation
- **Filtering**: Boolean indexing
- **Visualization Integration**: With matplotlib and seaborn

## Example Output

```
======================================================================
ANIME DATASET ANALYSIS WITH PANDAS
======================================================================

📊 Dataset Overview:
   • Total Anime: 50
   • Date Range: 1989 - 2022
   • Average Rating: 8.44/10
   • Total Members: 59,800,000

🏆 Top Performers:
   • Highest Rated: Fullmetal Alchemist: Brotherhood (9.1/10)
   • Most Popular: Death Note (2,500,000 members)

🎬 Content Types:
   • TV: 45
   • Movie: 5

🏢 Production:
   • Number of Studios: 24
   • Most Prolific Studio: Madhouse
```

## Future Enhancements

Possible extensions to this analysis:
- Sentiment analysis of anime descriptions
- Machine learning to predict ratings
- Time series analysis of popularity trends
- Network analysis of studio collaborations
- Comparison with real-world datasets from MyAnimeList or AniList APIs

## License

This project is part of the TidyTuesday-Python repository. The dataset is created for educational purposes based on publicly available information about popular anime.

## Author

Created as a demonstration of pandas data analysis capabilities for anime datasets.
