import tweepy
import csv

consumer_key = 'xSszuP2hz7KHnyD8mqtThgTwp'
consumer_secret = '8HFIwqAAgatXThOfISzFozcXj525Ip8mS1i0CspTXatGWRLNsf'
access_token = '1060902630-zWbmGtSdRIShRqMgro17gfH1QGOJyIWn49EtbIY'
access_token_secret = 'KUItZFQ2cfdfeujTeMotzbrZ2F6LrfHOUrliD9vehIMzw'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


csvFile = open('finalDatasetSecondTry.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
#csvWriter.writerow(["Timestamp", "Tweet", "Hashtags", "Tweet_ID"])
counter = 0

for tweet in tweepy.Cursor(api.search_full_archive,
                            #label must be set account specific!
                            label= '49euroticket',
                            query= '#49euroticket lang:de',
                            fromDate = "202001010000",
                            toDate = "202212260000"
                          ).items():
    status = api.get_status(tweet.id, tweet_mode="extended")
    if not tweet.retweeted and 'RT @' not in tweet.text:
        csvWriter.writerow([tweet.created_at, status.full_text, tweet.entities['hashtags'], tweet.id])
        counter += 1
        print(counter)