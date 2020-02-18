import pandas as pd
import numpy as np

#this is just a demonstration of a change

#Function 1: Metric Dictionary

### START FUNCTION
def dictionary_of_metrics(items):
    # your code here
    return

### END FUNCTION



#Function 2: Five Number Summary

### START FUNCTION
def five_num_summary(items):
    dict={'Max':round(np.max(items),2),
          'median':round(np.median(items),2),
          'min':round(np.min(items),2),
          'q1':round (np.percentile(items, 25 ),2),
          'q2':round(np.percentile(items,75),2)
         }
    return dict

### END FUNCTION



#Function 3: Date Parser

### START FUNCTION
def date_parser(dates):
    # your code here
    return

### END FUNCTION



#Function 4: Municipality & Hashtag Detector

### START FUNCTION
def extract_municipality_hashtags(df):
    municipality = []
    hashtags = []

    tweets = [i.split(" ") for i in df['Tweets']]

    new_munic_list = []
    new_tag_list = []

    for tweet in tweets:
        municipality.append([mun_dict[word] for word in tweet if word in list(mun_dict.keys())])
        hashtags.append([tag.lower() for tag in tweet if tag.startswith('#')])

    for item in municipality:
        if item == []:
            item = np.nan  
        new_munic_list.append(item)

    for tag in hashtags:
        if tag == []:
            tag = np.nan
        new_tag_list.append(tag)
    
    df['municipality'] = new_munic_list
    df['hashtags'] = new_tag_list
    
    return df

### END FUNCTION



#Function 5: Number of Tweets per Day

### START FUNCTION
def number_of_tweets_per_day(df):
    # your code here
    return

### END FUNCTION



#Function 6: Word Splitter

### START FUNCTION
def word_splitter(df):
    # your code here
    return

### END FUNCTION


#Function 7: Stop Words
### START FUNCTION
def stop_words_remover(df):
    # your code here
    return

### END FUNCTION