sentence = input("Please enter a statement: ").lower()
letters = sorted(set(sentence))
ltr_count = {}
for i in letters:
    ltr_count[i] = sentence.count(i)
print(ltr_count)

######
sentence = input("Please enter a statement: ").lower()
key = [j for j in sorted(set(sentence))]
value = [sentence.count(i) for i in sorted(set(sentence))]
print(dict(zip(key,value)))