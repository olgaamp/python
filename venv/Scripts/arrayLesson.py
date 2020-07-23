class DynamicArray:
    def __init__(self, length=0):
        self.__items = [0] * length
        self.__size = 0

    def increase_array(self):
        new_count = self.__size * 2
        if self.__size == 0:
            new_count = 4

        new_array = [0] * new_count
        for i in range(self.__size):
            new_array[i] = self.__items[i]

        self.__items = new_array

    def push_back(self, item):
        if self.__size == len(self.__items):
            self.increase_array()

        self.__items[self.__size] = item
        self.__size += 1

    def print(self):
        result = ''
        for i in range(self.__size):
            result += str(self.__items[i]) + ' '

        return result

    def get_count(self):
        return self.__size

    def get(self, index):
        if index >= self.__size or index < 0:
            raise Exception("Индекс находится за пределами массива.")
        return self.__items[index]

    def find(self, key):
        for i in range(self.__size):
            if self.__items[i] == key:
                return i
        return -1

    def find_last(self, key):
        for i in range(self.__size-1,-1,-1):
            if self.__items[i] == key:
                return i
        return -1

    def insert(self, index, item):
        if index < 0 or index > self.__size:
            raise Exception("Выход за пределами массива")

        if self.__size == len(self.__items):
            self.increase_array()

        # сдвигаем все элементы вправо до нужного индекса
        for i in range(self.__size - 1, index - 1, -1):
            self.__items[i + 1] = self.__items[i]

        self.__items[index] = item
        self.__size += 1

    def push_front(self, item):
        self.insert(0, item)

    def push_back_range(self, array):
        for i in range(len(array)):
            self.push_back(array[i])

    def insert_range(self, index, array):
        j=0
        for i in range(index,index+len(array)):
            self.insert(i,array[j])
            j += 1

    def pop_back(self):
        if self.__size == 0:
            raise Exception("Массив пустой.")
        self.__size -= 1

    def remove_by_index(self, index):
        if self.__size == 0:
            raise Exception("Массив пустой!")

        if index < 0 or index >= self.__size:
            raise Exception("Выход за пределами массива")

        for i in range(index + 1, self.__size):
            self.__items[i - 1] = self.__items[i]

        self.__size -= 1

    def pop_front(self):
        self.remove_by_index(0)

    def remove(self, item):
        if self.find(item) !=-1:
            self.remove_by_index(self.find(item))
            return True
        else:
            return False

    def remove_all(self, item):
        k=0
        while self.find(item) != -1:
            self.remove_by_index(self.find(item))
            k += 1
        return k


#
#
#
# array = DynamicArray(6)
#
# array.push_back_range([10,5,8,7,5])  # добавить в конец 10
#
# print(array.print())  # выводит "10 5"
#
# array.push_back_range([10,5,8,7,5])
# print(array.print())
# array.insert_range(3,[1,1,1,1,1,1])
# print(array.print())
# array.remove(1)
# print(array.print())
# k=array.remove_all(1)
# print(array.print(), k)
#
# numbers = []
#
# numbers.append(4)
# numbers.append(4)
# numbers.append(4)
# numbers.append(1)
# numbers.insert(2, 6)
#
# print(len(numbers))
# print(*numbers)
#
# n = int(input())
# array1 = input().split(' ')
#
# for i in array1:
#     i = int(i)
# print(array1)
# p = int(input())
# k = array1.count(p)
# print(k)
# print(array1)

# n = int(input())
# array = input().split(' ')
# for i in range(n):
#      array[i] = int(array[i])
#
# d = input().split(' ')
# k, c = int(d[0]), int(d[1])
# array.append(1)
# n = len(array)+1
#
# # сдвигаем все элементы вправо до нужного индекса
# for i in range(n - 1, k - 1, -1):
#     array[i + 1] = array[i]
# array[k] = c
#
# print(array)



n = int(input())


def color_balls(blist):
    n = len(blist)
    if n == 0:
        return 0
    tmp = []
    p = blist[0]
    k = 1
    for c in blist[1:]:
        if c == p:
            k += 1
        elif k < 3:
            tmp = tmp + [p] * k
            k = 1
        else:
            k = 1
        p = c
    if k < 3:
        tmp = tmp + [p] * k
    d = n - len(tmp)
    if d == 0:
        return 0
    else:
        return d + color_balls(tmp)


def task():
    blist = list(map(int, input().split()))
    return color_balls(blist)


print(task())