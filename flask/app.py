from flask import Flask,render_template,redirect,url_for,request
from textblob import TextBlob
import tweepy
from os import system
import re
import os
from tweets_service import get_tweets
from  unidecode import unidecode




app=Flask(__name__)


@app.route('/')
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
    keyword=request.form['tweet_item']
    count=int(request.form['tweet_count'])


    positive = 0
    negative = 0
    neutral = 0

    tweets=get_tweets(keyword,count)




    list_user, list_tweets, list_ids, list_likes, list_source = [], [], [], [], []

    #print("tweets for the comment are")
    dict={ 0: 'no'}



    for i in tweets:
        list_user.append(i.user.screen_name)
        list_likes.append(i.retweet_count)
        list_source.append(i.source)
        list_ids.append(i.id)

        tweet=i.text
        tweet=unidecode(tweet)
        cleaned_tweet=clean(tweet)
        dict[i.retweet_count]=clean(cleaned_tweet)



        list_tweets.append(cleaned_tweet)

        blob = TextBlob(cleaned_tweet)

        nature = blob.sentiment.polarity

        if nature == 0.0:
            neutral += 1
        elif nature > 0.0:
            positive += 1
        else:
            negative += 1

        new_dict=sorted(dict.items(),reverse=True)




    return render_template('post.html',keyword=keyword,p=count,n=neutral,ne=negative,po=positive,tw=list_tweets,lu=list_user,d=new_dict)


def clean( tweet ):
    some=re.sub(r'https\S+','',tweet)
    some=re.sub(r'RT\s@\S+','',some)
    some=some.replace('\n', '')




    return some





@app.route('/post')
def post():
  return render_template('post.html',name='post')


        #flash(e)


if __name__ == '__main__':
    app.jinja_env.cache = {}
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
