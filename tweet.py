import tweepy
from textblob import TextBlob
import csv

consumer_key =  'EURtaNIDevjUO2wPZWE1MKrVp'
consumer_secret = 'M9njeaAdhuJ2z3Mpsd8k8KmOU6hK4UAq0WU8plVlIZkC3TT4Ob'

access_token = '3080325786-osVJFA9n9PMeQvjxz2P04Q8lJsjTXwDlI8XrTn7'
access_token_secret = 'koYcvGQOyacNz19xN9X8yPiCmTAoAtrImCk87HNYi4h8X'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

tweet = input("Enter the tweet you want to be searched : \n")


api = tweepy.API(auth)

public_tweets = api.search(tweet)

with open('twitter_sentiment.csv', 'w') as file:
	writer = csv.writer(file)
	writer.writerow(['Index', 'Tweet', 'Author', 'Label'])

	for i, tweet in enumerate(public_tweets):
		analysis = TextBlob(tweet.text)
		author = tweet.user.screen_name

		polarity = analysis.sentiment.polarity
		row_to_add = str(i+1) + ',' + tweet.text + ',' + author + ','

		if polarity > 0:
			file.write(row_to_add + "Positive")
			file.write('\n')
		elif polarity == 0:
			file.write(row_to_add + "Neutral")
			file.write('\n')
		else:
			file.write(row_to_add + "Negative")
			file.write('\n')
