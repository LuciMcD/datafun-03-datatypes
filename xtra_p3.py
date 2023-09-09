"""
Optional bonus. See course site for details.

"""

import doctest


from util_datafun_logger import setup_logger

logger, logname = setup_logger(__file__)


def compare_two_plays():
    ''' This function compares two plays by Shakespeare.'''
    logger.info("Calling compare_two_plays()")

    with open("text_hamlet.txt", "r") as f1:
        text = f1.read()
        wordlist1 = text.split()  # split on whitespace

    #logger.info(f"List of words from play 1: {wordlist1}")
    #wordlist1 contains a lot of words so I'll leave this commented to keep the log clean

    with open("text_juliuscaesar.txt", "r") as f2:
        text = f2.read()
        wordlist2 = text.split()  # split on whitespace

    #logger.info(f"List of words from play 2: {wordlist2}")
    #wordlist2 contains a lot of words so I'll leave the commented to keep the log clean

    wordset1 = set(wordlist1) 
    wordset2 = set(wordlist2)  

    wordset1sort = sorted(wordset1)
    wordset2sort = sorted(wordset2)


   #logger.info(f"The unique sorted words in Hamlet are: {wordset1sort} ")
   #logger.info(f"The unique sorted words in Julius Caesar are: {wordset2sort}")
    #Both unique sets have a large number of words so I'll leave it commented out for now

    maxlen = 10  
    logger.info(f"Our max length of words is {maxlen} letters")
    
    lonword1 = [word for word in wordset1 if len(word) > maxlen]
    
    lonword2 = [word for word in wordset2 if len(word) > maxlen]

    longwordset1 = set(lonword1)  
    longwordset2 = set(lonword2) 

    logger.info(f"longwordset1 is: {longwordset1}")
    logger.info(f"")
    logger.info(f"")
    logger.info(f"longwordset2 is: {longwordset2}")

    
    longwords = longwordset1 & longwordset2
    logger.info(f"The intersection of our 2 sets is: {longwords}")
   
    print(len(longwordset1))
    print(len(longwordset2))
    print(len(longwords))
    print()
    print(f"{sorted(longwords) = }")
    print()

    # check your work
    print("TESTING...if nothing prints before the testing is done, you passed!")
    doctest.testmod()
    print("TESTING DONE")

def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())


# -------------------------------------------------------------
# Call some functions and execute code!

if __name__ == "__main__":
    logger.info("Calling functions from main block")

    compare_two_plays()

    logger.info("Complete the code to compare two plays.")
    show_log()

