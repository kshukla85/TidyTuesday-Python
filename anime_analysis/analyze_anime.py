"""
Anime Dataset Analysis using Python Pandas
===========================================

This script performs comprehensive data analysis on an anime dataset,
demonstrating various pandas operations including data loading, cleaning,
exploration, grouping, and visualization.

Dataset Source: Custom generated dataset based on popular anime titles
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Set style for better-looking plots
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

def load_data(filepath='anime.csv'):
    """Load the anime dataset from CSV file."""
    print("=" * 70)
    print("LOADING ANIME DATASET")
    print("=" * 70)
    
    df = pd.read_csv(filepath)
    print(f"\nDataset loaded successfully!")
    print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    return df

def explore_data(df):
    """Perform initial data exploration."""
    print("\n" + "=" * 70)
    print("DATA EXPLORATION")
    print("=" * 70)
    
    print("\n1. First 5 rows:")
    print(df.head())
    
    print("\n2. Dataset Info:")
    print(df.info())
    
    print("\n3. Basic Statistics:")
    print(df.describe())
    
    print("\n4. Column Names:")
    print(df.columns.tolist())
    
    print("\n5. Missing Values:")
    print(df.isnull().sum())
    
    print("\n6. Data Types:")
    print(df.dtypes)

def analyze_ratings(df):
    """Analyze anime ratings."""
    print("\n" + "=" * 70)
    print("RATING ANALYSIS")
    print("=" * 70)
    
    print(f"\n1. Average Rating: {df['rating'].mean():.2f}")
    print(f"2. Median Rating: {df['rating'].median():.2f}")
    print(f"3. Rating Range: {df['rating'].min():.1f} - {df['rating'].max():.1f}")
    print(f"4. Standard Deviation: {df['rating'].std():.2f}")
    
    print("\n5. Top 10 Highest Rated Anime:")
    top_rated = df.nlargest(10, 'rating')[['name', 'rating', 'genre', 'year']]
    print(top_rated.to_string(index=False))
    
    print("\n6. Rating Distribution:")
    rating_counts = pd.cut(df['rating'], bins=[7.0, 7.5, 8.0, 8.5, 9.0, 9.5], 
                          labels=['7.0-7.5', '7.5-8.0', '8.0-8.5', '8.5-9.0', '9.0-9.5'])
    print(rating_counts.value_counts().sort_index())

def analyze_by_type(df):
    """Analyze anime by type (TV, Movie, etc.)."""
    print("\n" + "=" * 70)
    print("ANALYSIS BY TYPE")
    print("=" * 70)
    
    print("\n1. Count by Type:")
    type_counts = df['type'].value_counts()
    print(type_counts)
    
    print("\n2. Average Rating by Type:")
    avg_rating_by_type = df.groupby('type')['rating'].agg(['mean', 'count', 'std'])
    print(avg_rating_by_type)
    
    print("\n3. Average Episodes by Type:")
    avg_episodes_by_type = df.groupby('type')['episodes'].mean()
    print(avg_episodes_by_type)

def analyze_by_year(df):
    """Analyze anime trends by year."""
    print("\n" + "=" * 70)
    print("TEMPORAL ANALYSIS")
    print("=" * 70)
    
    print("\n1. Anime Distribution by Year:")
    year_counts = df['year'].value_counts().sort_index()
    print(year_counts.head(10))
    
    print("\n2. Average Rating by Decade:")
    df['decade'] = (df['year'] // 10) * 10
    decade_stats = df.groupby('decade').agg({
        'rating': ['mean', 'count'],
        'members': 'mean'
    }).round(2)
    print(decade_stats)

def analyze_studios(df):
    """Analyze anime by studio."""
    print("\n" + "=" * 70)
    print("STUDIO ANALYSIS")
    print("=" * 70)
    
    print("\n1. Top 10 Studios by Number of Anime:")
    studio_counts = df['studios'].value_counts().head(10)
    print(studio_counts)
    
    print("\n2. Average Rating by Studio (Top 10):")
    studio_ratings = df.groupby('studios')['rating'].agg(['mean', 'count'])
    studio_ratings = studio_ratings.sort_values('mean', ascending=False).head(10)
    print(studio_ratings)

def analyze_popularity(df):
    """Analyze anime popularity based on members."""
    print("\n" + "=" * 70)
    print("POPULARITY ANALYSIS")
    print("=" * 70)
    
    print("\n1. Most Popular Anime (by members):")
    most_popular = df.nlargest(10, 'members')[['name', 'members', 'rating', 'year']]
    print(most_popular.to_string(index=False))
    
    print(f"\n2. Average Members: {df['members'].mean():,.0f}")
    print(f"3. Total Members Across All Anime: {df['members'].sum():,.0f}")
    
    # Correlation between rating and members
    correlation = df['rating'].corr(df['members'])
    print(f"\n4. Correlation between Rating and Members: {correlation:.3f}")

def analyze_genres(df):
    """Analyze anime genres."""
    print("\n" + "=" * 70)
    print("GENRE ANALYSIS")
    print("=" * 70)
    
    # Extract individual genres
    all_genres = []
    for genres in df['genre']:
        all_genres.extend([g.strip() for g in genres.split(',')])
    
    genre_counts = pd.Series(all_genres).value_counts()
    print("\n1. Most Common Genres:")
    print(genre_counts.head(15))
    
    print(f"\n2. Total Unique Genres: {len(genre_counts)}")

def create_visualizations(df):
    """Create visualizations of the anime data."""
    print("\n" + "=" * 70)
    print("CREATING VISUALIZATIONS")
    print("=" * 70)
    
    # Create output directory for plots
    output_dir = Path('plots')
    output_dir.mkdir(exist_ok=True)
    
    # 1. Rating Distribution
    plt.figure(figsize=(10, 6))
    plt.hist(df['rating'], bins=20, edgecolor='black', alpha=0.7)
    plt.xlabel('Rating')
    plt.ylabel('Frequency')
    plt.title('Distribution of Anime Ratings')
    plt.grid(True, alpha=0.3)
    plt.savefig(output_dir / 'rating_distribution.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: rating_distribution.png")
    plt.close()
    
    # 2. Rating vs Members Scatter Plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['rating'], df['members'], alpha=0.6, s=100)
    plt.xlabel('Rating')
    plt.ylabel('Members')
    plt.title('Anime Rating vs Popularity (Members)')
    plt.grid(True, alpha=0.3)
    plt.savefig(output_dir / 'rating_vs_members.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: rating_vs_members.png")
    plt.close()
    
    # 3. Anime Count by Year
    plt.figure(figsize=(12, 6))
    year_counts = df['year'].value_counts().sort_index()
    plt.bar(year_counts.index, year_counts.values, edgecolor='black', alpha=0.7)
    plt.xlabel('Year')
    plt.ylabel('Number of Anime')
    plt.title('Number of Anime by Year')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3, axis='y')
    plt.savefig(output_dir / 'anime_by_year.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: anime_by_year.png")
    plt.close()
    
    # 4. Average Rating by Type
    plt.figure(figsize=(10, 6))
    type_ratings = df.groupby('type')['rating'].mean().sort_values(ascending=False)
    plt.barh(type_ratings.index, type_ratings.values, edgecolor='black', alpha=0.7)
    plt.xlabel('Average Rating')
    plt.ylabel('Type')
    plt.title('Average Rating by Anime Type')
    plt.grid(True, alpha=0.3, axis='x')
    plt.savefig(output_dir / 'rating_by_type.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: rating_by_type.png")
    plt.close()
    
    # 5. Top 10 Studios by Count
    plt.figure(figsize=(12, 6))
    studio_counts = df['studios'].value_counts().head(10)
    plt.barh(studio_counts.index, studio_counts.values, edgecolor='black', alpha=0.7)
    plt.xlabel('Number of Anime')
    plt.ylabel('Studio')
    plt.title('Top 10 Studios by Number of Anime')
    plt.grid(True, alpha=0.3, axis='x')
    plt.savefig(output_dir / 'top_studios.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: top_studios.png")
    plt.close()
    
    print(f"\nAll visualizations saved in '{output_dir}/' directory")

def generate_summary_report(df):
    """Generate a summary report of key findings."""
    print("\n" + "=" * 70)
    print("SUMMARY REPORT")
    print("=" * 70)
    
    print(f"\n📊 Dataset Overview:")
    print(f"   • Total Anime: {len(df)}")
    print(f"   • Date Range: {df['year'].min()} - {df['year'].max()}")
    print(f"   • Average Rating: {df['rating'].mean():.2f}/10")
    print(f"   • Total Members: {df['members'].sum():,}")
    
    print(f"\n🏆 Top Performers:")
    top_anime = df.nlargest(1, 'rating').iloc[0]
    print(f"   • Highest Rated: {top_anime['name']} ({top_anime['rating']}/10)")
    
    most_popular = df.nlargest(1, 'members').iloc[0]
    print(f"   • Most Popular: {most_popular['name']} ({most_popular['members']:,} members)")
    
    print(f"\n🎬 Content Types:")
    for content_type, count in df['type'].value_counts().items():
        print(f"   • {content_type}: {count}")
    
    print(f"\n🏢 Production:")
    print(f"   • Number of Studios: {df['studios'].nunique()}")
    top_studio = df['studios'].value_counts().index[0]
    print(f"   • Most Prolific Studio: {top_studio}")
    
    print("\n" + "=" * 70)

def main():
    """Main function to run all analyses."""
    print("\n" + "=" * 70)
    print("ANIME DATASET ANALYSIS WITH PANDAS")
    print("=" * 70)
    
    # Load data
    df = load_data()
    
    # Perform analyses
    explore_data(df)
    analyze_ratings(df)
    analyze_by_type(df)
    analyze_by_year(df)
    analyze_studios(df)
    analyze_popularity(df)
    analyze_genres(df)
    
    # Create visualizations
    create_visualizations(df)
    
    # Generate summary
    generate_summary_report(df)
    
    print("\n✅ Analysis complete! Check the 'plots' directory for visualizations.")
    print("=" * 70)

if __name__ == "__main__":
    main()
