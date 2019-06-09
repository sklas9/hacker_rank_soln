'''You are given a spreadsheet that contains a list of N athletes and their details (such as age, height, weight and so on). 
You are required to sort the data based on the Kth attribute and print the final resulting table. 
Follow the example given below for better understanding.'''

Sample input:
5 3      #N, M
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1         #K

Sample output:
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12

The details are sorted based on the second attribute, since K is zero-indexed.

Solution:
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    sorted_arr = sorted(arr,key=lambda arr : arr[k])
    for i in range(n):
        print(*sorted_arr[i])
