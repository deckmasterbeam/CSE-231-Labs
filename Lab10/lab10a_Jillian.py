
import string

def build_word_set( input_file ):
    
    word_set = set()
    
    for line in input_file:

        # Creates a list of words to be iterated through
        word_lst = line.strip().split()

        # Strips any punctuation that might be attached to any word and 
        # converts to lower case 
        word_lst = [w.lower().strip(string.punctuation) for w in word_lst]
        
        for word in word_lst:
            
            if word != "":

                # Adds the word to a set, giving a set of unique words
                word_set.add( word )
                
    return word_set


def compare_files( file1, file2 ):

    # Build two sets:
    file1_set = build_word_set(file1)
    file2_set = build_word_set(file2)

    # Display the total number of unique words between the
    # two files.  If a word appears in both files, it should
    # only be counted once.
    unique_words = file1_set^file2_set
    print("Number of unique words: ", len(unique_words))

    # Display the number of unique words which appear in both
    # files.  A word should only be counted if it is present in
    # both files.
    similar_words = file1_set & file2_set
    print("Number of similar words: ", len(similar_words))
  
     
######################################################################

f1 = open( "document1.txt" )
f2 = open( "document2.txt" )

compare_files( f1, f2 )

f1.close()
f2.close()

