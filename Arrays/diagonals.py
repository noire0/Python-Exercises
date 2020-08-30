#!/bin/python

# Given an integer n, produce a two-dimensional array of size (n×n) and complete it according to the following rules, and print with a single space between characters:

#    On the main diagonal write 0 .
#    On the diagonals adjacent to the main, write 1 .
#    On the next adjacent diagonals write 2 and so forth. 

# Print the elements of the resulting array. 

def matrix(n):
    A = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i == j+k or i == j-k:
                    A[i].append(k)
    return A

if __name__ == '__main__':
    n = int(input())
    A = matrix(n)
    for i in range(n):
        print(*A[i])
