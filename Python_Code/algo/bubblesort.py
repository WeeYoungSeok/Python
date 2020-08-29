# -*- coding:utf-8 -*-


def bubble(sort_data):
    # 4번만 도는이유는 길이가 5이지만 비교는 4번만하면 전체가 비교된다
    for i in range(sort_data.__len__() - 1):
        # 4번만 도는이유는 같음
        for j in range(sort_data.__len__() - i - 1):
            if(sort_data[j] > sort_data[j+1]):
                sort_data[j],sort_data[j+1] = sort_data[j+1],sort_data[j]
        print(sort_data)
    print(sort_data)


if __name__ == '__main__':
    sort_data = [5, 3, 2, 4, 1]
    print(len(sort_data))
    bubble(sort_data)