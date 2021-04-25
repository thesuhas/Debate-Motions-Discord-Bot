from bs4 import BeautifulSoup
import requests
import pandas as pd
import random

def motion_scrape(words, num = 5):
    # If number is non-positive
    if (num < 0):
        return "Cannot give negative number of motions"
    elif (num == 0):
        return "Cannot give zero motions"
    url = ''
    # If only 1 keyword is passed
    if (len(words) == 1):
        url = words[0]
    else:
        for i in range(len(words)):
            if i != len(words) - 1:
                url += words[i] + '+'
            else:
                url += words[i]
    try:
        motions = pd.read_html(f'http://hellomotions.com/search?q={url}&search-motions=')
        df = motions[0]
        motions = random.sample(df['Motion'].tolist(), num)
        motions_ret = ''
        # Generate required string
        for i in range(len(motions)):
            motions_ret += str(i + 1) + '. ' + motions[i] + '\n'

        return motions_ret
    except:
        # If query resulted in 0 results
        return "Please try a different set of keywords"

motion_scrape(['Economics'], 2)