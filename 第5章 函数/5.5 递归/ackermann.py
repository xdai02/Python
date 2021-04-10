"""
    Ackermann's Function 
	              ①        n + 1             m = 0
	    A(m, n) = ②      A(m-1, 1)           m > 0, n = 0
	              ③  A(m-1, A(m, n-1))       m > 0, n > 0
"""
def A(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return A(m-1, 1)
    else:
        return A(m-1, A(m, n-1))

def main():
    print(A(3, 4))

if __name__ == "__main__":
    main()