# Author : Suman Debnath
# Email : debnath.1@iitj.ac.in
# Roll No : MT19AIE321
# M.Tech-AI(2020) 
# Date : 1st Oct 2020
# DSP Lab 1 

'''
Usage:

$ python DSP_Lab1_MT19AIE321.py 10 5 true          # It will create matrix of size 10x10 and random numbers would range from (0, 5)
$ python DSP_Lab1_MT19AIE321.py 10 100 true        # It will create matrix of size 10x10 and random numbers would range from (0, 100)
$ python DSP_Lab1_MT19AIE321.py 100 500 false      # It will create matrix of size 100x100 and random numbers would range from (0, 500)

true  -> it will print the matrix on console 
false -> it will not print the matrix on console (default is false)

'''

import random                       # Will be used to generate a random number
import sys                          # Will be used to take user input for N, to create NxN matrix
from pprint import pprint as pp     # Will be used to print the matrix on console (if user wants)    



def createMatrix(num, limit):  
    
    matrix = [[random.randint(0,limit) for col in range(num)] for row in range(num)]
    return matrix

def myInsersionSort(a):
    no_elements = len(a)
    for j in range(1,no_elements):
        k = a[j]
        i = j-1

        while i >= 0 and a[i] > k:
            a[i+1] = a[i]
            i = i-1

        a[i+1] = k
        
    return a

def sortMatrixByRow(matrix):
    num = len(matrix)
    for i in range(num):
        matrix[i] = myInsersionSort(matrix[i])
        
    return matrix

def transposeMatrix(matrix):
    num = len(matrix)
    matrix_transposed = [[ matrix[col][row] for col in range(num)] for row in range(num)]
    
    return matrix_transposed

def myBinarySearch(a, search_element):   
    left = 0
    right = len(a)-1
    middle = (left + right)//2 
    
    while left <= right:
        if search_element == a[middle]:
            found_flag = True
            break
        elif search_element < a[middle]:
            right = middle - 1
            middle = (left + right)//2 
        elif search_element > a[middle]:
            left = middle + 1
            middle = (left + right)//2 
    else:
        found_flag = False
        
    return found_flag

def getSmallestCommonNumber(matrix):

    first_column = [matrix[row][0] for row in range(len(matrix))]
    common_elements = []

    for element in first_column:

        for i in range(1, len(matrix)):
            a = [matrix[row][i] for row in range(len(matrix))]
            if myBinarySearch(a, element):
                if i == len(matrix)-1:
                    common_elements.append(element)
                continue
            else:
                break

    if common_elements:
        smallest_common_ele = myInsersionSort(common_elements)[0]
    else:
        smallest_common_ele = -1
    
    return smallest_common_ele

def main():

    # Step 1
    if len(sys.argv) == 1:
        print(f"Need at least TWO argument as the value of N and Max range of Random number generation, for example: \n")
        print(f"$ python {sys.argv[0]} 10 5 true          # It will create matrix of size 10x10 and random numbers would range from (0, 5)")
        print(f"$ python {sys.argv[0]} 10 100 true        # It will create matrix of size 10x10 and random numbers would range from (0, 100)")
        print(f"$ python {sys.argv[0]} 100 500 false      # It will create matrix of size 100x100 and random numbers would range from (0, 500)")
        print("\ntrue  -> it will print the matrix on console")
        print("false -> it will not print the matrix on console (default is false)")
        sys.exit()
    if len(sys.argv) > 3 and sys.argv[3].lower() == "true" :
        print_flag = True
    else:
        print_flag = False

    num = int(sys.argv[1])
    limit = int(sys.argv[2])

    matrix = createMatrix(num, limit)
    print("************************************************************************")
    print("Step 1")
    print("Initial randomly generated Matrix :")
    print("************************************************************************")
    if print_flag:
        pp(matrix)
    print("************************************************************************")

    # Step 2
    matrix = sortMatrixByRow(matrix)
    print("Step 2")
    print("Sorted Matrix (Row wise)")
    print("************************************************************************")
    if print_flag:
        pp(matrix)
    print("************************************************************************")


    # Step 3 
    matrix_transposed = transposeMatrix(matrix)
    print("Step 3")
    print("Transpose of the Matrix")
    print("************************************************************************")
    if print_flag:
        pp(matrix_transposed)
    print("************************************************************************")

    # Step 4
    smallest_comm_ele = getSmallestCommonNumber(matrix_transposed)
    print("Step 4")
    print("************************************************************************")
    print("Finding the smallest COMMON element across all columns(if any)")
    print(f"Smallest Common Element across all columns is : {smallest_comm_ele}\n")
    print(f"NOTE: If the above is -1, that means there is NO common elements across all the columns in the matirx")
    print("************************************************************************")

main()



