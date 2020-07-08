

#find the longest word of sentence entered by user
sentence = input("please a sentence\n")
i = 0
words=[]
x = 0
a = 0
while i<len(sentence)-1:
   
    while x<len(sentence)-1 and sentence[x]!=" ":
        x+=1
    words.append(sentence[a:x])
    i=x
    a=i+1

print(max(words, key = len))
