"""
Script to create a sample anime dataset for analysis.
This dataset contains information about popular anime titles.
"""
import pandas as pd

# Create a comprehensive anime dataset
anime_data = {
    'anime_id': range(1, 51),
    'name': [
        'Death Note', 'Fullmetal Alchemist: Brotherhood', 'Attack on Titan', 
        'Steins;Gate', 'Hunter x Hunter', 'Code Geass', 'Cowboy Bebop',
        'One Punch Man', 'Mob Psycho 100', 'My Hero Academia', 
        'Naruto', 'One Piece', 'Bleach', 'Dragon Ball Z', 'Demon Slayer',
        'Sword Art Online', 'Tokyo Ghoul', 'Psycho-Pass', 'Parasyte',
        'Neon Genesis Evangelion', 'Samurai Champloo', 'Trigun', 
        'Yu Yu Hakusho', 'Jujutsu Kaisen', 'Chainsaw Man', 
        'Vinland Saga', 'Made in Abyss', 'Re:Zero', 'The Promised Neverland',
        'Erased', 'Your Name', 'A Silent Voice', 'Weathering with You',
        'Spirited Away', 'Princess Mononoke', 'Haikyuu!!', 'Kuroko no Basket',
        'Food Wars!', 'Dr. Stone', 'The Rising of the Shield Hero',
        'Overlord', 'That Time I Got Reincarnated as a Slime', 
        'Konosuba', 'No Game No Life', 'Violet Evergarden',
        'Angel Beats!', 'Clannad: After Story', 'Anohana', 
        'Your Lie in April', 'March Comes in Like a Lion'
    ],
    'genre': [
        'Mystery, Thriller', 'Action, Adventure, Fantasy', 'Action, Drama', 
        'Sci-Fi, Thriller', 'Action, Adventure', 'Mecha, Military', 'Action, Sci-Fi',
        'Action, Comedy', 'Action, Comedy', 'Action, School', 
        'Action, Adventure', 'Action, Adventure', 'Action, Supernatural', 
        'Action, Martial Arts', 'Action, Demons',
        'Action, Adventure, Fantasy', 'Action, Horror', 'Action, Sci-Fi', 
        'Action, Horror, Sci-Fi',
        'Mecha, Psychological', 'Action, Samurai', 'Action, Sci-Fi', 
        'Action, Supernatural', 'Action, Supernatural', 'Action, Horror', 
        'Action, Adventure, Historical', 'Adventure, Fantasy', 'Drama, Fantasy', 
        'Mystery, Thriller',
        'Mystery, Thriller', 'Drama, Romance', 'Drama, Romance', 
        'Drama, Romance, Fantasy',
        'Adventure, Fantasy', 'Adventure, Fantasy', 'Sports', 'Sports',
        'School, Comedy', 'Adventure, Sci-Fi', 'Action, Adventure, Fantasy',
        'Action, Fantasy', 'Action, Fantasy', 
        'Comedy, Fantasy', 'Game, Fantasy', 'Drama, Fantasy',
        'Drama, Supernatural', 'Drama, Romance', 'Drama, Supernatural', 
        'Drama, Romance, Music', 'Drama, Slice of Life'
    ],
    'type': [
        'TV', 'TV', 'TV', 'TV', 'TV', 'TV', 'TV', 'TV', 'TV', 'TV',
        'TV', 'TV', 'TV', 'TV', 'TV', 'TV', 'TV', 'TV', 'TV', 'TV',
        'TV', 'TV', 'TV', 'TV', 'TV', 'TV', 'TV', 'TV', 'TV', 'TV',
        'Movie', 'Movie', 'Movie', 'Movie', 'Movie', 'TV', 'TV', 'TV', 
        'TV', 'TV', 'TV', 'TV', 'TV', 'TV', 'TV', 'TV', 'TV', 'TV', 'TV', 'TV'
    ],
    'episodes': [
        37, 64, 75, 24, 148, 50, 26, 12, 12, 113,
        220, 1000, 366, 291, 26, 25, 12, 22, 24, 26,
        26, 26, 112, 24, 12, 24, 13, 25, 12, 12,
        1, 1, 1, 1, 1, 85, 75, 24, 24, 25,
        13, 24, 10, 12, 13, 13, 24, 11, 22, 22
    ],
    'rating': [
        8.6, 9.1, 8.8, 9.0, 9.0, 8.7, 8.9, 8.7, 8.5, 8.4,
        8.3, 8.7, 7.9, 8.1, 8.6, 7.6, 7.8, 8.3, 8.3, 8.5,
        8.5, 8.2, 8.5, 8.6, 8.7, 8.7, 8.7, 8.2, 8.5, 8.5,
        8.4, 8.9, 8.1, 8.6, 8.4, 8.6, 8.3, 8.5, 8.1, 8.0,
        7.9, 8.1, 8.1, 8.2, 8.6, 8.1, 8.9, 8.3, 8.6, 8.4
    ],
    'members': [
        2500000, 2000000, 2200000, 800000, 1200000, 1500000, 1300000,
        1800000, 900000, 2100000, 1900000, 1600000, 1400000, 1100000, 1700000,
        2300000, 1700000, 600000, 800000, 1000000, 700000, 500000,
        600000, 1500000, 1300000, 700000, 600000, 1200000, 900000, 800000,
        1900000, 1100000, 900000, 1400000, 900000, 1200000, 800000,
        900000, 800000, 1000000, 700000, 1100000, 1200000, 900000,
        1000000, 1100000, 900000, 1000000, 1100000, 700000
    ],
    'year': [
        2006, 2009, 2013, 2011, 2011, 2006, 1998, 2015, 2016, 2016,
        2002, 1999, 2004, 1989, 2019, 2012, 2014, 2012, 2014, 1995,
        2004, 1998, 1992, 2020, 2022, 2019, 2017, 2016, 2019, 2016,
        2016, 2016, 2019, 2001, 1997, 2014, 2012, 2015, 2019, 2019,
        2015, 2018, 2016, 2014, 2018, 2010, 2008, 2011, 2014, 2016
    ],
    'studios': [
        'Madhouse', 'Bones', 'Wit Studio', 'White Fox', 'Madhouse', 
        'Sunrise', 'Sunrise', 'Madhouse', 'Bones', 'Bones',
        'Pierrot', 'Toei Animation', 'Pierrot', 'Toei Animation', 'ufotable',
        'A-1 Pictures', 'Pierrot', 'Production I.G', 'Madhouse',
        'Gainax', 'Manglobe', 'Madhouse', 'Pierrot', 'MAPPA', 'MAPPA',
        'Wit Studio', 'Kinema Citrus', 'White Fox', 'CloverWorks',
        'A-1 Pictures', 'CoMix Wave Films', 'Kyoto Animation', 
        'CoMix Wave Films', 'Studio Ghibli', 'Studio Ghibli',
        'Production I.G', 'Production I.G', 'J.C.Staff', 'TMS Entertainment',
        'Kinema Citrus', 'Madhouse', '8bit', 'Studio Deen', 'Madhouse',
        'Kyoto Animation', 'P.A. Works', 'Kyoto Animation', 'A-1 Pictures',
        'A-1 Pictures', 'Shaft'
    ]
}

# Create DataFrame
df = pd.DataFrame(anime_data)

# Save to CSV
df.to_csv('anime.csv', index=False)
print("Anime dataset created successfully!")
print(f"Dataset shape: {df.shape}")
print(f"\nFirst few rows:")
print(df.head())
