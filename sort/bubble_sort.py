# encoding: utf-8
#@author: wuxing
#@file: bubble_sort.py
#@time: 2020/4/9 10:14
#@desc: 冒泡排序，比较两个位置的大小，然后交换位置

import random

def bubblesort(data):
    print(f"data: {data}")
    length = len(data)
    totle = 0
    for i in range(length - 1):
        count = 0                               # 用0 来优化， 提高效率
        for j in range(i, length):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
                totle += 1
                count += 1
        if i != 0:
            if count == 0:
                print(f"totle: {totle}")
                print(f"count: {count}")
                print(sorted(data) == data)
                print(f"sort: {sorted(data)}")
                return data
    print(f"totle: {totle}")
    print(f"count: {count}")
    print(sorted(data) == data)
    print(f"sort: {sorted(data)}")
    return data

if __name__ == '__main__':
    data = [random.randint(1,100) for _ in range(20)]
    print(f"result: {bubblesort(data)}")