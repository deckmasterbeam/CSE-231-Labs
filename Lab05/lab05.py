dictionary = open("dictionary.txt", "r")

#Part A
print("Part A: find words that contain a, e, i, o, and u in that order")
for word in dictionary:
    a_spot,e_spot,i_spot,o_spot,u_spot = 0,0,0,0,0
    word = word.lower()
    a_spot = word.find("a")
    e_spot = word.find("e")
    i_spot = word.find("i")
    o_spot = word.find("o")
    u_spot = word.find("u")
    if word.count("a") != 1 or word.count("e") != 1 or word.count("i") \
    != 1 or word.count("o") != 1 or word.count("u") != 1:
        continue
    if a_spot == -1 or e_spot == -1 or i_spot == -1 or o_spot == -1 or \
    u_spot == -1:
        continue
    if a_spot < e_spot and e_spot < i_spot and i_spot < o_spot and o_spot \
    < u_spot:
        print(word)
    """for char in word:
        word_strip = word.strip("bcdfghjklmnpqrstvwxyz")
    print(word_strip)
    if word_strip == VOWELS:
        print(word)"""
dictionary.close()
dictionary = open("dictionary.txt", "r")
#Part B
print("Part B: find words that don't contain s and only have a single vowel,\
 y being included as a vowel")
def find_s(word_input):
    for char in word_input:
        if char == "s":
            return True
    return False
    
for word in dictionary:
    if len(word) != 8:
        continue
    word = word.lower()
    s_found = find_s(word)
    if s_found == True:
        continue
    vowel_count = 0
    vowel_count = word.count("a") + word.count("e") + word.count("i") + word.count("o") + word.count("u") + word.count("y")
    if vowel_count == 1:
        print(word)