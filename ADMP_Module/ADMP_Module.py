import json
import pandas as pd
import TwitterQuery as tq
from datetime import datetime

# Load twitter credentials from json file
twitterCredentials = {}
with open("twitter_credentials.json", "r") as file:
    twitterCredentials = json.load(file)

year = 2020
formated_tweets = []
index = '1100047155438473216'

while year >= 2017 :
    twitter_querier = tq.TwitterApiConstruct(twitterCredentials)
    
    try:
        list_of_tweets = twitter_querier.get_user_timeLine(index)

        if list_of_tweets == []:
            break
    
        for tweet in list_of_tweets:
            datetime_object = datetime.strptime(tweet["created_at"], '%a %b %d %H:%M:%S %z %Y')
            dictionary_of_tweets = {"id": tweet["id"], "Date": str(datetime_object), "DisplayName": tweet["user"]["screen_name"], "Tweet": tweet["text"], "Location": tweet["user"]["location"]}
            formated_tweets.append(dictionary_of_tweets)
            index = tweet["id"]
            year = datetime_object.year
    except :
        break

df = pd.DataFrame(formated_tweets)
df.to_csv(r'C:/Users/sosan/Documents/ADMP/ClassWorkData/crimeTweets.csv', index = False)

