
import pandas as pd
netflix_df= pd.read_csv("netflix_data.csv")
#inspect structure
print(netflix_df.shape)
print(netflix_df.head())
print(netflix_df.columns)
#the dataset contains both movies and TV shows, so first filter for:

#type == "Movie"
#release_year between 1990 and 1999
movies_in_the_90s=netflix_df[
    (netflix_df["type"] == "Movie") &
    (netflix_df["release_year"] >= 1990) &
    (netflix_df["release_year"] < 2000)
]
print(movies_in_the_90s.head())
#exploring movie duration statistics
print(movies_in_the_90s["duration"].describe())

#single most common duration
common_duration=movies_in_the_90s["duration"].mode()[0]
print(common_duration)
#count the short action movies
short_action_movies=len(netflix_df[
    (netflix_df["type"]=="Movie")&   
    (netflix_df["duration"]<90)&
    (netflix_df["genre"]=="Action")
])

print("Most frequent duration:",common_duration)
print("Short action movies:", short_action_movies)