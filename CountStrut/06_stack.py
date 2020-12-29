"""

利用顺序表，创建栈
Stack() 创建一个新的空栈
push(item) 添加一个新的元素item到栈顶
pop() 弹出栈顶元素
peek() 返回栈顶元素
is_empty() 判断栈是否为空
size() 返回栈的元素个数

"""


class Stack(object):
    """栈"""
    def __init__(self):
        self.__list = []

    def push(self, item):
        """入栈,在列表的尾部去压栈"""
        self.__list.append(item)

    def pop(self):
        """出栈,如果再尾部填加"""
        self.__list.pop()

    def peek(self):
        """返回栈顶元素,栈顶是列表的尾部"""
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        """判断栈是否为空"""
        return self.__list == []
        # if self.__list:
        #     return True
        # else:
        #     return False

    def size(self):
        """返回栈的元素个数"""
        return len(self.__list)


if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.is_empty())

    print(stack.size())
    
    stack.pop()
    print(stack.size())
    print(stack.peek())