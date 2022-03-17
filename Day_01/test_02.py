# def hello():
#     print("hello")
#
#
# hello()

# 完整的for循环
# students = [
#     {"name": "lucy"},
#     {"name": "jack"}
# ]
# find_name = input("please input find name: ")
# for student in students:
#     print(student)
#     if student["name"] == find_name:
#         print("find %s" % find_name)
#         break
# else:
#     print("not find")

a = 10


def test():
    global a
    a = 3
    print(a)

    
def test1():
    print(a)


test()
test1()
