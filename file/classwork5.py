
class NonPositiveError(UserWarning):
    pass


class handleError:
    def __init__(self, number):
        self.number = number

    def is_number(self):
        try:
            float(self.number)
            return True
        except ValueError:
            return False
        
    def is_positive(self):
        try:
            if self.number > 0:
                return True
        except NonPositiveError:
            return False
def main ():
    while True:
        print("enter a number")
        num = input()
        if handleError(num).is_number():
            print("this is a number")
            return True
        else:
            print("enter a valid number")
            handleError(input()).is_number()
main()