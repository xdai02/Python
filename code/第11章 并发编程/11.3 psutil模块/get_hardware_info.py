import psutil

def main():
    # CPU信息
    print("【CPU】物理数量：%d" % psutil.cpu_count(logical=False))
    print("【CPU】逻辑数量：%d" % psutil.cpu_count(logical=True))
    print("【CPU】用户用时：%f" % psutil.cpu_times().user)
    print("【CPU】系统用时：%f" % psutil.cpu_times().system)
    print("【CPU】空闲时间：%f" % psutil.cpu_times().idle)

    # 磁盘信息
    print("【磁盘】全部磁盘信息：%s" % psutil.disk_partitions())
    print("【磁盘】D盘使用率：%s" % str(psutil.disk_usage("D:")))
    print("【磁盘】IO使用率：%s" % str(psutil.disk_io_counters()))

    # 网络信息
    print("【网络】数据交换信息：%s" % str(psutil.net_io_counters()))
    print("【网络】接口信息：%s" % str(psutil.net_if_addrs()))
    print("【网络】接口状态：%s" % str(psutil.net_if_stats()))

if __name__ == "__main__":
    main()