class Student:
    def __init__(self, first, last, ssn, email, age):
        self.first = first
        self.last = last
        self.ssn = ssn
        self.email = email
        self.age = age


    def __eq__(self, rhs):
        if not isinstance(rhs, Student):    # to make sure it doesn't try to check if a student is equal to a clown
            return False                    # well if it does it returns false 
        return self.ssn == rhs.ssn