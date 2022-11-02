import csv


class User:
    all_users = []

    # Constructor
    def __init__(self, name: str, age: int, courses=[], is_verified=False):
        self.__name = name
        self.__age = age
        self.__courses = courses
        self.__is_verified = is_verified

        assert age > 0, "Please enter a valid age !!!"

        User.all_users.append(self)

    # Magical method to beautify all users list's elements
    def __repr__(self):
        return f"{self.__class__.__name__}({self.__name}, {self.__age}, {self.__courses}, {self.__is_verified})"

    # Using getters for getting unchangeable attributes
    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def courses(self):
        return self.__courses

    @property
    def is_verified(self):
        return self.__is_verifd

    # Create instances from the data from csv file
    @classmethod
    def instance_initiate(cls, file_name):
        with open(file_name, mode='r') as file:
            csv_file = csv.DictReader(file)
            users = list(csv_file)

            for user in users:
                cls(user["name"], int(user["age"]))

    # Methods
    def verified(self):
        self.__is_verified = True
        print(f"Congratulation {self.__name}, You are verified now.")

    def buy_course(self, course_name):
        if self.__is_verified:
            self.__courses.append(course_name)
            print(f"You successfully bought {course_name} course.")
        else:
            print("Please complete your verification to purchase any course.")
