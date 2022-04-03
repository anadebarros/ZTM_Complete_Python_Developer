import tweepy
import time

# download your home timeline tweets
# and print each one of their texts to the console.

auth = tweepy.OAuthHandler("9iTa36KxD8XGfMkuGVkQ5g7sr",
                           "oSC8L7O4BJXaRf4sa8rQwE8wAxVtj80sVtMOB5CP7nKEzEI2WK")
auth.set_access_token("83951674-5j24ddrYAJ4lTMBZhySh5EIaqo8JTuxZ2EMkR62rn",
                      "QXJOlw5i9U8uKtHJ0L4spbGSxE66ZPRcGrtStIXjAT7tE")

api = tweepy.API(auth)

user = api.me()

# Create a bot that automatically follows those who follow me

# create a limit handler, not to overbear the twitter server


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     print(follower.name)


# Be a narcisist and love your own tweets. or retweet anything with a keyword!
search = "anonymous"
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('liked the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
