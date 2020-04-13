# encoding: utf-8
#@author: wuxing
#@file: quick_sort.py
#@time: 2020/4/9 10:08
#@desc: 快速排序， 选择一个值，然后遍历数组， 将小于他的放到left， 大于的放到right， 重复操作， 重复操作直到排序好

import random

def quicksort(data:list):
    if len(data) >= 2:
        # mid = data[len(data) // 2]  # 取中间的数
        mid = data[0]
        left, right = [], []
        data.remove(mid)            # 移除这个数
        for i in data:
            if i < mid:
                left.append(i)
            else:
                right.append(i)
        return quicksort(left) + [mid] + quicksort(right)
    else:
        return data

if __name__ == '__main__':
    data = [random.randint(1,100) for _ in range(20)]
    data = [1, 15, 17, 23, 30, 35, 35, 37, 40, 40, 40, 63, 66, 73, 74, 75, 82, 86, 88, 92]
    print(quicksort(data))