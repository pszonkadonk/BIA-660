import re
import nltk
import requests
from bs4 import BeautifulSoup
from collections import Counter

#Michael Pszonka
#Lecture 4 Assignment


# Question 1

def split_sentence(line):
    sentence_split = list(filter(None, re.split("\W+", line)))
    print(sentence_split)
    return sentence_split

#Question 2

def pos_counts(fname):
    cnt = Counter()
    article_tags = []
    with open(fname) as article:
        for line in article:
            line = line.strip()
            tokenized = nltk.word_tokenize(line)
            tagged = nltk.pos_tag(tokenized)
            article_tags.append(tagged)
    
    for x in article_tags:
        for word in x:
            tag = word[1]
            if tag in cnt:
                cnt[tag] += 1
            else:
                cnt[tag] = 1
    print(cnt)
    return cnt

#Question 3
# Decided to specify headlines further by grabbing h1 and h2 tags with class=title


def scrape_npr():
    NPR_ORG = "http://www.npr.org"
    soup = BeautifulSoup(requests.get(NPR_ORG).content, 'lxml')
    head_lines = [line.text.strip() for line in soup.find_all(["h1", "h2"], {"class": "title"})]

    print_headlines(head_lines)


def print_headlines(head_lines):
    for l in head_lines:
        print(l)
        print("----------------------")


def run_tests():
    assert split_sentence("this! is,a , sentence...\n\n") == ['this', 'is', 'a', 'sentence']
    assert split_sentence("red+blue=purple!") == ['red', 'blue', 'purple']

    # article.txt contains "The quick brown fox jumps over the lazy dog"
    assert pos_counts("article.txt") == Counter({'NN': 3, 'DT': 2, 'JJ': 2, 'VBZ': 1, 'IN': 1})


if __name__ == '__main__':
    import sys 
    if len(sys.argv) == 2 and sys.argv[1] == "--test":  # valid if we run as python prog.py --test
        run_tests()
    elif len(sys.argv) == 1:
        split_sentence('red+blue=purple!')
        pos_counts("article.txt")        
        scrape_npr()



