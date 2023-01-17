import tweepy
import csv

consumer_key = 'UrCTyepM53D0uujn7QlkCLuko'
consumer_secret = 'vJO0ZxZIoLKGmjhpWEJISUY3zt4E4jRKvB5AByNQH9771mYN6v'
access_token = '1605540034966323202-uOKkUEwSPyiQaFvu9290P1819yqaRX'
access_token_secret = 'zykYGGXGLMPXG6FN0sog301ayOWiArauYRKLcv6kmhz5l'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


csvFile = open('TwitterDataset.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
#csvWriter.writerow(["Timestamp", "Tweet", "Hashtags", "Tweet_ID"])
counter = 0

for tweet in tweepy.Cursor(api.search_tweets,
                            #label must be set account specific!
                            label= '30days',
                            q= '#49euroticket OR #9euroticket lang:de',
                          ).items():
    status = api.get_status(tweet.id, tweet_mode="extended")
    if not tweet.retweeted and 'RT @' not in tweet.text:
        csvWriter.writerow([tweet.created_at, status.full_text, tweet.entities['hashtags'], tweet.id])
        counter += 1
        print(counter)