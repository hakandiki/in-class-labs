

#find the longest word of sentence entered by user
sentence = input("please a sentence\n")
i = 0
words=[] #creating for store word of the sentence
x = 0
a = 0
while i < len(sentence)-1:
   
    while x < len(sentence) and sentence[x] != " ":
        x += 1
    words.append(sentence[a:x])
    i = x
    a = x = i+1

print(max(words, key = len))
