#!/usr/bin/python3
"""
nqueens backtracking program to print the coordinates of n queens
on an nxn grid such that they are all in non-attacking positions
"""


from sys import argv

if __name__ == "__main__":
    a = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # initialize the answer list
    for p in range(n):
        a.append([p, None])

    def already_exists(y):
        """check that a queen does not already exist in that y value"""
        for z in range(n):
            if q == a[z][1]:
                return True
        return False

    def reject(z, q):
        """determines whether or not to reject the solution"""
        if (already_exists(q)):
            return False
        p = 0
        while(p < z):
            if abs(a[z][1] - q) == abs(p - z):
                return False
            p += 1
        return True

    def clear_a(z):
        """clears the answers from the point of failure on"""
        for p in range(z, n):
            a[p][1] = None

    def nqueens(z):
        """recursive backtracking function to find the solution"""
        for q in range(n):
            clear_a(z)
            if reject(z, q):
                a[z][1] = q
                if (z == n - 1):  # accepts the solution
                    print(a)
                else:
                    nqueens(z + 1)  # moves on to next x value to continue

    # start the recursive process at x = 0
    nqueens(0)
