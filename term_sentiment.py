# Import packages
import sys
import json
import re
import pandas as pd

#from numpy import test

#def hw():
#    print('Hello, world!')

#def lines(fp):
#    print(str(len(fp.readlines())))

#def main():
#    sent_file = open(sys.argv[1])
#    tweet_file = open(sys.argv[2])
#    hw()
#    lines(sent_file)
#    lines(tweet_file)

#if __name__ == '__main__':
#    main()

# Make dictionary of the sentiment scores for each word or phrase from AFINN-11.text
dictionary = {}
with open("AFINN-111.txt") as pc_sentiment_file:
    for word_and_sentiment in pc_sentiment_file:
        word_and_sentiment = word_and_sentiment.strip('\n')
        (word_phrase, sentiment_score) = word_and_sentiment.split("\t")
        dictionary[str(word_phrase)] = int(sentiment_score)

# Convert the data from output_copy_3.txt (JSON strings) into Python data structures
json_output = []
with open("output_copy_3.txt") as output_file:
    for line in output_file:
        line = line.encode('utf-8')
        json_output.append(json.loads(line))

# Create dictionary with tweets as keys and tweet sentiment scores as values
tweets = []
sent_scores = []

for line in json_output:
    # Reset sentiment of tweet to be 0
    tweet_sentiment = 0

    # Check if tweet
    if "text" in line:
        # Use only English tweets
        if "lang" in line:
            language = line["lang"]
            if language == "en":

                # Get the text of the tweet
                tweet_text = line['text']

                # Process the text (note: there some preprocessing of the output file done directly in the text editor prior to doing this)
                tweet_text = re.sub(r'http\S+', '', tweet_text)
                tweet_text = re.sub("RT @\\w+", "", tweet_text)
                tweet_text = re.sub("@\\w+", " ", tweet_text)
                tweet_text = tweet_text.replace('`', ' ').replace('~', ' ').replace('!', ' ').replace('$', ' ').replace('%', ' ').replace('^', ' ').replace('&', ' ').replace('*', ' ').replace('(', ' ')
                tweet_text = tweet_text.replace(')', ' ').replace('-', ' ').replace('_', ' ').replace('+', ' ').replace('=', ' ').replace('{', ' ').replace('}', ' ').replace('[', ' ').replace(']', ' ').replace('|', ' ')
                tweet_text = tweet_text.replace(':', ' ').replace(';', ' ').replace('"', ' ').replace('<', ' ').replace('>', ' ').replace(',', ' ').replace('.', ' ').replace('?', ' ').replace('/', ' ')
                tweet_text = tweet_text.replace(' \\ ', ' ').replace('\\ ', ' ')
                tweet_text = tweet_text.lower()

                # Split the words of the text
                tweet_words = tweet_text.split()

                # Rejoin the words with just a space between them
                tweets.append(' '.join(tweet_words))

                # Find the length of the number of words in the tweet
                tot_num_words = len(tweet_words)

                # Get the index of the current word
                current_word_index = 0

                # Go through each word and sum up the sentiments from the AFINN-111 file for each tweet
                for word in tweet_words:
                    # Reset the index of the phrase to be the current word
                    phrase_index = current_word_index

                    # Create the variable term to build words or phrases from
                    term = ''

                    # Go through each word and build phrases to find the sentiments of those words from the AFINN-111 file
                    while phrase_index < tot_num_words:
                        # Add the next word to create new phrase (or start with the next single word to build phrase from)
                        term = term + ' ' + ''.join(tweet_words[phrase_index])
                        # Remove leading a training spaces
                        term = term.strip()
                        # If the term is in the dictionary then add score
                        if term in dictionary:
                            tweet_sentiment = tweet_sentiment + dictionary[term]
                        # If the term is not in the dictionary then add 0
                        if term not in dictionary:
                            tweet_sentiment = tweet_sentiment + 0
                        # Update the index of the phrase
                        phrase_index = phrase_index + 1
                    # Update the index of the current word
                    current_word_index = current_word_index + 1
                # Add sentiment score to list of all sentiment scores
                sent_scores.append(tweet_sentiment)

# Create dictionary of tweets and their sentiment scores
dict_tweet_sent = dict(zip(tweets, sent_scores))

# Find words not in dictionary and add them to new_words
new_words = []

for line in json_output:
    # Check if tweet
    if "text" in line:
        # Use only English tweets
        if "lang" in line:
            language = line["lang"]
            if language == "en":
                # Get the text of the tweet
                tweet_text = line['text']

                # Process the text (note: there some preprocessing of the output file done directly in the text editor prior to doing this)
                tweet_text = re.sub(r'http\S+', '', tweet_text)
                tweet_text = re.sub("RT @\\w+", "", tweet_text)
                tweet_text = re.sub("@\\w+", " ", tweet_text)
                tweet_text = tweet_text.replace('`', ' ').replace('~', ' ').replace('!', ' ').replace('$', ' ').replace('%', ' ').replace('^', ' ').replace('&', ' ').replace('*', ' ').replace('(', ' ')
                tweet_text = tweet_text.replace(')', ' ').replace('-', ' ').replace('_', ' ').replace('+', ' ').replace('=', ' ').replace('{', ' ').replace('}', ' ').replace('[', ' ').replace(']', ' ').replace('|', ' ')
                tweet_text = tweet_text.replace(':', ' ').replace(';', ' ').replace('"', ' ').replace('<', ' ').replace('>', ' ').replace(',', ' ').replace('.', ' ').replace('?', ' ').replace('/', ' ')
                tweet_text = tweet_text.replace(' \\ ', ' ').replace('\\ ', ' ')
                tweet_text = tweet_text.lower()

                # Split the words of the text
                tweet_words = tweet_text.split()

                # For all of the words in the tweet, add those words to new_words if they are not yet in the list
                for word in tweet_words:
                    if word not in dictionary:
                        if word not in new_words:
                            new_words.append(word)

# Create empty list to ass the sentiments of each new word to
new_words_sent = []

# Calculate the sentiment of each new word
for new_word in new_words:
    # Create an empty list that track the sentiments of each tweet that contains the current word
    track_sent = []
    # Get all of the tweets that contain the word
    for tweet in dict_tweet_sent:
        # Create 
        end_test = 0
        # Split the words of the tweet
        tweet_split = tweet.split()
        # Find the tweets that contain the word and get their sentiment scores
        for word in tweet_split:
            if new_word == word:
                track_sent.append(dict_tweet_sent[tweet])
                end_test = 1
            # If word is found in tweet, stop looking for word
            if end_test == 1:
                break
    # Calculate the average sentiment of each tweet containing the current word and add the sentiment to the list that tracks the sentiments of each word
    new_words_sent.append(sum(track_sent) / len(track_sent))

# Print each word and its sentiment score
for word in range(0, len(new_words)):
    print(new_words[word] + ' ' + str(new_words_sent[word]))
