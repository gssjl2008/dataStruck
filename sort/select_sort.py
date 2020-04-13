# encoding: utf-8
#@author: wuxing
#@file: select_sort.py
#@time: 2020/4/9 13:42
#@desc: 选择排序， 遍历数组， 将第一个设置为最小值， 依次与后面的数组进行比对， 如果小于【最小值】，则将【最小值】设为新的值，


import random

def selectsort(data):
    length = len(data)
    for i in range(length - 1):
        index = i
        for j in range(i + 1, length):
            if data[j] < data[index]:
                index = j
        data[index], data[i] = data[i], data[index]
    return data



if __name__ == '__main__':
    data = [random.randint(1,100) for _ in range(20)]
    print(f"data: {data}")
    print(selectsort(data))
    print(selectsort(data) == sorted(data))