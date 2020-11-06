# Author : Suman Debnath
# Email : debnath.1@iitj.ac.in
# Roll No : MT19AIE321
# M.Tech-AI(2020)
# Date : 19th Oct 2020
# DSP Lab 2

import fileinput

def get_good_tuple(a, k):
    n = len(a)
    good_tuple = []
    for i in range(n):
        tmp = a[i] * a[i]
        if tmp <= k:
            good_tuple.append((i, i))
            tmp = a[i]
        else:
            tmp = a[i]
        for j in range(i+1, n):
            tmp = tmp * a[j]
            if tmp <= k:
                good_tuple.append((i, j))
            else:
                break

    return good_tuple

def main():
    # Reading the input from STDIN
    data = []
    for line in fileinput.input():
        data.append(line)
        data = [d.rstrip() for d in data]

    n, k = data[0].split()
    n, k = int(n), int(k)

    a = data[1].split()
    a = [int(i) for i in a]

    result = get_good_tuple(a, k)
    for i in result:
        print(i, end=" ")
    print("\n")

if __name__ == "__main__":
    main()