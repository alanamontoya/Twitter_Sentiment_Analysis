# Twitter Sentiment Analysis

### Summary

*	Access Twitter’s Application Programming Interface (API) using python to download tweets (note: this was done when Twitter's API was still available).
*	Estimate the public's perception (the sentiment) of particular terms or phrases.
*	Analyze the relationship between location and mood from tweet sentiments.

### Background

Twitter historically represented a fundamental instrument in making social measurements. Millions of people voluntarily express opinions across any topic imaginable --- this data source is incredibly valuable for both research and business.

For example, researchers have shown that the "mood" of communication on twitter reflects biological rhythms and can even used to predict the stock market. A student at UW used geocoded tweets to plot a map of locations where "thunder" was mentioned in the context of a storm system in Summer 2012.

### Overview

This project consisted of the following:


  
#### _Files:_

* _AFINN-111.txt_:
    * A list of words each assigned with a pre-computed sentiment score in the range from -5 to +5 which represents the sentiment strength of the words. The AFINN sentiment score was developed by Finn Årup Nielsen as a way to gauge the sentiment of text. Words with negative scores are considered negative, while those with positive scores are considered positive. Examples:

          abandon   -2
          luck      3
          solve     1
      
      Each line in this file contains a word or phrase followed by a sentiment score. This file is used to compute the tweet sentiments in _tweet_sentiment.py_.
* _tweet_sentiment.py_:
    * A script that computes the sentiment of each tweet based on the sentiment scores of the terms in the tweet. The sentiment of a tweet is equivalent to the sum of the sentiment scores for each term in the tweet. Each word or phrase that is found in a tweet but not found in _AFINN-111.txt_ is given a sentiment score of 0.
* _term_sentiment.py_:
    * A script that computes the sentiment for the terms in the tweets that do not appear in the file AFINN-111.txt. Once the sentiment of a _tweet_ is deduced (as done in _tweet_sentiment.py_), the sentiment of the non-sentiment carrying _words_ that do not appear in AFINN-111.txt can then be deduced by working backwords. For example, if the word "soccer" always appears in proximity with positive words like "great" and "fun", then it cane be deduced that the term "soccer" itself carries a positive sentiment.
* _term_sentiment_output.txt_:
    * The output of _term_sentiment.py_. This is needed to run the _happiest_state.py_ file.
* _frequency.py_:
    * A script that computes frequency histogram of the term. The frequency of a term is calculated as:
      $$\frac{\text{Number of occurrences of \textbf{the term} in all tweets}}{\text{Number of occurrences of \textbf{all terms} in all tweets}}$$

      The script returns the terms with their corresponding frequency.
* _happiest_state.py_:
    * A script that computes the happiest state. The script returns the two-letter state abbreviation of the state with the highest average tweet sentiment.
* _top_ten.py_:
    * A script that computes the ten most frequently occurring hashtags.
