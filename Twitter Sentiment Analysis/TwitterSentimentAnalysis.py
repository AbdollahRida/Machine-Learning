import tweepy
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer

import numpy as np
import operator


# Step 1 - Authenticate
consumer_key= 'uvxkXGqgli9DIwpByDSmyVoPW'
consumer_secret= 'N52mwUqweYpWQIzhEYc8q0w9fNIvwCLtU8ibJzxQn1J36nsZXd'

access_token='804444504409444352-ZKRAT2ndWC0cGk3INq1tx2bFrvmXeTi'
access_token_secret='N7BZDXnu44GS98XCso2UJ3ign1CrSFbVY0FdY2xNn37hI'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('JTX')

# Prepare query features

queries = ['Polytechnique', 'Traditions', 'Papin', 'Prez', '5 Personnes', 'CASB', 'Mythe', 'JTX2016', 'Tournage']

hashtag = "Valentin"

since = "2017-10-01"
until = "2017-10-27"

# Treshold

def get_label(analysis, threshold = 0):
    if analysis.sentiment[0]>threshold:
        return 'Positive'
    else:
        return 'Negative'

# Retrieve and save
avis = dict()
for query in queries:
    query_pol = []
    query_tweets = api.search(q=[hashtag, query],count=100, since = since, until=until)
    with open('%s_tweets.csv' % query, 'wb') as query_file:
        for tweet in query_tweets:
            analysis = TextBlob(tweet.text, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
            query_pol.append(analysis.sentiment[0])
            query_file.write('%s,%s\n' % (tweet.text.encode('utf8'), get_label(analysis)))
    avis[query] = np.mean(query_pol)
sorted_analysis = sorted(avis.items(), key = operator.itemgetter(1), reverse = True)
print('Moyennes des avis par ordre décroissant: ')
for query, pol in sorted_analysis:
    print('%s : %0.3f' % (query, pol))
