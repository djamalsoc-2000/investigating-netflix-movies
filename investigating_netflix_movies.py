import pandas as pd

# Load the Netflix dataset (replace 'netflix_titles.csv' with your actual file path if different)
netflix_df = pd.read_csv('netflix_data.csv')

netflix_df.head()
netflix_df.info()
print(netflix_df["type"].unique())
print(netflix_df["genre"].unique())  # Note: The correct column might be 'listed_in' instead of 'genre'

movies_90s = netflix_df[(netflix_df["type"] == "Movie")
            & (netflix_df["release_year"] >= 1990)
            & (netflix_df["release_year"] < 2000)]

import matplotlib.pyplot as plt

plt.hist(movies_90s["duration"], bins = 20)
plt.xlabel("Duration(minutes)")
plt.ylabel("Number of movies")
plt.title("1990s movie durations")
plt.show()

print(movies_90s["duration"].value_counts().head())  # top counts to see the contenders
duration = int(movies_90s["duration"].mode()[0])
print(duration)

action_90s = movies_90s[movies_90s["genre"] == "Action"]
short_movies = action_90s[action_90s["duration"] < 90]
short_movie_count = int(len(short_movies))
print(short_movie_count)