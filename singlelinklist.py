# encoding: utf-8
#@author: gssjl2004@126.com
#@file: singlelinklist.py
#@time: 2019/12/25 13:38
#@desc:

from dataclasses import dataclass

# 使用python新版本特性 dataclasses
@dataclass
class Node:
    data: None
    next: None

    # 等同于下面
    # def __init__(self, data, next):
    #     self.data = data
    #     self.next = next

    # 设置 __repr__ 显示具体的值，方便查看
    def __repr__(self):
        return "%s" %(self.data)

class Linklist:

    def __init__(self):
        #  根节点默认None
        self.root = None

    def is_empty(self):
        # 跟节点为None 代表空
        if self.root is None:
            return True

    def size(self):
        if self.root is None:
            return 0
        n = 0
        cur = self.root
        while cur.next != None:
            cur = cur.next
            n += 1
        n += 1
        print("linklist size: %s" %n)
        return n

    def add(self, data, head=False):
        '''
        新增节点， 往后添加，或者前面添加
        :param data:
        :return:
        '''
        if self.is_empty():
            # 根节点为None， 添加第一个节点， next 指向 None
            self.root = Node(data, None)
            return

        if head:
            # 从头部添加，则直接将新节点的next指向以前的根节点， 并重新成为根节点
            self.root = Node(data, self.root)
        else:
            cur = self.root
            # 遍历当前链表，直到cur.nexe 为None时， 将cur.next 指向新的node， 同时新的node的next指向None
            while cur.next != None:
                cur = cur.next
            cur.next = Node(data, None)

    def remove(self, value):
        '''
        删除指定的值
        :param value:
        :return:
        '''
        if self.is_empty():
            raise IndexError('Linklist is empty')

         #  只有一个节点的时候， 直接设为 None
        if self.root.next is None and self.root.data == value:
            self.root = None
            return

        pre = None
        cur = self.root
        while cur.next != None:
            print("cur data: %s" %cur.data)
            if cur.data == value:
                try:
                    # 如删除第一个根节点， 则pre为None，会报错，此时，捕捉错误， 将根节点转到根节点的下一个节点
                    pre.next = cur.next
                    return
                except AttributeError:
                    self.root = self.root.next
                    return
            pre = cur
            cur = cur.next
        if cur.data == value:
            pre.next = cur.next
            return
        else:
            raise ValueError("Linklist has not value %s" %value)

    def pop(self, index=None):
        '''
        默认删除最后一个节点元素
        :param index: 索引号 or None  0 - size
        :return:
        '''
        if index:
            assert index < self.size()

        if self.is_empty():
            raise IndexError('Linklist is empty')

        # 根节点的next为None时，
        if self.root.next is None:
            self.root = None
            return
        if index:
            n = 0
            pre = None
            cur = self.root
            while cur.next != None:
                pre = cur
                cur = cur.next
                n += 1
                if n == index:
                    pre.next = cur.next
                    break
        #  index 等于0时候， 直接将根节点设置为下一个节点
        elif index == 0:
            self.root = self.root.next
        else:
            pre = None
            cur = self.root
            while cur.next != None:
                pre = cur
                cur = cur.next
            pre.next = None

    def all(self):
        '''
        用列表和字典的形式展示链表
        :return:
        '''
        result = []
        if self.is_empty():
            print("Linklist is empty!")
            return

        cur = self.root
        while cur.next != None:
            node = {'data':cur.data, 'next':cur.next}
            cur = cur.next
            result.append(node)
        node = {'data': cur.data, 'next': cur.next}
        result.append(node)
        print(result)
        return result



if __name__ == '__main__':

    s = Linklist()
    s.add('abc')
    s.all()
    s.remove('abc')
    s.all()
    s.add('bcd')
    s.add('cde', head=True)
    s.add('def')
    s.add('efg', head=True)
    s.size()
    s.all()
    s.pop(3)
    s.size()
    s.add('fgi')
    s.all()
    s.remove('efg')
    s.all()

