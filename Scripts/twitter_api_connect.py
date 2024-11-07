import tweepy

def load_twitter_credentials(file_path):
    # Create a dictionary to hold the credentials
    credentials = {}
    
    # Open the file and read each line, splitting on '=' to get key-value pairs
    with open(file_path, "r") as file:
        for line in file:
            key, value = line.strip().split("=")
            credentials[key] = value
    
    return credentials

def connect_to_twitter_api():
    # Provide the full path to your credentials file
    credentials_path = "D:/ES data/Projects/Elections/Twitter_credentials.txt"
    
    # Load credentials from the text file
    credentials = load_twitter_credentials(credentials_path)

    api_key = credentials["TWITTER_API_KEY"]
    api_secret_key = credentials["TWITTER_API_SECRET_KEY"]
    access_token = credentials["TWITTER_ACCESS_TOKEN"]
    access_token_secret = credentials["TWITTER_ACCESS_TOKEN_SECRET"]

    # Authenticate with Twitter API using OAuth
    auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
    api = tweepy.API(auth)

    return api
