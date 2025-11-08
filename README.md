# TidyTuesday-Python

My own side projects

## Anime Dataset Analysis

A comprehensive data analysis project using pandas in Python to analyze anime data. This project demonstrates various data analysis techniques including exploratory data analysis, statistical analysis, and data visualization.

### Features

- **Data Exploration**: Load and explore the anime dataset
- **Descriptive Statistics**: Calculate summary statistics and distributions
- **Rating Analysis**: Analyze anime ratings and identify top-rated shows
- **Popularity Analysis**: Examine anime popularity based on member counts
- **Episode Analysis**: Study episode distributions across different anime types
- **Yearly Trends**: Track anime trends over the years
- **Genre Analysis**: Explore genre distributions and patterns
- **Visualizations**: Generate informative charts and plots

### Dataset

The dataset (`data/anime_dataset.csv`) contains information about 50 anime titles with the following attributes:
- `anime_id`: Unique identifier
- `name`: Anime title
- `genre`: Genres (pipe-separated)
- `type`: Type (TV, Movie, etc.)
- `episodes`: Number of episodes
- `rating`: Rating score (0-10)
- `members`: Number of members/fans
- `year`: Release year
- `studio`: Production studio

### Installation

1. Clone the repository:
```bash
git clone https://github.com/kshukla85/TidyTuesday-Python.git
cd TidyTuesday-Python
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

### Usage

Run the analysis script:
```bash
python anime_analysis.py
```

The script will:
1. Load the anime dataset
2. Perform comprehensive data analysis
3. Display statistics and insights in the console
4. Generate visualization plots (PNG files)

### Output

The analysis generates the following visualizations:
- `rating_distribution.png`: Distribution of anime ratings
- `type_distribution.png`: Distribution of anime types
- `rating_vs_members.png`: Relationship between rating and popularity
- `top_studios.png`: Top studios by number of anime produced
- `episodes_distribution.png`: Distribution of episode counts

### Requirements

- Python 3.7+
- pandas >= 2.0.0
- numpy >= 1.24.0
- matplotlib >= 3.7.0
- seaborn >= 0.12.0

### Project Structure

```
TidyTuesday-Python/
├── data/
│   └── anime_dataset.csv      # Anime dataset
├── anime_analysis.py           # Main analysis script
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
└── .gitignore                  # Git ignore file
```

### Analysis Sections

1. **Data Exploration**: Overview of the dataset structure and contents
2. **Descriptive Statistics**: Summary statistics for all numerical features
3. **Rating Analysis**: Insights into anime ratings and quality
4. **Popularity Analysis**: Understanding what makes anime popular
5. **Episode Analysis**: Episode count patterns and distributions
6. **Yearly Trends**: How anime production and quality evolved over time
7. **Genre Analysis**: Most popular genres and genre combinations
8. **Visualizations**: Visual representations of key findings

### Contributing

Feel free to fork this repository and submit pull requests for any improvements.

### License

This project is licensed under the terms specified in the LICENSE file.
