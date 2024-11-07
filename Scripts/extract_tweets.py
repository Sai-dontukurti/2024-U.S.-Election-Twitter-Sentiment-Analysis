from twitter_api_connect import connect_to_twitter_api
import tweepy

def extract_tweets(query, count=10):
    # Connect to Twitter API using the function from the first script
    api = connect_to_twitter_api()

    # Use Tweepy Cursor to search for tweets matching the query (multiple hashtags/keywords)
    tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en").items(count)
    
    tweet_data = []

    # Collect relevant information from each tweet
    for tweet in tweets:
        tweet_info = {
            "text": tweet.text,
            "created_at": tweet.created_at,
            "user": tweet.user.screen_name,
            "location": tweet.user.location
        }
        tweet_data.append(tweet_info)

    return tweet_data

if __name__ == "__main__":
    # Define the search query with multiple hashtags or keywords
    query = "#Election2024 OR #Biden OR #Trump OR #Kamala"
    count = 20  # Number of tweets to fetch

    # Extract tweets
    tweets = extract_tweets(query, count)

    # Display the extracted tweets
    for tweet in tweets:
        print(f"User: {tweet['user']}, Location: {tweet['location']}, Created at: {tweet['created_at']}")
        print(f"Tweet: {tweet['text']}")
        print("-" * 40)
