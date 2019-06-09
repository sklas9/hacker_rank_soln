'''
You are given a space separated list of integers.
If all the integers are positive, then you need to check if any integer is a palindromic integer.

Sample Input:
5           #n
12 9 61 5 14  #A

Sample output:
True

Condition 1: All the integers in the list are positive. 
Condition 2: 5 is a palindromic integer.
'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
A=list(map(int,input().split()))
if(all(x>=0 for x in A)):
    if(any(str(x)[::]==str(x)[::-1] for x in A)):
        print("True")
    else:
        print("False")
