
"""
returns the difference between two words, where the difference
being compute is the levenshtein distance between word1 and
word2.
word1: String
word2: String
"""
def compareWords(word1, word2):
    word1 = list(word1.lower())
    word2 = list(word2.lower())
    d = []
    """Algorithim used for computing levenshtein distance was found
    on the website of https://en.wikipedia.org/wiki/Levenshtein_distance"""
    for i in range(0, len(word1) + 1):
        temp = []
        for j in range(0, len(word2) + 1):
            if (j == 0):
               temp.append(i)
            elif (i ==0):
                temp.append(j)
            else:
                temp.append(0)
        d.append(temp)
        
    for x in range(1, len(word1) + 1):
        for y in range(1, len(word2) + 1):
            if word1[x - 1] == word2[y -1]:
                diff = 0
            else:
                diff = 1
            d[x][y] = min(d[x][y-1] + 1,
                        d[x-1][y] + 1,
                        d[x-1][y-1] + diff)

    return d[len(d) - 1][len(d[0]) - 1]
    
    
    
    
    
