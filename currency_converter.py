import urllib.request
import json
def currency_converter(currency_from, currency_to, currency_input):

    yql_base_url = "https://query.yahooapis.com/v1/public/yql"
    yql_query = 'select%20*%20from%20yahoo.finance.xchange%20where%20pair' \
                '%20in%20("' + currency_from + currency_to + '")'
    yql_query_url = yql_base_url + "?q=" + yql_query + "&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
    try:
        yql_response = urllib.request.urlopen(yql_query_url)
        try:
            json_string = str(yql_response.read())
            json_string = json_string[2:]
            json_string = json_string[:-1]
            print(json_string)
            yql_json = json.loads(json_string)
            last_rate = yql_json['query']['results']['rate']['Rate']
            currency_output = currency_input * float(last_rate)
            return currency_output
        except (ValueError, KeyError, TypeError):
            print(yql_query_url)
            return "JSON format error"
    except IOError as e:
        print(str(e))


currency_input = 1
# // currency codes : http://en.wikipedia.org/wiki/ISO_4217
currency_from = "USD"
currency_to = "TRY"
rate = currency_converter(currency_from, currency_to, currency_input)
print(rate)


""" Content Aggregator
----------------------------------------
"""
import urllib
import os
import requests
import datetime
import subprocess
# // reddit imports
import praw
import pprint
# // pip install feedparser
import feedparser
# // stockexchange
from nsetools import Nse
# // Place your CLIENT_ID & CLIENT_SECRET below
reddit = praw.Reddit(client_id='XXXXXXX',
                     client_secret='XXXXXXXXXXX',
                     grant_type_access='client_credentials',
                     user_agent='script/1.0')
# // class Reddit:
# //    def TopNews(self):
# //          Add your favorite NEWS subreddits in the argument as many as you'd like.
# //         for submission in reddit.subreddit('News+WorldNews+UpliftingNews+').top(limit=10):
# //             top_news = reddit.domain(submission).top('month')
# //             print(top_news)
"""
Each class contains functions which further calls
APIs from the neccesary packages and the rest is 
self explanatory I suppose
"""


class News:
    def Indian_News(self):
        newsfeed = feedparser.parse(
            "http://feeds.feedburner.com/ndtvnews-india-news"
        )
        print("Today's News: ")
        for i in range(0, 20):
            entry = newsfeed.entries[i]
            print(entry.title)
            print(entry.summary)
            print("------News Link--------")
            print(entry.link)
            print("###########################################")
        print('-------------------------------------------------------------------------------------------------------')


class Medium:
    # // https://github.com/thepracticaldev/dev.to/issues/28#issuecomment-325544385
    def medium_programming(self):
        feed = feedparser.parse(
            "https://medium.com/feed/tag/programming"
        )
        print("Programming Today: ")
        for i in range(10):
            entry = feed.entries[i]
            print(entry.title)
            print("URL: " + entry.link)
            print("###########################################")
        print('-------------------------------------------------------------------------------------------------------')

    def medium_python(self):
        feed_python = feedparser.parse(
            "https://medium.com/feed/tag/python"
        )
        print("Python Today: ")
        for i in range(10):
            entry = feed_python.entries[i]
            print(entry.title)
            print("URL: " + entry.link)
            print("###########################################")
        print('-------------------------------------------------------------------------------------------------------')

    def medium_developer(self):
        feed_developer = feedparser.parse(
            "https://medium.com/feed/tag/developer"
        )
        print("Developer News Today: ")
        for i in range(5):
            entry = feed_developer.entries[i]
            print(entry.title)
            print("URL: " + entry.link)
            print("###########################################")
        print('-------------------------------------------------------------------------------------------------------')


class StockExchange:
    def nse_stock(self):
        nse = Nse()
        print("TOP GAINERS OF YESTERDAY")
        pprint.pprint(nse.get_top_gainers())
        print("###########################################")
        print("TOP LOSERS OF YESTERDAY")
        pprint.pprint(nse.get_top_losers())
        print("###########################################")
        print('-------------------------------------------------------------------------------------------------------')


# // objects inititalization
# // reddit_object = Reddit()
News_object = News()
Medium_object = Medium()
StockExchange_object = StockExchange()
if __name__ == "__main__":
    # // Functions call of each class
    # // reddit_object.TopNews()
    News_object.Indian_News()
    Medium_object.medium_python()
    Medium_object.medium_programming()
    Medium_object.medium_developer()
    StockExchange_object.nse_stock()
