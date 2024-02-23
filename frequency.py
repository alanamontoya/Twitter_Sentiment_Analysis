# Import packages
import json
import re

# Convert the data from output_copy_3.txt (JSON strings) into Python data structures
json_output = []
with open("output_copy_3.txt") as output_file:
    for line in output_file:
        line = line.encode('utf-8')
        json_output.append(json.loads(line))

# Create empty list to add words from tweets into
string_output_text = []

# Convert text from all of the tweets into a single list
for line in json_output:
    # Check if tweet
    if "text" in line:
        # Get the text of the tweet
        tweet_text = line['text']

        # Process the text (note: there some preprocessing of the output file done directly in a text editor prior to doing this)
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

        # Add words to overall list of words from the tweets
        string_output_text = string_output_text + tweet_words

# Find the number of occurrences of all terms in all tweets
all_term_freq = len(string_output_text)

# Create empty list to track the number of times a word appeard in all of the tweets
term_count = []

# Make a list of all of the unique terms in the tweets
for word in string_output_text:
    if word not in term_count:
        term_count.append(word)

# Get length of term_count
len_term_count = len(term_count)

# Compute term frequency and print out results
for word in range(0, len_term_count):
    print(term_count[word], " ", string_output_text.count(term_count[word]) / all_term_freq)




        
