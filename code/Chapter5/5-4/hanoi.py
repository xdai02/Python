move = 0

def hanoi(n, src, mid, dst):
    global move

    if n == 1:
        print(src, "->", dst)
        move += 1
    else:
        # move top n-1 disks from src to mid
        hanoi(n - 1, src, dst, mid)
        print(src, "->", dst)
        move += 1
        # move top n-1 disks from mid to dst
        hanoi(n - 1, mid, src, dst)

def main():
    hanoi(3, "A", "B", "C")
    print("Moves:", move)

if __name__ == "__main__":
    main()