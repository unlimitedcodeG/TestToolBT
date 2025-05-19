class Node:
    def __init__(self):
        self.next = None


a = Node()
b = Node()
a.next = b
b.next = a  # a 和 b 互相引用

del a, b  # 引用计数都减为 1，但永远无法到 0
# 如果没有分代 GC，这两块内存将泄漏
import gc

gc.disable()  # 关闭自动分代GC
gc.enable()  # 开启
gc.collect()  # 手动触发一次完整的分代GC，返回回收的对象数量
gc.get_threshold()  # 查看当前三代阈值，默认 (700, 10, 10)
gc.set_threshold(1000, 15, 15)  # 调整阈值
