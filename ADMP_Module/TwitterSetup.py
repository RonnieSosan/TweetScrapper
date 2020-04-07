import json
from datetime import datetime

datetime_object = datetime.strptime("Thu Mar 05 14:29:01 +0000 2020", '%a %b %d %H:%M:%S %z %Y')
if datetime_object.year > 2017:
    print(datetime_object)
# Enter your keys/secrets as strings in the following fields
credentials = {}
credentials['CONSUMER_KEY'] = 'pvYciJxPQTzABP7S4lqq2CR0M'
credentials['CONSUMER_SECRET'] = 'g6Zid67HG8FqgOIEJD1ekqTSF4Hea61pIH22fmyykHKniirsiP'
credentials['ACCESS_TOKEN'] = '235636604-C83m6ZQjZRiUngNnZ4mXVH6RAu96Yz5iHZJNABl9'
credentials['ACCESS_SECRET'] = 'E1LilgLS9u7707mTB4Kv6SAWEkxph93oo9kX3TO59wRYk'

# Save the credentials object to file
with open("twitter_credentials.json", "w") as file:
    json.dump(credentials, file)
