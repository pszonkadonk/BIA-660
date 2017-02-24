from collections import Counter

def top_words(words, scores):
    cnt = Counter()
    with open("sample.txt") as rd:
        for line in rd:
            movie_data = line.strip().split("|")
            if(int(movie_data[3]) in scores):
                review = movie_data[2].split(" ")
                for word in review:
                    if word in cnt:
                        cnt[word] += 1
                    else:
                        cnt[word] = 1
        
    return cnt.most_common(words)



foo = top_words(10, [1,3])

print(foo)