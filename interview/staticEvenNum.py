#static even number
class evens:
    @staticmethod
    def even(n):
        if n%2==0:
            return "the number is even"
        else:
            return "the number is odd"
print(evens.even(4))