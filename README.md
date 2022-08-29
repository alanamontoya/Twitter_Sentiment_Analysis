# Twitter_Sentiment_Analysis

Summary:

*	Accessed Twitter’s API to download tweets.
*	Derived the sentiments of tweets using Finn Arup Nielsen’s list of words rated for valence in python.
*	Computed the sentiment of terms that did NOT exist in Finn Arup Nielsen’s list of words rated for valence by computing the average sentiment scores of the tweets that contained the new words.
*	Analyzed the relationship between location and mood from tweet sentiments.

Files:

* _output_copy_3.txt_: The processed Twitter data downloaded from the live Twitter stream using the development API.
* _tweet_sentiment.py_: A script that computes the sentiment of each tweet based on the sentiment scores of the terms in the tweet. The sentiment of a tweet is equivalent to the sum of the sentiment scores for each term in the tweet. Each word or phrase that is found in a tweet but not found in _AFINN-111.txt_ is given a sentiment score of 0.
* _AFINN-111.txt_: A list of pre-computed sentiment scores. Each line in the file contains a word or phrase followed by a sentiment score. This file is used to compute the tweet sentiments in _tweet_sentiment.py_. 
* _term_sentiment.py_: A script that computes the sentiment for the terms that do not appear in the file AFINN-111.txt.
* _frequency.py_: A script that computes the term frequency histogram of the livestream data harvested. The frequency of a term is calculated as [# of occurrences of the term in all tweets]/[# of occurrences of all terms in all tweets].
* _happiest_state.py_: A script that computes the happiest state. The script returns the two letter state abbreviation of the state with the highest average tweet sentiment.
* _top_ten.py_: A script that computes the ten most frequently occurring hashtags in the downloaded tweets.
