import json
import tweepy

## API Credentials
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user_id = "" ## profile"s ID

followers = api.followers(user_id)
friends = api.friends(user_id)

def not_mutual(friends, followers):
    return [x.screen_name for x in friends if x.screen_name not in followers]

print(not_mutual(friends, followers))

## Not yet tested