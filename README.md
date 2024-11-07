# 2024 US Election Twitter Sentiment Analysis

This project analyzes sentiment around the 2024 US Presidential Election using Twitter data. By gathering and processing tweets about the election, the project aims to provide insights into public opinion and trends in sentiment across different demographics, locations, and time periods.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Data Collection](#data-collection)
- [Sentiment Analysis](#sentiment-analysis)
- [Results](#results)
- [Future Enhancements](#future-enhancements)
- [Contributors](#contributors)

## Overview
Public sentiment on social media is a powerful indicator of public opinion, especially during significant events like the US Presidential Election. This project gathers real-time Twitter data to analyze trends in sentiment around the 2024 election, identifying positive, negative, and neutral sentiments toward candidates and election-related issues.

## Features
- **Data Collection**: Extracts real-time election-related tweets using the Twitter API.
- **Sentiment Analysis**: Classifies tweets by sentiment (positive, neutral, negative) using natural language processing (NLP).
- **Geospatial Analysis**: Analyzes sentiment by location to observe regional trends.
- **Time-Series Analysis**: Tracks sentiment changes over time to identify shifts in public opinion.

## Project Structure
twitter-election-sentiment-analysis/ ├── data/ │ ├── raw_tweets.csv │ ├── processed_tweets.csv ├── notebooks/ │ ├── data_collection.ipynb │ ├── sentiment_analysis.ipynb │ └── visualization.ipynb ├── src/ │ ├── data_collection.py │ ├── sentiment_analysis.py │ └── visualization.py ├── README.md └── requirements.txt


- **data/**: Stores raw and processed tweet data.
- **notebooks/**: Jupyter notebooks for data collection, sentiment analysis, and visualization.
- **src/**: Python scripts for data collection, processing, and visualization.
- **README.md**: Project overview and usage instructions.
- **requirements.txt**: Dependencies for setting up the environment.

## Technologies Used
- **Python**: Core programming language for data processing and sentiment analysis.
- **Twitter API**: Data source for real-time election tweets.
- **Natural Language Processing (NLP)**: For sentiment classification and text processing.
- **Geospatial Tools**: Analyzes location-based trends in sentiment.
- **Data Visualization**: Uses libraries like `matplotlib` and `seaborn` to visualize sentiment patterns.

## Data Collection
- **Twitter API**: Uses the Twitter API to collect real-time tweets containing keywords related to the 2024 US Election.
- **Data Storage**: Saves raw tweets to `data/raw_tweets.csv` and processed data to `data/processed_tweets.csv`.

## Sentiment Analysis
- **NLP Model**: Utilizes a pre-trained NLP model, such as VADER or TextBlob, to classify tweets as positive, neutral, or negative.
- **Text Preprocessing**: Cleans tweets by removing stopwords, hashtags, mentions, and URLs for accurate analysis.
- **Geospatial and Temporal Trends**: Aggregates sentiment scores by location and time to track shifts in public opinion.

## Results
- **Sentiment Trends**: Provides insights into positive, neutral, and negative sentiment distributions across regions and time.
- **Candidate Sentiment Analysis**: Examines public opinion toward specific candidates, highlighting significant sentiment changes.
- **Geographic Analysis**: Reveals regional differences in sentiment and key election-related issues.

## Future Enhancements
- **Sentiment by Demographics**: Integrate demographic information to analyze sentiment among different age groups, genders, and other factors.
- **Enhanced NLP Model**: Incorporate advanced deep learning models (e.g., BERT) for improved sentiment accuracy.
- **Dashboard for Real-Time Monitoring**: Develop a web-based dashboard for visualizing real-time sentiment analysis results.

## Contributors
- Sai Narayana Murthy Dontukurti

Thank you for reviewing the **2024 US Election Twitter Sentiment Analysis** project!
