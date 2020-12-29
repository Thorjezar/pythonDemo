"""

定义节点类
节点的属性有，前驱区，数据区和后置区

定义一个双向链表的类，需要满足以下功能
is_empty() 链表是否为空
length() 链表长度
travel() 遍历链表
add(item) 链表头部添加
append(item) 链表尾部添加
insert(pos, item) 指定位置添加
remove(item) 删除节点
search(item) 查找节点是否存在

"""


class Node(object):
    """节点"""
    def __init__(self, item):
        self.elem = item  # 节点的数据区
        self.next = None  # 节点的后置区
        self.prev = None  # 节点的前驱区


class DoubleLinkList(object):  # class DoubleLinkList(SingleLinkList) 对于双链表可以用面向对象继承来实现代码复用
    """双链表"""
    def __init__(self, node=None):
        """初始化一个单链表,node表示可以给定义一个初始的节点，缺省值为空"""
        self.__head = node

    def is_empty(self):
        """判断是否为空"""
        # 为空就是头结点指向的是None
        return self.__head is None

    def length(self):
        """返回长度"""
        # 设置游标来指到单向链表节点
        cur = self.__head
        # 设置计数值
        count = 0
        # 如果不是最后一个节点，就进行加一操作
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历单链表"""
        # 设置游标来指到单向链表节点
        cur = self.__head
        # 如果不是最后一个节点或者不是开始节点，就打印出来这个节点
        while cur is not None:
            print(cur.elem, end=" ")
            cur = cur.next
            # print(cur.elem, end=" ")

    def add(self, item):
        """从头添加节点，头插法"""
        node = Node(item)
        # 将头元素的前驱区指向新节点（新增步骤）
        self.__head.prev = node
        # 将新节点的next域指向原有的头节点
        node.next = self.__head
        # 将头节点替换成新创建的节点
        self.__head = node

    def append(self, item):
        """从尾添加节点,尾插法"""
        # 创建节点对象
        node = Node(item)
        # 如果是空单向链表，那么就将节点绑定到头节点上面
        if self.is_empty():
            self.__head = node
        else:
            # 设置游标指向单向链表节点
            cur = self.__head
            # 如果不是指向最后一个节点，就进行循环
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur  # 补充这句

    def insert(self, pos, item):
        """从任意位置添加节点"""
        if pos < 0:  # 如果传值小于0，代表头插法
            self.add(item)
        elif pos > (self.length()-1):  # 如果传值大于链表的最大值，就在尾部填加，尾插法
            self.append(item)
        else:
            # 定义一个指向pos节点的指针
            cur = self.__head
            # 定义指针位置
            count = 0
            while count < pos:
                count += 1
                cur = cur.next
            # 创建新节点，先改变新节点的next域，然后再改变原有链的节点
            node = Node(item)
            # 先打断的关系新建的node节点
            node.next = cur
            node.prev = cur.prev
            # 再打断原有的关系
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        """移除节点,与list的remove类似，都是从头开始进行，找到符合的就删除"""
        # 先进行遍历
        cur = self.__head
        while cur is not None:  # 想判断到是否是最后一个节点或者是空单链表
            if cur.elem == item:
                # 判断是否是头节点
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        # 判断链表是否只有一个节点
                        cur.next.prev = None
                        return True
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                        return True
            else:
                cur = cur.next
        return False

    def search(self, item):
        """搜索节点"""
        # node = Node(item)
        cur = self.__head
        # if self.length() > 1:
        #     count = 0
        #     while cur.elem != item:
        #         count += 1
        #         cur = cur.next
        #     print(count)
        # else:
        #     print(None)
        while cur is not None:  # 想判断到是否是最后一个节点或者是空单链表
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    dll = DoubleLinkList()
    
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)

    dll.add(7)
    dll.travel()
    dll.insert(3, 100)
    print("\n")
    dll.travel()
    # print("\n")
    # print(dll.search(1111))
    print("\n")
    # print(dll.remove(3))
    # dll.travel()
    # print(dll.remove(5))
    # dll.travel()
    print(dll.remove(7))
    dll.travel()
    # print(dll.remove(2))
    # dll.travel()
    # print(dll.remove(100))
    # dll.travel()