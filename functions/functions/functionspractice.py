import pandas as pd
import numpy as np

#Function 1: Metric Dictionary

### START FUNCTION

def dictionary_of_metrics(items):

    """ This code calculates the mean, median, standard deviation, variance, 
    maximum and minumum of the data given as a list. It rounds the values
    to 2 decimal places and returns the output as a dictionary. """

     return {'mean': round(np.mean(items), 2),
            'median': round(np.median(items), 2),
            'var': round(np.var(items, ddof=1), 2),
            'std': round(np.std(items, ddof=1), 2),
            'min': round(np.min(items), 2),
            'max': round(np.max(items), 2)}

### END FUNCTION


#Function 2: Five Number Summary

### START FUNCTION

def five_num_summary(items):

    """
    The function takes a list of data and returns a dictionary of
    the 5 number summary.
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

    """ This function returns the number of tweets based on certain date. """

    new_list = [i[0:10] for i in dates] 
    return new_list

### END FUNCTION


#Function 4: Municipality & Hashtag Detector

### START FUNCTION

def extract_municipality_hashtags(df):

    """ This function extracts the mentioned municipality and hashtags
    from a dataframe of tweets. It adds 2 new columns to the dataframe
    with the municipality mentioned and the hashtags in each tweet. """

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

    """ This funtion groups the number of tweets accourding to the
    specific date. """

    df['Date']=[i.split(' ')[0] for i in df['Date']]
    return df.groupby('Date').count()

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
    The function removes stop words from tweets and adds
    a new column of tweets without stop words.
    """    

    another=[]
    tweets=[i.lower().split() for i in df['Tweets']]
    

    for i in tweets:
        new_column=[]
        for items in i:
            if items not in stop_words_dict['stopwords'] :
            
               new_column.append(items)
        another.append(new_column)

    
    df['Without Stop Words']=another
    return df

### END FUNCTION