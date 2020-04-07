# Import the Twython class
from twython import Twython
import json

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
            result = python_tweets.search(**{"q":"crime", "until": "2019-03-30"})
        except:
            return api_response

        return api_response