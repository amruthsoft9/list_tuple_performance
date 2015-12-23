
# import dis
# import timeit
from timeit import Timer
# import time


def listTest():
    list_data=[3,2,1,4,7,9,5,8,6,10,11,12,14,13,15,19,20,18,16,17,875,345,123,32,45,98,5432,4353,65,99]
    list_data2=[13,76,98,99,1,4,5,7,6]

    # list_data.sort()

    list_data.index(14)   # return 12. position in list
    #  max(list_data)       # return (5432) -> max value in list
    # len(list_data)       # returns the number of elements in the list
    # list_data + list_data2    # list_data2 adds the elements to the list_data
    # list(set(list_data + list_data2)) # set -> remove duplicate elements

def tupleTest():
    tuple_data=(3,2,1,4,7,9,5,8,6,10,11,12,14,13,15,19,20,18,16,17,875,345,123,32,45,98,5432,4353,65,99)
    tuple_data2=(13,76,98,99,1,4,5,7,6)

    # tuple(sorted(tuple_data))

    tuple_data.index(14)    # return 12. position in list

    # max(tuple_data)   # return (5432) -> max value in list
    # len(tuple_data)   # returns the number of elements in the tuple.
    # tuple_data + tuple_data2   # tuple_data2 adds the elements to the tuple_data
    # tuple(set(tuple_data + tuple_data2))    # set -> remove duplicate elements

if __name__=='__main__':
    # Class for timing execution speed of small code snippets.

    t_listTest = Timer(listTest)  # returns the number of seconds it took to execute the code
    print("listTester: " + str(t_listTest.timeit()))


    t_tupleTest = Timer(tupleTest)  # returns the number of seconds it took to execute the code
    print("tupleTester: " + str(t_tupleTest.timeit()))
