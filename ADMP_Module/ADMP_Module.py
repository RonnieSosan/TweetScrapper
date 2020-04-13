import json
import pandas as pd
import TwitterQuery as tq
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import *


# set dates for query
fromdate = '2017-01-01'
todate = '2020-01-31'
search_term = 'Knife Crime'


#twitterCredentials = {}
#with open("twitter_credentials.json", "r") as file:
    #twitterCredentials = json.load(file)


year = 2017
formated_tweets = []

# set the loop for running through the years until 2019
while year <= 2019 :
    twitter_querier = tq.TwitterApiConstruct()

    #list_of_tweets = twitter_querier.get_user_timeLine_new('syptweet', fromdate, todate, 10)
    
    try:
        list_of_tweets = twitter_querier.query_tweets('20km', search_term, fromdate, todate, 'Sheffield, United Kingdom', 100)

        if list_of_tweets == []:
            break
        
        #loop through each tweet
        for tweet in list_of_tweets:
            #create a time object from the tweet date
            datetime_object = datetime.strptime(tweet.formatted_date, '%a %b %d %H:%M:%S %z %Y')

            #create a dictionary for the tweet
            dictionary_of_tweets = {"id": tweet.id, "Date": str(datetime_object), "username": tweet.username, "Tweet": tweet.text, "Location": tweet.geo}

            #append the tweet to the list of formatted tweets
            formated_tweets.append(dictionary_of_tweets)
            index = tweet.id
            date = datetime_object

        fromdate = (datetime.strptime(fromdate, "%Y-%m-%d") + relativedelta(months =+ 1)).strftime("%Y-%m-%d")
        todate = (datetime.strptime(todate, "%Y-%m-%d") + relativedelta(months =+ 1)).strftime("%Y-%m-%d")
        year = datetime.strptime(todate, "%Y-%m-%d").year

    except:
        raise
        #break

df = pd.DataFrame(formated_tweets)
df.to_csv(r'C:/Users/sosan/Documents/ADMP/ClassWorkData/{1}_result.csv'.format(search_term), index = False)

