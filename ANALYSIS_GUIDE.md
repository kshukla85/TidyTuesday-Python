# Anime Dataset Analysis Guide

## Overview

This guide provides detailed information about the anime dataset analysis performed using pandas in Python.

## Dataset Description

The dataset contains **50 anime entries** with the following attributes:

| Column | Type | Description |
|--------|------|-------------|
| anime_id | int | Unique identifier for each anime |
| name | string | Title of the anime |
| genre | string | Genres (pipe-separated, e.g., "Action\|Adventure") |
| type | string | Format (TV series or Movie) |
| episodes | int | Number of episodes |
| rating | float | Rating score (0-10 scale) |
| members | int | Number of community members/fans |
| year | int | Release year |
| studio | string | Production studio |

## Analysis Sections

### 1. Data Exploration
- **Purpose**: Understand the structure and quality of the dataset
- **Key Findings**:
  - 50 anime entries with 9 columns
  - No missing values (100% data completeness)
  - No duplicate entries
  - Data types are correctly assigned

### 2. Descriptive Statistics
- **Purpose**: Summarize the central tendencies and distributions
- **Key Metrics**:
  - Average rating: 8.52 (high-quality selection)
  - Median episodes: 24.5
  - Total community members: 27,960,609
  - Year range: 1989-2020 (31 years of anime history)

### 3. Rating Analysis
- **Purpose**: Identify quality trends and top-performing anime
- **Insights**:
  - Top-rated: Fullmetal Alchemist: Brotherhood (9.26)
  - Movies have higher average ratings (8.99) than TV series (8.49)
  - Top studios by rating: CoMix Wave Films, Studio Ghibli, Sunrise

### 4. Popularity Analysis
- **Purpose**: Understand audience engagement patterns
- **Insights**:
  - Most popular: Sword Art Online (987,654 members)
  - Weak negative correlation between rating and popularity (-0.119)
  - TV series slightly more popular on average than movies

### 5. Episode Analysis
- **Purpose**: Examine content length patterns
- **Insights**:
  - Range: 1 episode (movies) to 1000 episodes (One Piece)
  - Average TV series: 70 episodes
  - Most common range: 12-26 episodes (single season)

### 6. Yearly Trends
- **Purpose**: Track anime production and quality over time
- **Insights**:
  - Peak production years: 2016 (6 anime), 2019 (5 anime)
  - Average quality improving in recent years
  - 2018 shows highest average rating (8.71)

### 7. Genre Analysis
- **Purpose**: Identify popular themes and categories
- **Insights**:
  - Most common genre: Action (29 occurrences)
  - Top 5: Action, Drama, Adventure, Fantasy, Comedy
  - 28 unique genres in total
  - Many anime combine multiple genres

## Visualizations

### 1. Rating Distribution (`rating_distribution.png`)
Shows the frequency distribution of anime ratings. Most anime cluster in the 8.0-9.0 range, indicating a high-quality dataset.

### 2. Type Distribution (`type_distribution.png`)
Displays the split between TV series (47) and Movies (3). TV series dominate the dataset.

### 3. Rating vs Members (`rating_vs_members.png`)
Scatter plot showing the relationship between rating and popularity. Reveals that high ratings don't always correlate with high popularity.

### 4. Top Studios (`top_studios.png`)
Horizontal bar chart of the 10 most productive studios. Madhouse leads with 7 anime.

### 5. Episodes Distribution (`episodes_distribution.png`)
Histogram of episode counts (filtered to ≤100 for clarity). Shows most anime have 12-26 episodes.

## Key Insights

1. **Quality Over Quantity**: The dataset represents high-quality anime with an average rating of 8.52/10
2. **Studio Excellence**: Certain studios (Madhouse, Studio Pierrot, Kyoto Animation) are consistently productive
3. **Genre Diversity**: Action and Drama are the most popular genres, but anime often blend multiple genres
4. **Format Preference**: TV series are much more common than movies (94% vs 6%)
5. **Recent Trends**: Modern anime (2015-2020) maintain high quality with increasing production

## Running the Analysis

```bash
# Install dependencies
pip install -r requirements.txt

# Run the analysis
python anime_analysis.py
```

## Extending the Analysis

You can extend this analysis by:

1. **Adding More Data**: Include additional anime entries
2. **Time Series Analysis**: Analyze trends over decades
3. **Genre Deep Dive**: Analyze specific genres in detail
4. **Studio Comparison**: Compare studios by various metrics
5. **Predictive Modeling**: Build models to predict ratings or popularity

## Data Source Note

This dataset contains sample data for demonstration purposes. For production analysis, consider using larger datasets from sources like MyAnimeList or AniList APIs.

## Requirements

- Python 3.7+
- pandas >= 2.0.0
- numpy >= 1.24.0
- matplotlib >= 3.7.0
- seaborn >= 0.12.0

## License

This project is open source and available under the terms in the LICENSE file.
