from TwitterSearch import *

class TwitterUtils:
    @staticmethod
    def getTweets(keyword):
        try:
            tso = TwitterSearchOrder() # create a TwitterSearchOrder object
            tso.set_keywords([keyword]) # let's define all words we would like to have a look for
            tso.set_language('en') # we want to see German tweets only
            tso.set_include_entities(False) # and don't give us all those entity information

            # it's about time to create a TwitterSearch object with our secret tokens
            ts = TwitterSearch(
                consumer_key = '3iULonI4Xfllv7xPdxaes8eSh',
                consumer_secret = 'edlvvermsGTOBXOffE9Gi3tlEpCC8T1e9cET1uUvuht6oS2MSM',
                access_token = '126733672-EnlC0iMa1WIziFkpJvHAwFc9hNQ0NNC59Ts6afAb',
                access_token_secret = 'UHZRo6WRT7KwLOTyWeYXqK3vO32AZLQBBhM4mDuPaWfZJ'
             )

             # this is where the fun actually starts :)
            #for tweet in ts.search_tweets_iterable(tso):
                #print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

        except TwitterSearchException as e: # take care of all those ugly errors if there are some
            print(e)

        return ts.search_tweets_iterable(tso)

    @staticmethod
    def getUserTimeline(username):
        try:
            tuo = TwitterUserOrder(username) # create a TwitterUserOrder

            # it's about time to create TwitterSearch object again
            ts = TwitterSearch(
                consumer_key = '3iULonI4Xfllv7xPdxaes8eSh',
                consumer_secret = 'edlvvermsGTOBXOffE9Gi3tlEpCC8T1e9cET1uUvuht6oS2MSM',
                access_token = '126733672-EnlC0iMa1WIziFkpJvHAwFc9hNQ0NNC59Ts6afAb',
                access_token_secret = 'UHZRo6WRT7KwLOTyWeYXqK3vO32AZLQBBhM4mDuPaWfZJ'
             )
           # start asking Twitter about the timeline
           #for tweet in ts.search_tweets_iterable(tuo):
               #print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

        except TwitterSearchException as e:
            print(e)

        return ts.search_tweets_iterable(tuo)
