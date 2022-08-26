# Import packages
import pandas as pd
import re
import numpy as np
import json

# Make dictionary of the sentiment scores for each word or phrase from term_sentiment_output.txt
# 
# Note: term_sentiment_output.txt was created by running the following in the command prompt:
#       "python term_sentiment.py > term_sentiment_output.txt"
dictionary = {}
with open("term_sentiment_output.txt") as pc_sentiment_file:
    for word_and_sentiment in pc_sentiment_file:
        word_and_sentiment = word_and_sentiment.strip('\n')
        (word_phrase, sentiment_score) = word_and_sentiment.split(" ")
        dictionary[str(word_phrase)] = float(sentiment_score)

# Convert the data from output_copy_3.txt (JSON strings) into Python data structures
json_output = []
with open("output_copy_3.txt") as output_file:
    for line in output_file:
        line = line.encode('utf-8')
        json_output.append(json.loads(line))

# Make dictionary of states and their abbreviations
states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

# Create empty lists of state abbreviations and their sentiment scores
state_abb = []
state_sentiment = []

# Add the sentiment of each tweet in the term_sentiment.txt file
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

        # Go through each word and sum up the sentiments from the term_sentiment_output.txt file for each tweet
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
                # If the term is in the dictionary add score
                if term in dictionary:
                    tweet_sentiment = tweet_sentiment + dictionary[term]
                # If the term is not in the dictionary then add 0
                if term not in dictionary:
                    tweet_sentiment = tweet_sentiment + 0

                # Update the index of the phrase
                phrase_index = phrase_index + 1

            # Update the index of the current word
            current_word_index = current_word_index + 1



        # Get the location of each user
        user = line['user']
        location = user['location']
        # Only consider users who have a location indicated
        if location is not None:
            # Replace commas with spaces
            location = location.replace(',', ' ')
            # Split location into list of words
            loc_split = location.split()
            # Check if any of the words indicated in location correspond to a US state
            for term in loc_split:
                # If the term is a key in the states dictionary then add their location and tweet sentiment to their respective lists, then break loop
                if term in states:
                    state_abb.append(term)
                    state_sentiment.append(tweet_sentiment)
                    break
                # If the term is a value in the states dictionary then add their location and tweet sentiment to their respective lists, then break loop
                elif term in states.values():
                    for abb, state in states.items():
                        if term == state:
                            state_abb.append(abb)
                            state_sentiment.append(tweet_sentiment)
                    break

# Create DataFrame of states are their average sentiment scores in descending order
data = {'state_abb': state_abb, 'state_sentiment': state_sentiment}  
state_sent_df = pd.DataFrame(data)
state_avg_sent_df = state_sent_df.groupby('state_abb').agg(avg_sentiment = ('state_sentiment', 'mean'))
state_avg_sent_df = state_avg_sent_df.sort_values(by = ['avg_sentiment'], ascending = False)

# Get the happiest state
happiest_state = state_avg_sent_df.head(1)

# Print the happiest state 
print(happiest_state.iloc[0].name)