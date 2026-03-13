class Movie:
    lang="Telugu"
    def  __init__(self,director,hero,tp):
    self.director=
    self.hero = hero

    class Student:
        def __init__(self, name, marks):
            self.name = name
            self.marks = marks

        def is_passed(self):
            return self.marks > 40

    # Creating two student objects
    student1 = Student("Rahul", 75)
    student2 = Student("Anjali", 35)

    # Checking result
    if student1.is_passed():
        print(student1.name, "has passed")
    else:
        print(student1.name, "has failed")

    if student2.is_passed():
        print(student2.name, "has passed")
    else:
        print(student2.name, "has failed")c