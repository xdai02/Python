import time

def main():
    start = time.time()
    print("【开始】%s" % start)

    sum = 0
    for i in range(99999999):
        sum += i
    
    end = time.time()
    print("【结束】%s" % end)

    print("【耗时】%.2fs" % (end - start))

if __name__ == "__main__":
    main()