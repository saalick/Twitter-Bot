import tweepy
import time

#import twitter apps configaration file from config.py file
from config import *

msg = "Hello World"
#Authentication using keys & accesstoken
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

twt = api.search(q="#YourHashtag")
for st in twt:
    usr = st.user.screen_name
    msg = "@%s Hello!" %(usr)
    st = api.update_status(msg, st.id)
    time.sleep(20)

			
