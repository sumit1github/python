
class List_reverse():
    def reverse_list(self):
        list = [1, 2, 3, 4, 5, 6]
        list1 = []
        for i in range(1, len(list)+1):
            list1.append(list[-i])
        print(list1)


if __name__ == "__main__":
    obj = List_reverse()
    obj.reverse_list()
