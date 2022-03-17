def show():
    a = 1
    while a <= 9:
        b = 1
        while b <= a:
            print("%d * %d = %d" % (b, a, a * b), end="\t")
            b += 1
        print("")
        a += 1


# 一般__name__ == "__main__" 下面都是关于这个python模块的测试代码，当其他模块引用这个模块时，其下的测试代码就不会执行
if __name__ == "__main__":
    print(__name__)
    show()
