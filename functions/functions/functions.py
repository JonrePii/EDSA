import pandas as pd
import numpy as np


def dictionary_of_metrics(items):
    """
        Return's the mean, median, standard deviation, variance, minimum value 
        and the maximum value of the given list, rounded to 2 decimal places.
        (ddof=1)
    
    Parameters:
        argument1(list): A list of integers/floats.
        
    """
    return {'mean': round(np.mean(items), 2),
            'median': round(np.median(items), 2),
            'std': round(np.std(items, ddof=1), 2),
            'var': round(np.var(items, ddof=1), 2),
            'min': round(np.min(items), 2),
            'max': round(np.max(items), 2)}


def five_num_summary(items):
    """
        Return's the 5 number summary of the given list, rounded to 2 decimal places.
    
    Parameters:
        argument1(list): A list of integers/floats.
        
    """
    return {'max': round(np.max(items), 2),
            'median':  round(np.median(items), 2),
            'min': round(np.min(items), 2),
            'q1': round(np.quantile(items, .25),2),
            'q3':round(np.quantile(items, .75), 2)}


def date_parser(dates):
    """
        Takes a list of datetime strings as input and returns only the date in "yyyy-mm-dd" format.
    
    Parameters:
        argument1(list): A list of datetime strings.
        
    """
    return  [str(i.date()) for i in [pd.to_datetime(i) for i in dates]]


def extract_municipality_hashtags(df):
    """
        Returns a modified dataframe that includes two new columns:
            1.'municipality':
                -Extracted the municipality from a tweet using 
                    the "mun_dict" dictonary.
            2. 'hashtags':
                -Extracted a list of hashtags from a tweet.
    
    Parameters:
        argument1(pd.DataFrame): A Pandas Dataframe with a "Tweets" column 
            that contains strings(Tweets).
        
    """
    emails = []
    hashtags = []
    for x in df["Tweets"]:
        emails.append([mun_dict[i] for i in x.lower().split(" ")  if i in mun_dict.keys()])  
        hashtags.append([i[i.find("#"):] for i in x.lower().split(" ")  if "#" in i])  
    formatted_emails = [i if i else np.nan for i in emails]
    formatted_hashtags = [i if i else np.nan for i in hashtags] 
    df["municipality"] = formatted_emails
    df["hashtags"] = formatted_hashtags
    return df


def number_of_tweets_per_day(df):
    """
        Takes a pandas dataframe and return's a new dataframe with 
            the number of tweets that were posted per day.
            This functions counts the amount of times each unique 
            date appears in the "Date" column of the Dataframe.
    
    Parameters:
        argument1(pd.DataFrame): A Pandas Dataframe with 
            a "Date" column.
        
    """
    parsed = date_parser(df["Date"])
    unique_parsed = sorted(list(set(parsed)))
    counts = [parsed.count(i) for i in unique_parsed]
    
    tweets_per_day_df = pd.DataFrame({"Date": unique_parsed, "Tweets": counts})
    tweets_per_day_df.set_index('Date', inplace=True)

    return tweets_per_day_df


def word_splitter(df):
    """
        Splits the sentences in a dataframe's column into a list of 
            separate words and returns the same dataframe with 
            the lists of words in a column named 'Split Tweets'.
    
    Parameters:
        argument1(pd.DataFrame): A Pandas Dataframe with a "Tweets" column 
            that contains strings(Tweets).
        
    """
    df["Split Tweets"] = [i.lower().split() for i in df["Tweets"]]
    return df


def stop_words_remover(df, no_links=False, date_parsed=False):
    """
        Return's the same dataframe with an added column "Without Stop Words" that contains
            the tweet with english stop words removed from the tweet. The tweet is split
            into a list. "stop_words_dict" dictionairy in data/data.py is
            used to spesify the english stop words. 
    
    Parameters:
        argument1(pd.DataFrame): A Pandas Dataframe with a "Tweets" column 
            that contains strings(Tweets).
        argument2(boolean): Optionally removes links from tweets
        argumant3(boolean): Optionally parses "Date" column.
        
    """
    without_stop_words = [[w for w in i if w.lower() not in stop_words_dict["stopwords"]] for i in [i.lower().split() for i in df["Tweets"]]]
    if date_parsed == True:
        df["Date"] = date_parser(df["Date"])
    if no_links == True:
        without_links = [[x for x in i if "http" not in x] for i in without_stop_words]
    df["Without Stop Words"] = without_stop_words
    return df

