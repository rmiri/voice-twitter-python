import twitter
import keys 


t = twitter.Api(consumer_key=keys.CONSUMER_KEY,
                consumer_secret=keys.CONSUMER_SECRET,
                access_token_key=keys.ACCESS_TOKEN,
                access_token_secret=keys.ACCESS_SECRET)

def postStatus(msg):
    status = t.PostUpdate(msg)
    print('Tweet sent, goodbye')

def logConsole(msg):
    print(msg)

