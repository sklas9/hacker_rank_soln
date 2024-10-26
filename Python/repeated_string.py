'''
https://www.hackerrank.com/challenges/repeated-string/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

There is a string, , of lowercase English letters that is repeated infinitely many times. Given an integer, , find and print the number of letter a's in the first letters of the infinite string.

Example
s = 'abcac'
n=11
The substring we consider is abcacabcaca, the first characters of the infinite string.
There are 5 occurrences of a in the substring
'''
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n

def repeatedString(s, n):
    count_a = 0
    a_in_s = s.count('a')
    quotient = n//len(s)
    remainder = n % len(s)
    a_left_out = s[0:remainder:].count('a')
    count_a = quotient*a_in_s + a_left_out
    return count_a
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()