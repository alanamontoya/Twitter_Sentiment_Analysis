# Import packages
import json
import re
import pandas as pd

from numpy import unique

# Convert the data from output_copy_3.txt (JSON strings) into Python data structures
json_output = []
with open("output_copy_3.txt") as output_file:
    for line in output_file:
        line = line.encode('utf-8')
        json_output.append(json.loads(line))

# Create empty list to add hashtags to
all_hashtags = []

# Add all hashtags into list (not unique list)
for line in json_output:
    # Get hashtags from each tweet if they exist
    if "entities" in line:
        entity = line['entities']
        hashtags = entity['hashtags']

        # For each hashtag, add it to the overall list of hashtags
        for instance in hashtags:
            hashtag = instance['text']
            # Add all hashtags into list
            all_hashtags.append(hashtag)

# Make an empty list to add all of the unique hashtags to
unique_hashtags = []

# Go through each hashtag and if it is not yet in the unique list of hashtags, add it to the list
for hashtag in all_hashtags:
    if hashtag not in unique_hashtags:
        unique_hashtags.append(hashtag)

# Find the total number of unique hashtags
len_unique_hashtags = len(unique_hashtags)

# Create empty list of hashtag counts
hashtag_count = []

# Compute count of each hashtag
for hashtage_term in range(0, len_unique_hashtags):
    hashtag_count.append(all_hashtags.count(unique_hashtags[hashtage_term]))

# Make a dataframe of all of the hashtags and their counts, sorting them in descending order
data = {'hashtag': unique_hashtags, 'count': hashtag_count}  
hashtags_df = pd.DataFrame(data)
hashtags_df = hashtags_df.sort_values(by = ['count'], ascending = False)

# Get top 10 hashtags witht the highest counts
top_10_hashtags = hashtags_df.head(10)

# Print the top 10 hashtags
for row in range(0, 10):
    print(top_10_hashtags.iloc[row]['hashtag'], " ", top_10_hashtags.iloc[row]['count'])