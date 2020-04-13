# Import the Twython class
from twython import Twython
import json
import GetOldTweets3 as got

class TwitterApiConstruct:

    def __init__(self, creds={}):
        self.credentials = creds

    def get_user_timeLine(self, max_id=''):   
        api_response = []
        # Instantiate an object
        python_tweets = Twython(self.credentials['CONSUMER_KEY'], self.credentials['CONSUMER_SECRET'])

        # Create our query
        query = {'screen_name': 'syptweet'
                }

        # check and add the max_id if passed
        if max_id != '' :
            query['max_id'] = max_id

        try:
            api_response = python_tweets.get_user_timeline(**query)
        except:
            return api_response

        return api_response
    
    def get_user_timeLine_new(self, username = '', from_date = '', to_date = '', number_of_tweets = 10):

         # generate a query criteria 
        tweetCriteria = got.manager.TweetCriteria().setUsername(username)\
                                                .setSince(from_date)\
                                                .setUntil(to_date)\
                                                .setMaxTweets(number_of_tweets)\
                                                .setEmoji("unicode")

        #query for tweets from GetOldTweets3 using the query criteria
        list_of_tweets = got.manager.TweetManager.getTweets(tweetCriteria)

        return list_of_tweets
    
    def query_tweets(self, range_in_km = '10km', search_term = '', from_date = '', to_date = '', location = '', number_of_tweets = 10):

        tweetCriteria = got.manager.TweetCriteria().setQuerySearch(search_term).setNear(location).setWithin(range_in_km).setMaxTweets(number_of_tweets).setTopTweets(True)

        if to_date != '':
            tweetCriteria.setUntil(to_date)

        if from_date != '':
            tweetCriteria.setSince(from_date)

        list_of_tweets = got.manager.TweetManager.getTweets(tweetCriteria)

        return list_of_tweets

        