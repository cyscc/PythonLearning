class Test:
    count = 0

    @classmethod
    def countNum(cls):
        print(cls.count)

    def __init__(self, name=None, age=None):
        self.name = name
        self.__age = age
        print("创建name为%s对象" % self.name)

    @staticmethod
    def staticMethod():
        print("......")

    def putAge(self):
        print("%s对象的年龄为%d" % (self.name, self.__age))

    def __del__(self):
        print("%s消失了" % self.name)

    def __str__(self):
        return "输出%s对象" % self.name


t1 = Test("cyss")
print(t1.__dir__())
