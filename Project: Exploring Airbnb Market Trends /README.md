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
