import tweepy

api_key = "XXXXXXXXXXXXXXXX"
key_secret = "XXXXXXXXXXXXXXXXXXXXXX"
access_token = "XXXXXXXXXXXXXXXXXXXXXXXXX"
token_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

auth = tweepy.OAuthHandler(api_key,key_secret)
auth.set_access_token(access_token,token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

for data in tweepy.Cursor(api.search, q="tesla").items(10):
    print(data.text)