import pandas as pd
import numpy as np

#this is just a demonstration of a change

#Function 1: Metric Dictionary

### START FUNCTION
def dictionary_of_metrics(items):
    """ this code calculates the mean,median,standard deviation,variance,maximum and minumum
    of the data given as a list. It rounds the answers to 2 decimal places
 and returns the output as a dictionary"""
     return {'mean': round(np.mean(items), 2),
            'median': round(np.median(items), 2),
            'var': round(np.var(items, ddof=1), 2),
            'std': round(np.std(items, ddof=1), 2),
            'min': round(np.min(items), 2),
            'max': round(np.max(items), 2)}

    # your code here

### END FUNCTION



#Function 2: Five Number Summary

### START FUNCTION

def five_num_summary(items):

    """
    The function takes a list of Gauteng data and return a dictionary of with keys maximum, median, minimum, first quartile and third quartile.
    """
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
    
    """
    The function removes a stop words from a dictionary and return a column without stop words.
    """     
    another=[]
    tweets=[i.lower().split(' ') for i in df['Tweets']]
    

    for i in tweets:
        new_column=[]
        for items in i:
            if items not in stop_words_dict['stopwords'] :
            
               new_column.append(items)
        another.append(new_column)

    
    df['Without Stop Words']=another
    return df


### END FUNCTION