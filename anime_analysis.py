"""
Anime Dataset Analysis using Pandas
====================================
This script performs comprehensive data analysis on an anime dataset.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


def load_data(filepath):
    """
    Load the anime dataset from CSV file.
    
    Args:
        filepath (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Loaded anime dataset
    """
    print("Loading anime dataset...")
    df = pd.read_csv(filepath)
    print(f"Dataset loaded successfully with {len(df)} rows and {len(df.columns)} columns.\n")
    return df


def explore_data(df):
    """
    Perform initial data exploration.
    
    Args:
        df (pd.DataFrame): Anime dataset
    """
    print("=" * 80)
    print("DATA EXPLORATION")
    print("=" * 80)
    
    print("\n1. First few rows of the dataset:")
    print(df.head())
    
    print("\n2. Dataset information:")
    print(df.info())
    
    print("\n3. Dataset shape:")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    
    print("\n4. Column names:")
    print(df.columns.tolist())
    
    print("\n5. Data types:")
    print(df.dtypes)
    
    print("\n6. Missing values:")
    print(df.isnull().sum())
    
    print("\n7. Duplicate rows:")
    print(f"Number of duplicates: {df.duplicated().sum()}")
    

def descriptive_statistics(df):
    """
    Calculate and display descriptive statistics.
    
    Args:
        df (pd.DataFrame): Anime dataset
    """
    print("\n" + "=" * 80)
    print("DESCRIPTIVE STATISTICS")
    print("=" * 80)
    
    print("\n1. Summary statistics for numerical columns:")
    print(df.describe())
    
    print("\n2. Average rating:")
    print(f"{df['rating'].mean():.2f}")
    
    print("\n3. Median episodes:")
    print(f"{df['episodes'].median():.0f}")
    
    print("\n4. Total members across all anime:")
    print(f"{df['members'].sum():,}")
    
    print("\n5. Rating distribution:")
    print(df['rating'].value_counts().sort_index())
    
    print("\n6. Type distribution:")
    print(df['type'].value_counts())
    
    print("\n7. Top 5 studios by number of anime:")
    studio_counts = df['studio'].value_counts().head()
    print(studio_counts)
    

def analyze_ratings(df):
    """
    Analyze anime ratings.
    
    Args:
        df (pd.DataFrame): Anime dataset
    """
    print("\n" + "=" * 80)
    print("RATING ANALYSIS")
    print("=" * 80)
    
    print("\n1. Top 10 highest-rated anime:")
    top_rated = df.nlargest(10, 'rating')[['name', 'rating', 'type', 'year']]
    print(top_rated.to_string(index=False))
    
    print("\n2. Average rating by type:")
    avg_rating_by_type = df.groupby('type')['rating'].mean().sort_values(ascending=False)
    print(avg_rating_by_type)
    
    print("\n3. Average rating by studio (top 10):")
    avg_rating_by_studio = df.groupby('studio')['rating'].mean().sort_values(ascending=False).head(10)
    print(avg_rating_by_studio)
    

def analyze_popularity(df):
    """
    Analyze anime popularity based on member count.
    
    Args:
        df (pd.DataFrame): Anime dataset
    """
    print("\n" + "=" * 80)
    print("POPULARITY ANALYSIS")
    print("=" * 80)
    
    print("\n1. Top 10 most popular anime (by members):")
    top_popular = df.nlargest(10, 'members')[['name', 'members', 'rating', 'year']]
    print(top_popular.to_string(index=False))
    
    print("\n2. Average members by type:")
    avg_members_by_type = df.groupby('type')['members'].mean().sort_values(ascending=False)
    print(avg_members_by_type)
    
    print("\n3. Correlation between rating and members:")
    correlation = df['rating'].corr(df['members'])
    print(f"Correlation coefficient: {correlation:.3f}")
    

def analyze_episodes(df):
    """
    Analyze episode distribution.
    
    Args:
        df (pd.DataFrame): Anime dataset
    """
    print("\n" + "=" * 80)
    print("EPISODE ANALYSIS")
    print("=" * 80)
    
    print("\n1. Anime with most episodes:")
    most_episodes = df.nlargest(5, 'episodes')[['name', 'episodes', 'type', 'year']]
    print(most_episodes.to_string(index=False))
    
    print("\n2. Average episodes by type:")
    avg_episodes_by_type = df.groupby('type')['episodes'].mean().sort_values(ascending=False)
    print(avg_episodes_by_type)
    
    print("\n3. Episode statistics:")
    print(f"   Minimum: {df['episodes'].min()}")
    print(f"   Maximum: {df['episodes'].max()}")
    print(f"   Mean: {df['episodes'].mean():.1f}")
    print(f"   Median: {df['episodes'].median()}")
    

def analyze_yearly_trends(df):
    """
    Analyze trends over the years.
    
    Args:
        df (pd.DataFrame): Anime dataset
    """
    print("\n" + "=" * 80)
    print("YEARLY TRENDS")
    print("=" * 80)
    
    print("\n1. Number of anime by year (last 10 years):")
    recent_years = df[df['year'] >= df['year'].max() - 9]
    anime_per_year = recent_years['year'].value_counts().sort_index()
    print(anime_per_year)
    
    print("\n2. Average rating by year (last 10 years):")
    avg_rating_per_year = recent_years.groupby('year')['rating'].mean().sort_index()
    print(avg_rating_per_year)
    

def analyze_genres(df):
    """
    Analyze genre distribution and popularity.
    
    Args:
        df (pd.DataFrame): Anime dataset
    """
    print("\n" + "=" * 80)
    print("GENRE ANALYSIS")
    print("=" * 80)
    
    # Extract all genres
    all_genres = []
    for genres in df['genre']:
        genre_list = genres.split('|')
        all_genres.extend(genre_list)
    
    genre_series = pd.Series(all_genres)
    
    print("\n1. Most common genres:")
    print(genre_series.value_counts().head(10))
    
    print("\n2. Total unique genres:")
    print(f"{len(genre_series.unique())} unique genres")
    

def create_visualizations(df):
    """
    Create data visualizations.
    
    Args:
        df (pd.DataFrame): Anime dataset
    """
    print("\n" + "=" * 80)
    print("CREATING VISUALIZATIONS")
    print("=" * 80)
    
    # Set style
    sns.set_style("whitegrid")
    plt.rcParams['figure.figsize'] = (12, 6)
    
    # 1. Rating distribution
    plt.figure(figsize=(10, 6))
    plt.hist(df['rating'], bins=20, edgecolor='black', alpha=0.7, color='skyblue')
    plt.xlabel('Rating')
    plt.ylabel('Frequency')
    plt.title('Distribution of Anime Ratings')
    plt.grid(axis='y', alpha=0.5)
    plt.savefig('rating_distribution.png', dpi=300, bbox_inches='tight')
    print("✓ Rating distribution histogram saved as 'rating_distribution.png'")
    plt.close()
    
    # 2. Type distribution
    plt.figure(figsize=(8, 6))
    type_counts = df['type'].value_counts()
    plt.bar(type_counts.index, type_counts.values, color='coral', edgecolor='black')
    plt.xlabel('Type')
    plt.ylabel('Count')
    plt.title('Distribution of Anime Types')
    plt.xticks(rotation=45)
    plt.grid(axis='y', alpha=0.5)
    plt.savefig('type_distribution.png', dpi=300, bbox_inches='tight')
    print("✓ Type distribution bar chart saved as 'type_distribution.png'")
    plt.close()
    
    # 3. Rating vs Members scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['rating'], df['members'], alpha=0.6, color='green')
    plt.xlabel('Rating')
    plt.ylabel('Members')
    plt.title('Relationship between Rating and Popularity (Members)')
    plt.grid(alpha=0.3)
    plt.savefig('rating_vs_members.png', dpi=300, bbox_inches='tight')
    print("✓ Rating vs Members scatter plot saved as 'rating_vs_members.png'")
    plt.close()
    
    # 4. Top studios
    plt.figure(figsize=(12, 6))
    top_studios = df['studio'].value_counts().head(10)
    plt.barh(top_studios.index, top_studios.values, color='purple', edgecolor='black')
    plt.xlabel('Number of Anime')
    plt.ylabel('Studio')
    plt.title('Top 10 Studios by Number of Anime')
    plt.grid(axis='x', alpha=0.5)
    plt.savefig('top_studios.png', dpi=300, bbox_inches='tight')
    print("✓ Top studios bar chart saved as 'top_studios.png'")
    plt.close()
    
    # 5. Episodes distribution
    plt.figure(figsize=(10, 6))
    # Filter out extreme outliers for better visualization
    filtered_episodes = df[df['episodes'] <= 100]['episodes']
    plt.hist(filtered_episodes, bins=30, edgecolor='black', alpha=0.7, color='orange')
    plt.xlabel('Number of Episodes')
    plt.ylabel('Frequency')
    plt.title('Distribution of Anime Episodes (filtered to ≤100 episodes)')
    plt.grid(axis='y', alpha=0.5)
    plt.savefig('episodes_distribution.png', dpi=300, bbox_inches='tight')
    print("✓ Episodes distribution histogram saved as 'episodes_distribution.png'")
    plt.close()
    
    print("\nAll visualizations created successfully!")
    

def generate_summary_report(df):
    """
    Generate a comprehensive summary report.
    
    Args:
        df (pd.DataFrame): Anime dataset
    """
    print("\n" + "=" * 80)
    print("SUMMARY REPORT")
    print("=" * 80)
    
    print(f"""
    Total Anime: {len(df)}
    Average Rating: {df['rating'].mean():.2f}
    Highest Rating: {df['rating'].max()} ({df[df['rating'] == df['rating'].max()]['name'].values[0]})
    Lowest Rating: {df['rating'].min()} ({df[df['rating'] == df['rating'].min()]['name'].values[0]})
    
    Most Popular: {df.loc[df['members'].idxmax(), 'name']} ({df['members'].max():,} members)
    
    Most Productive Studio: {df['studio'].value_counts().index[0]} ({df['studio'].value_counts().values[0]} anime)
    
    Year Range: {df['year'].min()} - {df['year'].max()}
    
    Types: {', '.join(df['type'].unique())}
    """)
    

def main():
    """
    Main function to run the complete analysis.
    """
    print("\n" + "=" * 80)
    print("ANIME DATASET ANALYSIS WITH PANDAS")
    print("=" * 80 + "\n")
    
    # Load data
    df = load_data('data/anime_dataset.csv')
    
    # Perform analyses
    explore_data(df)
    descriptive_statistics(df)
    analyze_ratings(df)
    analyze_popularity(df)
    analyze_episodes(df)
    analyze_yearly_trends(df)
    analyze_genres(df)
    
    # Create visualizations
    create_visualizations(df)
    
    # Generate summary report
    generate_summary_report(df)
    
    print("\n" + "=" * 80)
    print("ANALYSIS COMPLETE!")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
