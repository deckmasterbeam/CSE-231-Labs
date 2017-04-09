vowels = ["a", "e", "i", "o", "u"]

word_given = input('Input a word (input "quit" to quit): ')
word = word_given.lower()

while word != "quit":
    if word[0] in vowels:
        print(word+"way")
    else:
        i = 0
        while word[i] not in vowels:
            i +=1
        print(word[i:]+word[:i]+"ay")
    word_given = input('Input a word (input "quit" to quit): ')
    word = word_given.lower() 