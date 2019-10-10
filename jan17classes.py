class Student:
    def __init__(self, first, last, iden):
        self.first_name = first
        self.last_name = last
        self.iden = iden

    def say_name(self):
        print("Hello, my name is ", self.first_name, self.last_name, "\n"
              "My ID number is", self.iden)

    def __eq__(self, other):
        if type(other) is type(self):
            return self.first_name == other.first_name and \
                   self. last_name == other.last_name and \
                   self.iden == other.iden
        
        return False

    def __str__(self):
        return self.iden+','+self.last_name+','+self.first_name
        

class Course:
    def __init__(self, title, number):
        self.title = title
        self.number = number

    def print_info(self):
        print("Title:", self.title, "Number:", self.number)



x = Student("Alice", "A.", "1")
x.say_name()


y = Student("Alice", "A.", "1")
y.say_name()
print(x == y)
      
z = Student("Steve", "C.", "3")
z.say_name()
print(z)

my_list = [x,
           y,
           z]


