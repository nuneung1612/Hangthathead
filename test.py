import random
word_list = []
this = ["Brazil", "Laos", "China", "Egypt", "India", "Peru", "Russia", "Serbia", "Turkey", "Fiji", "Nepal",\
    "Libya", "Kenya", "Iran", "Italy", "Japan", "Korea", "France", "Cuba", "Canada"]
for _ in range(5):
    WORD = random.choice(this)
    print(WORD)
    this.remove(WORD)
    print(this)
    WORD = WORD.upper()
    word_list.append(WORD)
print(word_list)
print(len(this))