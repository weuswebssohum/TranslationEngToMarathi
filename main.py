import itertools
import string

def generate_five_letter_words(length,name):
    # Use lowercase English letters
    letters = string.ascii_lowercase
    # Generate all possible combinations of 'length' letters
    words = itertools.product(letters, repeat=length)

    # Open file in append mode
    with open(name, 'a') as f:
        for word_tuple in words:
            word = ''.join(word_tuple)
            f.write(word + '\n')

# Call the function to generate the words for different lengths
generate_five_letter_words(7,"t7.txt")
print("6 done ")
generate_five_letter_words(6,"t6.txt")
print("6 done ")

generate_five_letter_words(5,"t5.txt")
print("5 done ")

generate_five_letter_words(4,"t4.txt")
print("4 done ")

generate_five_letter_words(3,"t3.txt")
print("3 done ")

generate_five_letter_words(2,"t2.txt")
print("2 done ")

generate_five_letter_words(1,"t1.txt")
print("1 done ")
