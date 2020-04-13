# encoding: utf-8
#@author: wuxing
#@file: insert_sort.py
#@time: 2020/4/9 10:27
#@desc: 插入排序， 选择

import random

def insertsort(data):
    length = len(data)
    for i in range(1, length):
        tmp = data[i]
        j = i - 1
        while tmp< data[j] and j >= 0:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = tmp

    return data

if __name__ == '__main__':
    data = [random.randint(1,100) for _ in range(20)]
    print(insertsort(data))