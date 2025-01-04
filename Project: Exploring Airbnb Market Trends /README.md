# Project: Exploring Airbnb Market Trends
---
##  Purpose
Welcome to New York City, one of the most-visited cities in the world. There are many Airbnb listings in New York City to meet the high demand for temporary lodging for travelers, which can be anywhere between a few nights to many months. In this project, we will take a closer look at the New York Airbnb market by combining data from multiple file types like `.csv`, `.tsv`, and `.xlsx`.

Recall that **CSV**, **TSV**, and **Excel** files are three common formats for storing data. 
Three files containing data on 2019 Airbnb listings are available to you:

**data/airbnb_price.csv**
This is a CSV file containing data on Airbnb listing prices and locations.
- **`listing_id`**: unique identifier of listing
- **`price`**: nightly listing price in USD
- **`nbhood_full`**: name of borough and neighborhood where listing is located

**data/airbnb_room_type.xlsx**
This is an Excel file containing data on Airbnb listing descriptions and room types.
- **`listing_id`**: unique identifier of listing
- **`description`**: listing description
- **`room_type`**: Airbnb has three types of rooms: shared rooms, private rooms, and entire homes/apartments

**data/airbnb_last_review.tsv**
This is a TSV file containing data on Airbnb host names and review dates.
- **`listing_id`**: unique identifier of listing
- **`host_name`**: name of listing host
- **`last_review`**: date when the listing was last reviewed

--- 
## Dataset description 
There were 3 separate DFS, so as a first step, I performed a merge of each of them.

### DF1 + DF2 + DF3 
| **Column**       | **Description**                            |
|-------------------|-------------------------------------------|
| `listing_id`      | The ID of the apartment                   |
| `host_name`       | Host name                                 |
| `last_review`     | Date of the last review                   |
| `room_type`       | Type of room                              |
| `price`           | The price of the apartment                |
| `nbhood_full`     | Local and City                            |

--- 
### Objective 
As a consultant working for a real estate start-up, you have collected Airbnb listing data from various sources to investigate the short-term rental market in New York. You'll analyze this data to provide insights on private rooms to the real estate company.

There are three files in the data folder: airbnb_price.csv, airbnb_room_type.xlsx, airbnb_last_review.tsv.

What are the dates of the earliest and most recent reviews? Store these values as two separate variables with your preferred names.
How many of the listings are private rooms? Save this into any variable.
What is the average listing price? Round to the nearest two decimal places and save into a variable.
Combine the new variables into one DataFrame called review_dates with four columns in the following order: first_reviewed, last_reviewed, nb_private_rooms, and avg_price. The DataFrame should only contain one row of values.

--- 
### Steps to EDA 
1. As a first step, I joined the data into a single dataframe, to make visualization easier.
2. I went to check the most recent dates of the views, checking if they were in the correct type (datetime).
3. I made the appropriate conversions
4. I checked the number of private room advertisements
5. I checked the average listing price, removing the word "dollars" and putting the column as an integer type.
6. I created a dataframe with the information that was being requested
