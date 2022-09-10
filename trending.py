import pandas
import tweepy

print("Get API keys from twitter developer account.\n")
api_key = input("Enter Consumer Key : ")
key_secret = input("Enter Consumer Key Secret : ")
access_token = input("Enter Access Token : ")
token_secret = input("Enter Access Token Secret : ")

auth = tweepy.OAuthHandler(api_key,key_secret)
auth.set_access_token(access_token,token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

woeid = input("\nEnter WOEId to select trending place : ")

hastag=[]
trends = api.get_place_trends(id = woeid)
for value in trends:
    for trend in value['trends']:
        hastag.append(trend['name'])

count = int(input("\nHow many tweets wants to extact per hastag : "))

date,user,tweet,like=[],[],[],[]
for tag in range(len(hastag)):
    raw_tweets = tweepy.Cursor(api.search_tweets, q=hastag[tag],
        lang="en", tweet_mode="extended", result_type='popular').items(count)
    for data in raw_tweets:
        date.append(data.created_at.strftime('%m/%d/%Y'))
        user.append(data.user.screen_name)
        like.append(data.favorite_count)
        tweet.append(data.full_text)

frame = {"Date":date,"User":user,"Tweet": tweet,"Like":like}
trends_tweets = pandas.DataFrame(frame)
trends_tweets.to_csv('Tweet.csv')
print(trends_tweets)