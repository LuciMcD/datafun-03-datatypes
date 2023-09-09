"""
Modify this docstring.

"""

# imports first
import random

from util_datafun_logger import setup_logger

logger, logname = setup_logger(__file__)

# reusable functions next
#list of ages
list_ages = [0, 1, 2, 3, 4, 5]

#list of number times moved
list_moves = [6, 8, 12, 7, 9, 4]

#list of genders
list_gender = ["female", "male"]

#list number of siblings
list_siblings = [1, 2, 4, 5]

#list of states with foster care
list_states = ["MO", "TN", "KS", "IA", "MN", "NE"]

def using_built_in_functions():
    logger.info(f"Using lists of ages: {list_ages} and the list of moves: {list_moves}")
    ages_moves = list_ages + list_moves
    len_of_ages_moves = len(ages_moves)
    logger.info(f"The length of 2 of our lists is: {len_of_ages_moves}")

    setA = set(list_ages + list_moves + list_siblings)
    logger.info(f"This is a set of values from list_ages, list_moves, and list_siblings: {setA}")

    zipA = list(zip(list_ages, list_moves, list_states))
    logger.info(f"Here are zipped tuples, listed respectively: ages, moves, and states {zipA}")
    logger.info(f"")

def random_choice():
    logger.info("Creating a random chosen list")
    listA = (f"A child,({random.choice(list_gender)}) {random.choice(list_ages)} years old moved {random.choice(list_moves)} times")
    logger.info(f"Random list: {listA}")
    logger.info(f"")

def using_hamlet():
    logger.info("Calling using_hamlet")

    with open("text_hamlet.txt") as fileObject:
        text = fileObject.read()
        list_words = text.split()
        unique_words = set(list_words)
        characters = {"Hamlet", "Claudius", "Gertrude", "Polonius", "Ophelia", "Laertes", "Ghost", "Horatio", "Fortinbras"}
        filtered_set = {word for word in unique_words if word in characters}


    logger.info(f"The following are all the characters of hamlet: {filtered_set}")

    ascA = sorted(filtered_set)
    logger.info(f"The sorted words are {ascA}")

    len2 = len(unique_words)
    logger.info(f"The number of unique words: {len2}")

    len3 = len(filtered_set)
    logger.info(f"The length of the filtered_set: {len3}")

def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())
# call functions and execute code
# use if __name__ == "__main__":
if __name__ == "__main__":
    logger.info("Calling functions from main block")

    using_built_in_functions()
    random_choice()
    using_hamlet()
    show_log()
