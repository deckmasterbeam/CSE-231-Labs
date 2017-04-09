
import string
from operator import itemgetter


def add_word( word_map, word ):
    '''
    Adding the words of the file that occur to word_map, and determining 
    how many times those words occur. 
    Values: word_map (list of all the words and their frequencies), word (the 
    word being inputted into the function)
    Returns: Nothing
    '''
    #Saying if the word isn't in the string of words, then it will be added to\
    #the string of words at the count of zero
    if word not in word_map:
        word_map[ word ] = 0

    #Incrementing the count of the word by one
    word_map[ word ] += 1


def build_map( in_file, word_map ):
    '''
    Splits the lines off of the larger file and iterates through the lines
    to determine the frequency of the words within, and adding them to the 
    larger word_map.
    Values: file pointer and word_map (word frequency list)
    Returns: Nothing
    '''
    for line in in_file:

        #Splitting each line into a list of words in the line
        word_list = line.split()

        for word in word_list:

            #Stripping the word of anything other than the word itself, and \
            #converting the word to lowercase 
            if word.count("-") == 0:            
                word = word.strip().strip(string.punctuation).lower()
                add_word( word_map, word )
        

def display_map( word_map ):
    '''
    Takes the words in the frequencies and prints them in a readable and 
    neat format.
    Values: word_map (list of word frequencies)
    Returns: Nothing
    '''
    word_list = list()

    # Iterating through the word_map to create a printable list of tuples
    for word, count in word_map.items():
        word_list.append( (word, count) )

    # Sorting the words according to the frequency at which they occur
    temp_word_list = sorted(word_list, key=str)
    freq_list = sorted( temp_word_list, key=itemgetter(1), reverse=True )

    print( "\n{:15s}{:5s}".format( "Word", "Count" ) )
    print( "-"*20 )
    for item in freq_list:
        print( "{:15s}{:>5d}".format( item[0], item[1] ) )


def open_file(filename):
    '''
    Takes a user input of a file name and attempts to open it.
    Values: file name
    Returns: file pointer
    '''
    while True:
        try:
            in_file = open( filename, "r" )
            return in_file
        except FileNotFoundError:
            print( "\n*** unable to open file ***\n" )
            filename = input("Input a file name: ")

word_map = dict()
in_file = open_file(input("Input a file name: "))

build_map( in_file, word_map )
display_map( word_map )
in_file.close()


