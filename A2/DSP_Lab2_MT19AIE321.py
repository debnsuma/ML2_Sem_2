# Author : Suman Debnath
# Email : debnath.1@iitj.ac.in
# Roll No : MT19AIE321
# M.Tech-AI(2020)
# Date : 19st Oct 2020
# DSP Lab 2

import sys
import fileinput


class Node:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next


class myLinkedList:

    # Starting point of the LinkedList
    def __init__(self):
        self.head = None
        self.tail = None

    def insertBegining(self, key):

        newNode = Node(key)

        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insertEnd(self, key):

        newNode = Node(key)

        if self.head != None:
            current = self.head

            while current.next != None:
                current = current.next

            current.next = newNode
            self.tail = newNode
        else:
            self.head = newNode
            self.tail = newNode

    def insertInplace(self, key, place):

        total_element = self.length()
        newNode = Node(key)

        # Check 0 - "place" position is not 0
        if place == 0:
            print("Zero is not a valid position, enter any number starting from 1")
            sys.exit()

        # Check 1 - If the insertion is on the 1st place in an empty LinkedList
        elif place == 1 and total_element == 0:
            self.head = newNode

        # Check 2 - If we have a valide insertion position(< total no. of elements)
        elif place > total_element:
            print(f"The LinkedList contains only : {total_element}, can not insert element at : {place} position")
            sys.exit()

        # Check 3 - Add the element at "place" position in a non-empty LinkedList
        elif place != 1:
            position = 1
            current = self.head
            while position != place - 1:
                current = current.next
                position += 1

            newNode.next = current.next
            current.next = newNode

        # Check 4 - If the insertion is on the 1st place in a non-empty LinkedList
        else:
            newNode.next = self.head
            self.head = newNode

    def display(self, save=False):

        current = self.head
        result = []
        while current != None:
            if not save:
                print(current.key, end=" ")
            else:
                result.append(current.key)
            current = current.next

        return result

    def length(self):
        total = 0
        current = self.head
        if self.head == None:
            return 0
        else:
            while current.next != None:
                current = current.next
                total += 1

        return total + 1

    def delete(self, element, LL2):

        total_element = self.length()

        # Check 1 - For empty LinkedList
        if self.head == None:
            print("LinkedList is Empty")

            return LL2

        # Check 2 - Delete the 1st Node or Head Node
        elif self.head.key == element:
            temp = self.head
            self.head = temp.next
            temp = None

            if LL2 == None:
                LL2 = myLinkedList()
                LL2.insertEnd(element)
            else:
                LL2.insertEnd(element)

            return LL2

        # Check 3 - For all other cases
        else:
            current = self.head
            count = 1
            while current.next != None:
                if current.next.key == element:
                    temp = current.next
                    current.next = temp.next
                    temp = None

                    if LL2 == None:
                        LL2 = myLinkedList()
                        LL2.insertEnd(element)
                    else:
                        LL2.insertEnd(element)

                    return LL2

                else:
                    current = current.next

            print("Element not found in the list")

        return LL2

    def rotate_right(self):

        current_tail = self.tail
        current = self.head

        self.head = self.tail
        self.head.next = current

        while current.next != current_tail:
            current = current.next

        self.tail = current
        self.tail.next = None

    def rotate_left(self):

        old_head = self.head

        current_tail = self.tail
        current = self.head

        self.head = self.head.next

        while current.next != current_tail:
            current = current.next

        current = current.next
        current.next = old_head

        self.tail = old_head
        self.tail.next = None


def q1(q1_que):
    LL = myLinkedList()
    LL2 = None

    for q in q1_que:
        task, key = q.split()

        if int(task) == 1:
            LL.insertEnd(int(key))
            LL.display()
            print("\n")
        elif int(task) == 2:
            LL2 = LL.delete(int(key), LL2=LL2)
            LL.display()
            print("\n")

    return LL, LL2


def q2(q2_que, LL=None):
    for q in q2_que:
        q = int(q)
        shift_by = abs(q)

        if q < 0:
            for i in range(shift_by):
                LL.rotate_left()
            LL.display()
            print("\n")

        if q > 0:
            for i in range(shift_by):
                LL.rotate_right()
            LL.display()
            print("\n")

        if q == 0:
            LL.display()
            print("\n")

    return LL


def merge(left, right, arr):
    i, j = 0, 0
    while i + j < len(arr):
        if j == len(right) or (i < len(left) and left[i] < right[j]):
            arr[i + j] = left[i]
            i += 1
        else:
            arr[i + j] = right[j]
            j += 1


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)
        merge(left, right, arr)

    return arr


def main():
    # Reading the input from STDIN
    data = []
    for line in fileinput.input():
        data.append(line)
        data = [d.rstrip() for d in data]

    # Featching Q1 queries
    query1_num = int(data[0])
    q1s = []
    for i in range(1, query1_num + 1):
        q1s.append(data[i])

    # Featching Q2 queries
    query2_num = int(data[query1_num + 1])
    q2s = []
    for i in range(query1_num + query2_num - 1, len(data)):
        q2s.append(data[i])

    LL, LL2 = q1(q1s)

    LL1 = q2(q2s, LL)

    first_list = LL1.display(save=True)

    if LL2 is not None:
        second_list = LL2.display(save=True)
    else:
        second_list = []

    first_list_sorted = mergeSort(first_list)

    if second_list != []:
        second_list_sorted = mergeSort(second_list)
    else:
        second_list_sorted = []

    final_list = first_list_sorted + second_list_sorted

    mergeSort(final_list)

    print("*********** Final Merged List ************")
    for i in final_list:
        print(i, end=" ")
    print("\n********** End of program ****************")


if __name__ == "__main__":
    main()