intro = input("introduce yourself:")
word = 1
character = 0
for i in intro:
    character = character+1
    if(i == " "):
        word = word+1
print(word, character)
