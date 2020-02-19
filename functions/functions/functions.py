import pandas as pd
import numpy as np

ebp_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/electrification_by_province.csv'
ebp_df = pd.read_csv(ebp_url)

for col, row in ebp_df.iloc[:,1:].iteritems():
    ebp_df[col] = ebp_df[col].str.replace(',','').astype(int)

ebp_df.head()

twitter_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'
twitter_df = pd.read_csv(twitter_url)
twitter_df.head()

# gauteng ebp data as a list
gauteng = ebp_df['Gauteng'].astype(float).to_list()

# dates for twitter tweets
dates = twitter_df['Date'].to_list()

# dictionary mapping official municipality twitter handles to the municipality name
mun_dict = {
    '@CityofCTAlerts' : 'Cape Town',
    '@CityPowerJhb' : 'Johannesburg',
    '@eThekwiniM' : 'eThekwini' ,
    '@EMMInfo' : 'Ekurhuleni',
    '@centlecutility' : 'Mangaung',
    '@NMBmunicipality' : 'Nelson Mandela Bay',
    '@CityTshwane' : 'Tshwane'
}

# dictionary of english stopwords
stop_words_dict = {
    'stopwords':[
        'where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon', 
        'may', 'why', 'â€™s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former', 
        'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through', 
        'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to', 
        'their', 'various', 'thereafter', 'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although', 
        'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still', 
        'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see', 'whose', 
        'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take', 
        'became', 'however', 'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind', 
        'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next', 
        'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor', 
        'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever', 
        'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least', 
        'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under', 
        'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call', 
        'nâ€™t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all', 
        'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full', 'themselves', 
        'been', 'in', "'d", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others', 
        "'s", "'re", 'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody', 
        'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten', 
        'hers', 'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely', 'sixty', 
        'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine', 
        'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', 'â€˜ll', 'too', 
        'seems', 'â€™m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow', 
        'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our', 
        'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon', 
        'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t',
        'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me', 
        'same', 'were', 'it', 'every', 'third', 'together'
    ]
}

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
            'q1': round(np.quantile(items, .25), 2),
            'q3': round(np.quantile(items, .75), 2)}


def date_parser(dates):
    """
        Takes a list of datetime strings as input and returns only the date in "yyyy-mm-dd" format.

    Parameters:
        argument1(list): A list of datetime strings.

    """
    return [str(i.date()) for i in [pd.to_datetime(i) for i in dates]]


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
        emails.append([mun_dict[i]
                       for i in x.lower().split(" ") if i in mun_dict.keys()])
        hashtags.append([i[i.find("#"):]
                         for i in x.lower().split(" ") if "#" in i])
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
    without_stop_words = [[w for w in i if w.lower() not in stop_words_dict["stopwords"]] for i in [
        i.lower().split() for i in df["Tweets"]]]
    if date_parsed == True:
        df["Date"] = date_parser(df["Date"])
    if no_links == True:
        without_links = [[x for x in i if "http" not in x]
                         for i in without_stop_words]
    df["Without Stop Words"] = without_stop_words
    return df