#for i in range(1,int(input())):
    #print(10**i * i//9)

#print(10**2 * 2//9)

#print((10**2//9)**2)

def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if (num_vowels % 2) == 0:
            score += 2
        else:
            score += 1
    return int(score)


#print(is_vowel('a'))

n = int(input())
words = input().split()
print(score_words(words))