# Import packages
import sys
import json
import re

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
import json

json_output = []
with open("output_copy_3.txt") as output_file:
    for line in output_file:
        line = line.encode('utf-8')
        json_output.append(json.loads(line))

# Print the sentiment of each tweet in the output.txt file
for line in json_output:
    # For each line assign tweet_sentiment as the variable to keep track of the sentiment of tweets
    tweet_sentiment = 0
    # Check if tweet
    if "text" in line:
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

        # Count the number of words in the tweet
        tot_num_words = len(tweet_words)

        # Create a "counter" variable to track the index the current word being used
        current_word_index = 0

        # Go through each word and sum up the sentiments from the AFINN-111 file for each tweet
        for word in tweet_words:
            # Reset the index of the phrase to be the current word
            phrase_index = current_word_index

            # Create the variable term to build words or phrases from
            term = ''

            # Go through each word and build phrases to find the sentiments of
            while phrase_index < tot_num_words:
                # Add the next word to create new phrase (or start with the next single word to build phrase from)
                term = term + ' ' + ''.join(tweet_words[phrase_index])
                
                # Remove the leading and trailing spaces in the term
                term = term.strip()
                # If the therm is in the dictionary of sentiments then add the corresponding sentiment score to the total sentiment of the tweet
                if term in dictionary:
                    tweet_sentiment = tweet_sentiment + dictionary[term]
                # If the term is not in the dictionary of sentiments then add 0
                if term not in dictionary:
                    tweet_sentiment = tweet_sentiment + 0

                # Update the index of the phrase
                phrase_index = phrase_index + 1

            # Update the index of the current word
            current_word_index = current_word_index + 1
            
        # Print the sentiments of each tweet
        print(tweet_sentiment)
