# Twitter Sentiment Analysis

### Summary

Twitter has historically served as a vital tool for making social measurements. Millions of individuals openly share their opinions on a wide array of subjects, making Twitter a rich resource for both research and business applications. For example, researchers have shown that the "mood" of communication on twitter [reflects biological rhythms](https://www.nytimes.com/2011/09/30/science/30twitter.html) and can even used to [predict the stock market](https://arxiv.org/pdf/1010.3003&embedded=true).

This project leverages Twitter's API to delve into and analyze the vast data produced by users. The aim is to perform sentiment analysis, examine the connections between tweet locations and moods, and identify prevailing trends in tweet content. The overarching goal is to harness Python and the Twitter API to extract meaningful insights from social media data, enhancing understanding of digital communication patterns.

### Objectives

*	Access Twitter’s Application Programming Interface (API) using python to download tweets (note: this was done when Twitter's API was still available).
*	Estimate the public's perception (the sentiment) toward specific terms or phrases found in tweets.
*	Analyze how geographical locations relate to the mood conveyed in tweets.
*	Explore other patterns in data such as term frequency and hashtag usage.

### Technologies Used

- <ins>Programming Language</ins>: Python
- <ins>Libraries and Frameworks</ins>
   - _pandas_ for data manipulation and analysis.
   - _numpy_ for numerical operations.
   - _json_ for parsing JSON formatted data from Twitter
   - _re_ for regular expression operations, facilitating text processing.
   - _sys_ for accessing command-line arguments and interacting with the Python runtime environment.
- <ins>Development Environment</ins>: Jupyter Notebook

### Methodology

###### Derive the sentiment of each tweet (`tweet_sentiment.py`)

   - Data Loading and Preprocessing
      - Text Import: Tweets are imported from a JSON file (output_copy_3.txt). Each line of this file is parsed into Python's dictionary format using the json library.
      - Text Cleaning: The tweet text undergoes several preprocessing steps:
         - Removal of URLs, retweet artifacts, and mentions.
         - Replacement of various punctuation and special characters with spaces to avoid concatenation of words.
         - Conversion to lowercase to ensure case insensitivity when processing sentiment scores.
   - Sentiment Dictionary Setup
      - A dictionary of sentiment scores is constructed from the AFINN-111.txt file, where each line contains a word or phrase and its associated integer sentiment score. These scores are used to evaluate the sentiment of each tweet.
   - Sentiment Calculation:
      - Extraction and Analysis: For each tweet, the text is split into individual words.
      - Score Computation: The script iterates over each word in a tweet. For each word or consecutive combination of words (phrases), the script checks if it exists in the sentiment dictionary. If it does, its score is added to the tweet's total sentiment score.
      - Edge Handling: If a word or phrase is not found in the dictionary, a sentiment score of 0 is assigned, ensuring that every word is accounted for without altering the overall sentiment calculation.
   - Output:
      - The final sentiment score of each tweet is printed, providing a line-by-line sentiment output corresponding to each tweet in the input file.


### Results

Derive the sentiment of each tweet (tweet_sentiment.py)
Derive the sentiment of new terms (term_sentiment.py)
Compute Term Frequency (frequency.py)
Which State is happiest? (happiest_state.py)
Top ten hash tags (top_ten.py)


***

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
