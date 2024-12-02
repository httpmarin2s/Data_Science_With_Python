# Exploratory Data Analysis: Netflix and the Movies of the 1990s

Netflix, which began in 1997 as a DVD rental service, has evolved into one of the largest entertainment and media companies. With a vast library of movies and series available, this provides an excellent opportunity to dive into data exploration and learn more about the entertainment industry.

In this analysis, we will focus on movies released in the 1990s. Using the `netflix_data.csv` dataset, we aim to better understand this remarkable decade for movies and perform exploratory data analysis (EDA).

---

## **Dataset Description**

The dataset includes the following columns:

| **Column**       | **Description**                           |
|-------------------|-------------------------------------------|
| `show_id`        | The ID of the show                        |
| `type`           | Type of the show (movie or TV show)       |
| `title`          | Title of the show                         |
| `director`       | Director of the show                      |
| `cast`           | Cast of the show                          |
| `country`        | Country of origin                         |
| `date_added`     | Date added to Netflix                     |
| `release_year`   | Year the show was released                |
| `duration`       | Duration of the show (in minutes)         |
| `description`    | Description of the show                   |

---

## **Objective**

The goal of this analysis is to extract insights about movies from the 1990s by exploring their characteristics, such as:

1. **Number of Movies**: How many 1990s movies are in the dataset?
2. **Popular Directors and Actors**: Which directors and actors contributed to 1990s movies?
3. **Country of Origin**: Which countries produced the most movies in this decade?
4. **Duration Analysis**: What's the average duration of movies released in the 1990s?
5. **Genres and Descriptions**: Are there any trends in movie descriptions?

---

## **Steps to Perform EDA**

1. **Import Libraries and Load Data**
   - Use Python libraries like `pandas`, `numpy`, and `matplotlib` to load and explore the data.

2. **Check the Shape AND Unique Values**
   - Use the netfilix_df.shape and netiflix['release_year'].unique() to check te unique values

3. **Filtering the 90s movies and copy in another dataframe**
   - netflix_df_90s = netflix_df_90s[(netflix_df_90s['release_year'] >= 1990) & (netflix_df_90s['release_year'] <= 1999)]

4. **Exploration Data Analysis**
   - Use mean and mode from pandas to analysis

5. **Action movies**
   - I used the filter mode to this 