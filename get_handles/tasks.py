from .models import BaseHandle, SimilarHandles
import tweepy
import os
import requests
from celery import task


# Set up API access
auth = tweepy.OAuthHandler(os.environ.get('TWITTER_CONSUMER_KEY'), os.environ.get('TWITTER_CONSUMER_SECRET'))
auth.set_access_token(os.environ.get('TWITTER_ACCESS_TOKEN'), os.environ.get('TWITTER_ACCESS_TOKEN_SECRET'))

api = tweepy.API(auth)

# edits1 and edits2 functions are from this blog post: http://norvig.com/spell-correct.html

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters if len(L + c + R)<=15]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): return (e2 for e1 in edits1(word) for e2 in edits1(e1))

@task
def create_similar_handles(bh):
    bh_date = BaseHandle.objects.get(handle=bh)
    sh = []
    for h in edits1(bh_date.handle): # In an ideal world we'd use the edits2 function, but it takes quite a long time
        if requests.get("https://twitter.com/" + h).status_code!=200:
            pass
        else:
            try:
                user=api.get_user(h)
                sh.append(SimilarHandles(base_handle_date=bh_date,
                                         handle=h,
                                         suspended=False,
                                         display_name = user.name,
                                         number_of_tweets = user.statuses_count,
                                         number_of_followers = user.followers_count,
                                         number_following = user.friends_count,
                                         date_joined = user.created_at,
                                         bio = user.description))
            except tweepy.TweepError as e:
                if e.api_code==63:
                    sh.append(SimilarHandles(base_handle_date=bh_date,
                                             handle=h,
                                             suspended=True))
                else:
                    pass
    SimilarHandles.objects.bulk_create(sh)