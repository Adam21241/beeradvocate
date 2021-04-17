import numpy as np


def is_float(x):
    """
    Returns True if object is float or float convertible. Otherwise returns false
    """
    
    try:
        float(x)
        return True
    except ValueError:
        return False


def pearson(s1, s2):
    """
    Description:
        Perform Pearson correlation on 2 pd.Series objects
        
    Parameters:
        s1 (pd.Series): first series object to count correlation
        s2 (pd.Series): second series object to count correlation
        
    Returns:
        corr (int): correlation between s1 and s2 (Pearson method)
    """
    
    s1_c = s1 - s1.mean()
    s2_c = s2 - s2.mean()
    corr = np.sum(s1_c * s2_c) / np.sqrt(np.sum(s1_c ** 2) * np.sum(s2_c ** 2))
    
    return corr


def get_recs(beer_name, tbl, num=3):
    """
    Description:
        Find top n beers highly correlated with given one
    
    Parameters:
        beer_name (str): beer for which the function will search most correlated beers
        tbl (pd.DataFrame): correlation matrix
        num (int, default=3): number of most correlated beers to return 

    Returns:
        reviews (list): list of tuples with name of correlated beer 
            and its correlation value with selected beer
    """
    
    reviews = []
    for beer in tbl.columns:
        if beer == beer_name:
            continue
        cor = pearson(tbl[beer_name], tbl[beer])
        if np.isnan(cor):
            continue
        else:
            reviews.append((beer, cor))
    reviews.sort(key=lambda tup: tup[1], reverse=True)
    reviews = reviews[:num]
    
    return reviews