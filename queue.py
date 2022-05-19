
class Queqe():
    q = []

    def Is_empty(self):
        if self.q == []:
            print("It is empty")
            return True
        else:
            return False

    def Equeqe(self, data):
        self.q.append(data)
        print("Data is added\n")
        print(self.q)

    def Display(self):
        if self.Is_empty == True:
            print("It is Empty")
        else:
            print(self.q)

    def Dqueqe(self):
        # here i am poping the frist element, means the value with index 0
        if self.Is_empty == True:
            print("It is Empty")
        else:
            self.q.pop(0)
            print(self.q)


while True:
    obj = Queqe()
    print(" \n 1 for Empty queqe checking.\n"
          "2 for display\n"
          "3 for enqueue\n"
          "4 for dqueue"
          )

    choice = int(input(" Enter a choice : "))
    if choice == 1:
        obj.Is_empty()
    elif choice == 3:
        choice = int(input(" Enter a data"))
        obj.Equeqe(choice)
    elif choice == 2:
        obj.Display()
    elif choice == 4:
        obj.Dqueqe()
    else:
        print("Invalid input")
