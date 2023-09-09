"""
Modify this docstring.

"""

# import some standard modules first - how many can you make use of?
import math
import statistics

# TODO: import from local util_datafun_logger.py 
from util_datafun_logger import setup_logger


# TODO: Call the setup_logger function to create a logger and get the log file name
logger, logname = setup_logger(__file__)


# TODO: Create some shared data lists if you like - or just create them in your functions

# TODO: define some custom functions
#list_1 is a list of numbers representing the number of times a foster child moved homes. The data is made up. 
list_1 = [18, 7, 20, 5, 10, 7, 8, 2, 6, 12, 8, 9, 3, 11, 5, 6, 15, 4, 5, 7]
listx = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #ages of foster children
listy = [6320, 10201, 10504, 11200, 9386, 5754, 5202, 5300, 4800, 4000]#yearly costs for child care based on age
lst = [10, 20, 30, 40]

def list1_statistics():
    logger.info(f"list_1: {list_1}")
    
    mean = statistics.mean(list_1)
    median = statistics.median(list_1)
    mode = statistics.mode(list_1)

    logger.info(f"mean: {mean}")
    logger.info(f"median: {median}")
    logger.info(f"mode: {mode}")

    stdev = statistics.stdev(list_1)
    variance = statistics.variance(list_1)

    logger.info(f"stdev: {stdev: .2f}")
    logger.info(f"variance: {variance: .2f}")
    logger.info(f"")
    logger.info(f"")


def list_correlation_prediction():
    logger.info(f"listx: {listx}")
    logger.info(f"listy: {listy}")

    correlationx_y = statistics.correlation(listx, listy)
    logger.info(f"correlation between x and y: {correlationx_y: .2f}")

    slope, intercept = statistics.linear_regression(listx, listy)
    logger.info(f"The equation of the best fit line is: y = {slope: .2f}x + {intercept: .2f}")

    futurex = 15 #this futurex value is the value given in the project instructions

    newy = slope * futurex + intercept
    
    logger.info(f"We predict that when x = {futurex}, y will be {newy: .2f}")
    logger.info(f"")
    logger.info(f"")

def list_1_built_in_functions():
    min_value = min(list_1)
    max_value = max(list_1)
    len1 = len(list_1)
    sum1 = sum(list_1)

    logger.info(f"The minimum value in list_1 is {min_value}")
    logger.info(f"The maximum value in list_1 is {max_value}")
    logger.info(f"The number of values in the list are: {len1}")
    logger.info(f"The sum of all the values in list_1 is {sum1}")

    average1 = sum1 / len1
    logger.info(f"The average value is {average1}")

    set1 = set(list_1)
    logger.info(f" The set of unique values for list_1 is: {set1}")

    asc1 = sorted(list_1)
    logger.info(f"Using the sorted function we get: {asc1}")

    desc1 = sorted(list_1, reverse=True)
    logger.info(f"Using the sorted reverse function we get: {desc1}")

    logger.info(f"")
    logger.info(f"")

def list_methods():
    logger.info(f"lst: {lst}")

    lst.append(50)
    logger.info(f"The appended list is: {lst}")

    lst.extend([5, 10, 15, 20])
    logger.info(f"The extended lst is: {lst}")

    lst.insert(2, 25)
    logger.info(f"lst after inserting values: {lst}")

    lst.remove(10)
    logger.info(f"The lst after removing a value: {lst}")

    count_of_20 = lst.count(20)
    logger.info(f"the number of 20's is {count_of_20}")

    lst.sort()
    logger.info(f"The ascending list is: {lst}")

    lst.sort(reverse=True)
    logger.info(f"The descending list is: {lst}")

    lst.copy
    logger.info(f"The lstcopy is {lst}")

    first = lst.pop(0)
    logger.info(f"Popped the first item off the top of lstcopy ({first}). Now lstcopy is {lst}")

    last = lst.pop(-1)
    logger.info(f"Popped the last item off the end of lstcopy ({last}). Now lstcopy is {lst}")
    logger.info(f"")
    logger.info(f"")

def list_1_transformations():
    logger.info(f"List_1= {list_1}")

    under10 = list(filter(lambda x: 10 > x, list_1))
    logger.info(f"Times moved under 10: {under10}")


    cubedroot = list(map(lambda x: math.cbrt(x), list_1))
    roundcbrt = [round(x,2) for x in cubedroot ]
    logger.info(f"The cubed root of the numbers is: {roundcbrt}")

    volume = list(map(lambda x: x**3, list_1))
    logger.info(f"The volume of a cube with x length is: {volume}")
    logger.info(f"")
    logger.info(f"")

def list_1_comprehension():
    logger.info(f"List_1: {list_1}")

    under10 = [ x for x in list_1 if x < 10]
    logger.info(f"The under 10 list is {under10}")

    triplelist = [ x*3 for x in list_1]
    logger.info(f"The list-1 tripled is: {triplelist}")

    evenslist = [ x for x in list_1 if x % 2 == 0]
    logger.info(f"The even numbers in list_1 are: {evenslist}")
    logger.info(f"")

def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())

# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":
    logger.info(f"Calling funcions from the main block")
    logger.info(f"All values are rounded to the nearest hundreth")
    # call your functions here (see instructions)
    list1_statistics()
    list_correlation_prediction()
    list_1_built_in_functions()
    list_methods()
    list_1_transformations()
    list_1_comprehension()

    show_log()





