#bubble_sort 由右向左排序是跟本書做法

number = [3,5,8,1,2,9,4,7,6]

def bubble_sort(number):
    print(number)
    for x in range(0, len(number)):
        print('x=' + str(x))
        try:
            for y in range(len(number) - 1, x, -1):
                print('y=' + str(y), '左=' + str(number[y-1]), '右=' + str(number[y]))
                if number[y-1] > number[y]:
                    number[y-1], number[y] = number[y], number[y-1]
                    print('done 左=' + str(number[y-1]), '右=' + str(number[y]), number)
                else:
                    continue
        except IndexError:
            print("indexerror")
            continue
    return number

print("排序结果:", bubble_sort(number))



