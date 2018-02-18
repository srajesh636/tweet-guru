from flask import Flask,render_template,redirect,url_for,request
from textblob import TextBlob
import tweepy

app=Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html',name='name')

@app.route('/about')
def about():
    return render_template('about.html',name='abt')

@app.route('/contact')
def contact():
    return render_template('contact.html',name='contact')

@app.route('/tweets',methods=['POST','GET'])
def tweets():
    usr=request.form['username']
    pas=int(request.form['password'])


    positive = 0
    negative = 0
    neutral = 0

    Ckey = "jxpGx90bgjqZDiRcdiT2uLUO9"
    Csecret = "DPI1QRcRE5CP37IaLDxJpRT0s3k0Dv1H2alhHWlPwCnt5PW81n"
    Atoken = "1396904694-SHm12SMxHJwhKT7fB5ivv0P9IHvZIC753wDMWT5"
    Asecret = "ejVaIC7oMmfyUiT6gYwlOUp6VpoFeMjkB3f5MviT0z0Sx"

    auth = tweepy.OAuthHandler(Ckey, Csecret)
    auth.set_access_token(Atoken, Asecret)
    api = tweepy.API(auth)



    tweets = tweepy.Cursor(api.search, q=usr, lan="en").items(pas)



    list_user, list_tweets, list_ids, list_likes, list_source = [], [], [], [], []

    #print("tweets for the comment are")
    dict={ 0: 'no'}


    for i in tweets:
        list_user.append(i.user.screen_name)
        list_likes.append(i.retweet_count)
        list_source.append(i.source)
        list_ids.append(i.id)

        dict[i.retweet_count]=i.text

        list_tweets.append(i.text)

        blob = TextBlob(i.text)

        nature = blob.sentiment.polarity

        if nature == 0.0:
            neutral += 1
        elif nature > 0.0:
            positive += 1
        else:
            negative += 1

        new_dict=sorted(dict.items(),reverse=True)



    return render_template('post.html',usr=usr,p=pas,n=neutral,ne=negative,po=positive,tw=list_tweets,lu=list_user,d=new_dict)







@app.route('/post')
def post():
  return render_template('post.html',name='post')



        #flash(e)


if __name__ == '__main__':
    app.jinja_env.cache = {}
    app.run()
