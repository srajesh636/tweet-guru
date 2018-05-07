
import tweepy

def get_tweets(search_term,count):

    keyword=search_term
    count=count
    Ckey = "jxpGx90bgjqZDiRcdiT2uLUO9"
    Csecret = "DPI1QRcRE5CP37IaLDxJpRT0s3k0Dv1H2alhHWlPwCnt5PW81n"
    Atoken = "1396904694-SHm12SMxHJwhKT7fB5ivv0P9IHvZIC753wDMWT5"
    Asecret = "ejVaIC7oMmfyUiT6gYwlOUp6VpoFeMjkB3f5MviT0z0Sx"

    auth = tweepy.OAuthHandler(Ckey, Csecret)
    auth.set_access_token(Atoken, Asecret)
    api = tweepy.API(auth)

    tweets = tweepy.Cursor(api.search, q=keyword, lan="en").items(count)



    return tweets
