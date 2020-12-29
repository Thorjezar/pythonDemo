"""

构建单向链表
python中 等号的本质，是存储对象的内存地址
python中，一切皆对象
Node类是节点类
每一个元素被称为节点
每一个节点中包含元素区和链接区
(elem, nextNode)
SingleLinkList单链表类
实现的方法：
is_empty() 链表是否为空
length() 链表长度
travel() 遍历整个链表
add(item) 链表头部添加元素
append(item) 链表尾部添加元素
insert(pos, item) 指定位置添加元素
remove(item) 删除节点
search(item) 查找节点是否存在

"""


class Node(object):
    """节点类"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    """单链表类"""
    def __init__(self, node=None):
        """初始化一个单链表,node表示可以给定义一个初始的节点，缺省值为空"""
        self.__head = node

    def is_empty(self):
        """判断是否为空"""
        # 为空就是头结点指向的是None
        return self.__head == None

    def length(self):
        """返回长度"""
        # 设置游标来指到单向链表节点
        cur = self.__head
        # 设置计数值
        count = 0
        # 如果不是最后一个节点，就进行加一操作
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历单链表"""
        # 设置游标来指到单向链表节点
        cur = self.__head
        # 如果不是最后一个节点或者不是开始节点，就打印出来这个节点
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
            # print(cur.elem, end=" ")

    def add(self, item):
        """从头添加节点，头插法"""
        node = Node(item)
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
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """从任意位置添加节点"""
        if pos < 0:  # 如果传值小于0，代表头插法
            self.add(item)
        elif pos > (self.length()-1):  # 如果传值大于链表的最大值，就在尾部填加，尾插法
            self.append(item)
        else:
            # 创建新节点，先改变新节点的next域，然后再改变原有链的节点
            node = Node(item)
            # 定义一个指向pos前节点的指针
            pre = self.__head
            # 定义指针位置
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 当循环退出后，指针指向pos-1
            node.next = pre.next
            # 先改变新节点的next域，然后再改变原有链的节点
            pre.next = node

    def remove(self, item):
        """移除节点,与list的remove类似，都是从头开始进行，找到符合的就删除"""
        # 先进行遍历
        cur = self.__head
        pre = None
        while cur is not None:  # 想判断到是否是最后一个节点或者是空单链表
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
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
        while cur != None:  # 想判断到是否是最后一个节点或者是空单链表
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    ll = SingleLinkList()  # 初始化的时候会创建一个空节点里面补充了一个None

    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)

    ll.add(7)
    ll.travel()
    ll.insert(3, 100)
    print("\n")
    ll.travel()
    # print("\n")
    # print(ll.search(1111))
    print("\n")
    # print(ll.remove(3))
    # ll.travel()
    # print(ll.remove(5))
    # ll.travel()
    ll.remove(7)
    ll.travel()
    # print(ll.remove(2))
    # ll.travel()
    # print(ll.remove(100))
    # ll.travel()