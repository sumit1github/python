from unicodedata import name


class Student():
    data = []

    def create_student(self, name, roll):
        data = {
            "name": name,
            "roll": roll
        }
        self.data.append(data)
        print(self.data)


while True:
    obj = Student()
    obj.create_student("sumit", "25")

