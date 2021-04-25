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


def random_words(num):
    url = 'http://hellomotions.com/ten-random-motions'
    html_text = requests.get(url)
    soup = BeautifulSoup(html_text.text, 'lxml')
    motions = soup.find_all('b')
    # Choose number of motions
    final = random.sample(motions, num)
    for i in range(len(final)):
        final[i] = str(final[i])
        final[i] = final[i].lstrip('<b>')
        final[i] = final[i].rstrip('</b>')
    motions_ret = ''
    # Generate required string
    for i in range(len(final)):
        motions_ret += str(i + 1) + '. ' + final[i] + '\n'

    return motions_ret
