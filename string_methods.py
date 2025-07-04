# pylint: disable=missing-docstring

# Warning:
# - One line of code for each method
# - Just look in the doc for the right method of the String class!

def add_comma(a_string):
    """
    returns a copy of the string with every word separated by a comma
    example: add_comma("John Peter Jude") => "John, Peter, Jude"
    """
               
    a_stringsplit= a_string.split()
    return ', '.join(a_stringsplit)

print(add_comma("John Peter Jude"))  # YOUR CODE HERE

def belongs_to(a_string, a_word):
    """
    returns True if a_string contains a_word
    example: belongs_to("hey jude", "jude") => True
    """
    return a_word in a_string
    pass  # YOUR CODE HERE


def count_repetition(a_string, a_substring):
    """
    returns how many times a_substring occurs in a_string
    example: count_repetition("000123000123", "0") => 6
    """
    rep=0
    for letter in a_string:
        if a_substring ==letter :
            rep+=1
    return rep
    pass  # YOUR CODE HERE

def is_a_question(a_string):
    """
    returns True if a_string ends with a "?"
    example: is_a_question("How are you?") => True
    """
    return a_string[-1]=='?'
    pass  # YOUR CODE HERE

def remove_surrounding_whitespaces(a_string):
    """
    returns a copy of the string with leading and trailing whitespaces removed
    example: delete_surrounding_whitespaces("  hey yo  ") => "hey yo"
    """
    return a_string.strip()
    pass  # YOUR CODE HERE

def replace(initial_string, old_letter, new_letter):
    """
    returns a copy of the string with the new letter replacing the old one
    example: replace("casanova", "a", "o") => "cosonovo"
    """
    new_string = ''
    for letter in initial_string: 
        if letter==old_letter: 
            new_string=new_string+new_letter
        else :
            new_string=new_string+letter
    return new_string
    pass  # YOUR CODE HERE

def full_description_concatenation(first_name, last_name, age):
    """
    returns a sentence with the first_name and the last_name capitalized and
     the age using concatenation
    example: full_description_concatenation("john", "doe", 33) => "John Doe is 33"
    """
    return(f"{first_name.capitalize()} {last_name.capitalize()} is {age}")
    pass  # YOUR CODE HERE

def full_description_formatting(first_name, last_name, age):
    """
    returns a sentence with the first_name and the last_name capitalized and
     the age using string interpolation
    example: full_description_formatting("john", "doe", 33) => "John Doe is 33"
    """
    return f"{first_name.capitalize()} {last_name.capitalize()} is {age}"
    pass  # YOUR CODE HERE

