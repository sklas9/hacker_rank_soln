'''
https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
There is a large pile of socks that must be paired by color.
Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
n=7
ar=[1,2,3,2,2,1,1]
pairs=2
'''

def sockMerchant(n, ar):
    # Write your code here
    pair = 0
    dist_char = set(ar)
    for char in dist_char:
        pair += ar.count(char)//2
    return pair

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()