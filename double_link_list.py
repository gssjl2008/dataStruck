# encoding: utf-8
#@author: wuxing
#@file: double_link_list.py
#@time: 2019/12/25 18:44
#@desc:

class Node:
    def __init__(self, data, head, tail):
        self.data = data
        self.head = head
        self.tail = tail

    def __repr__(self):
        return self.data

class Doublelinklist:

    def __init__(self):
        self.root = None

    def is_empty(self):
        if self.root is None:
            return True

    def add(self, data, front=None):
        if self.is_empty():
            self.root = Node(data, None, None)
            return
        if front:
            self.root = Node(data, None, self.root)
        else:
            cur = self.root
            while cur.tail != None:
                cur = cur.tail
            cur.tail = Node(data, cur, None)

    def remove(self, value):
        if self.is_empty():
            raise ValueError("Doublelinkslist is empty!")

         #  只有一个节点的时候， 直接设为 None
        if self.root.tail is None and self.root.data == value:
            self.root = None
            return

        pre = None
        cur = self.root
        while cur.tail != None:
            print("cur data: %s" %cur.data)
            if cur.data == value:
                try:
                    # 如删除第一个根节点， 则pre为None，会报错，此时，捕捉错误， 将根节点转到根节点的下一个节点
                    pre.tail = cur.tail
                    return
                except AttributeError:
                    self.root = self.root.tail
                    self.root.head = None
                    return
            pre = cur
            cur = cur.tail
        if cur.data == value:
            pre.tail = cur.tail
            return
        else:
            raise ValueError("Linklist has not value %s" %value)


    def all(self):
        if self.is_empty():
            print("Doublelinkslist is empty!")
            return
        result = []
        cur = self.root
        while cur.tail != None:
            info = {'head': cur.head, 'data':cur.data, 'tail':cur.tail}
            result.append(info)
            cur = cur.tail
        result.append({'head': cur.head, 'data': cur.data, 'tail': cur.tail})
        print(result)

if __name__ == '__main__':
    d = Doublelinklist()
    d.add('a')
    d.all()
    # d.remove('a')
    # d.all()
    d.add('b')
    d.all()
    d.remove('b')
    d.all()
    d.add('c')
    d.add('d',front=True)
    d.add('d')
    d.all()
    d.remove('d')
    d.all()