import sys

a = []  # 创建一个空列表对象，refcount 初始至少为 1
print(
    sys.getrefcount(a)
)  # 注意：getrefcount 会把它作为参数临时引用一次，所以结果至少比真实值大 1

b = a  # 赋值，列表的引用计数 +1
print(sys.getrefcount(a))

del b  # 删除引用，引用计数 −1
print(sys.getrefcount(a))

del a  # 再−1，变为 0，立即触发内存释放
