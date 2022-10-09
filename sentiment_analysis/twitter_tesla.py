import tweepy

# Twitter API credentials
bearer_token = os.environ.get("BEARER_TOKEN")
client = tweepy.Client(bearer_token)

# Get User's Tweets

# This endpoint/method returns Tweets composed by a single user, specified by
# the requested user ID

user_id = 13298072  # Tesla

response = client.get_users_tweets(user_id)

# By default, only the ID and text fields of each Tweet will be returned
for tweet in response.data:
    print(tweet.id)
    print(tweet.text)

# By default, the 10 most recent Tweets will be returned
# You can retrieve up to 100 Tweets by specifying max_results
response = client.get_users_tweets(user_id, max_results=100)

# Save response in text file with utf-8 encoding and store in 'data' directory
with open("data/tesla_tweets.txt", "w", encoding="utf-8") as f:
    f.write(str(response.data))