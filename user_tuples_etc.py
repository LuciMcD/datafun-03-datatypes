"""
Modify this docstring.
In this file we are practicing with tuples, sets, and dictionaries.
"""

from util_datafun_logger import setup_logger;

logger, logname = setup_logger(__file__)

def practice_with_tuples():
    #creating tuples

    tuple1 = ("female", 3, 7, "Missouri", 2)
    tuple2 = ("male", 5, 8, "Tennessee", 1)

    logger.info(f"tuple1: {tuple1}")
    logger.info(f"tuple2: {tuple2}")

    tupleconc = tuple1 + tuple2
    tuple3 = tuple1 *3

    logger.info(f"{tupleconc = }")
    logger.info(f"{tuple3 = }")

    tuple4 = ("MO", "TN", "KS", "IA")
    hasMO = "MO" in tuple4 #True
    hasAZ = "AZ" in tuple4 #False

    logger.info(f"tuple4: {tuple4}")
    logger.info(f"Does tuple4 have MO: {hasMO}")
    logger.info(f"Does tuple4 have AZ: {hasAZ}")

    first = tuple1[0]
    second = tuple1[1]
    last = tuple1[-1]

    logger.info(f"first item in tuple1:{first}")
    logger.info(f"The second item in tuple1 is: {second}")
    logger.info(f"The last item in tuple1: {last}")
    logger.info(f"")

def practice_with_sets():

    set1 = {0, 1, 2, 3, 4}
    set2 = {2, 4, 6, 3, 5}

    logger.info(f"set1 = {set1}")
    logger.info(f"set2 = {set2}")

    set3 = set1 | set2 #union

    set4 = set1 & set2 #intersection

    logger.info(f"The union of set1 and set2 is: {set3}")
    logger.info(f"The intersection of set1 and set2 is: {set4}")
    logger.info(f"")

def practice_with_dictionaries():
    
    dictA = {"gender": "female", "age": 3, "siblings": 2, "state": "MO"}
    dictB = {"gender": "male", "age": 4, "siblings": 3, "state": "KS"}

    logger.info(f"dictA: {dictA}")
    logger.info(f"dictB: {dictB}")

    dictC = {
        "gender": ["female", "male"],
        "age": [1, 2, 3, 4],
        "siblings": [0, 2, 3, 4],
        "states": ["MO", "KS", "IA"]
    }

    logger.info(f"dictC: {dictC}")

    with open("text_zen_of_python.txt") as file_object:
        word_list1 = file_object.read().split()

    word_counts = {}
    for word in word_list1:
        if word in word_counts:
            word_counts[word]+= 1
        else:
            word_counts[word] = 1

    logger.info(f"Given text_zen_python.text, the word_counts = {word_counts}")

    word_counts2 = {word: word_list1.count(word) for word in word_list1}
    
    logger.info(f"The word_counts2: {word_counts2}")
    logger.info(f"")
    

def show_log():
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())


if __name__ == "__main__":
    logger.info("Calling functions from main block")

    practice_with_tuples()
    practice_with_sets()
    practice_with_dictionaries()
    show_log()



