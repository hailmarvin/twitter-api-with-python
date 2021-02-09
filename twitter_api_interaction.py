import tweepy
import os
import time
import random

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

def get_user():
    username = input('Enter flags (type h for help): ')
    if username == 'h':
        help = """format: [username] -[flags]
    Flags
    -a     displays list of followers
    -b     displays list of following
    -c     displays list of non followers
    -d     displays list of non following
    -u     unfollow non followers
    -e     account information
    -q     exit script
    Multiple flags may be used. For instance:
    _10bih -ab
    If no flag is provided it will return account information"""
        print(help)
        get_user()
    elif username == 'q':
         exit()  
    else:
        separated = username.split('-')
        name =separated[0].split()
        if len(separated) < 2:
            flag = ''
        else:
            flag = separated[1]

        char = []
        if flag == '':
            char.append('e')
        else:
            for x in list(flag):
                char.append(x)

        for x in char:
            if x == 'e':
                user = api.get_user(name[0])
                print("The id is : " + str(user.id)) 
                print("The id_str is : " + user.id_str) 
                print("The name is : " + user.name) 
                print("The screen_name is : " + user.screen_name) 
                print("The location is : " + str(user.location)) 
                print("The profile_location is : " + str(user.profile_location)) 
                print("The description is : " + user.description) 
            elif x == 'a':
                print('List of Followers')
                for follower in api.followers(name[0]):
                    myFollowers.append(follower.screen_name)
                    print(follower.screen_name)
                print('\n')
            elif x == 'b':
                print('List of Following')
                for friend in api.friends(name[0]):
                    myFollowing.append(friend.screen_name)
                    print(friend.screen_name)
                print('\n')
            elif x == 'c':
                print('Accounts that do not follow back')
                for x in myFollowing:
                    if x not in myFollowers:
                        print(x)
                print('\n')
            elif x == 'd':
                print('Accounts you do not follow back')
                for x in myFollowers:
                    if x not in myFollowing:
                        print(x)
            elif x == 'u':
                me = api.me()
                if name[0] == me.screen_name:
                    for x in myFollowers:
                        if x not in myFollowing:
                            api.destroy_friendship(x)
                            n = random.randint(5, 12)
                            time.sleep(n)
                    print("Done!")    

                else:
                    print('You are not authenticated')      
        get_user()

get_user()    