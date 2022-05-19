class Stack():
    stk = []

    def isEmpty(self):
        if (self.stk == []):
            print("list is empty")
            return True
        else:
            print("list is not empty")
            return False

    def push(self, data):
        self.stk.append(data)
        print("data is added")
        print(self.stk)
        #top = len(self.stk)-1

    def pop_fun(self):
        if (self.isEmpty()) == True:
            print("UnderFlow Condition")
        else:
            i = self.stk.pop()
            print(i)
            print(self.stk)

    def peek(self):
        if (self.isEmpty() == True):
            print("Under flow")
        else:
            last_index = len(self.stk)-1
            last_element = self.stk[last_index]
            print(self.stk)
            print("Top Element is {}".format(last_element))

    def dispaly_stack(self):
        if (self.isEmpty() == True):
            print("Stack is Empty")
        else:
            last_index = len(self.stk)-1
            last_element = self.stk[last_index]
            print(self.stk)
            print("Top Element is {}".format(last_element))
            print(self.stk)


while True:

    obj = Stack()

    print("\n 1 for check the stack \n"
          "2 for Push\n"
          "3 for Pop\n"
          "4 for peek\n"
          "5 for Display Elements of Stack"
          )
    print("******************************")
    choice = int(input("Enter a choice : "))
    if choice == 1:
        obj.isEmpty()
    elif choice == 2:
        num = int(input("Enter a Number : "))
        obj.push(num)
    elif (choice == 3):
        obj.pop_fun()
    elif (choice == 4):
        obj.peek()
    elif (choice == 5):
        obj.dispaly_stack()
    else:
        print("Invalid: Enter again :")
