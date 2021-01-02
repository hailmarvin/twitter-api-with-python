import tweepy

## API Credentials
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
myFollowers = []
myFollowing = []

print('List of Followers')
for follower in api.followers():
    myFollowers.append(follower.screen_name)
    print(follower.screen_name)
print('\n')

print('List of Following')
for friend in api.friends():
    myFollowing.append(friend.screen_name)
    print(friend.screen_name)
print('\n')

print('Accounts that do not follow back')
for x in myFollowing:
    if x not in myFollowers:
        print(x)
print('\n')

print('Accounts you do not follow back')
for x in myFollowers:
    if x not in myFollowing:
        print(x)