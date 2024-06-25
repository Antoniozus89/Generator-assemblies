def create_operation(operation):
    if operation == "multiplication":
        def mult(x, y):
            return x * y

        return mult
    elif operation == "division":
        def div(x, y):
            return x / y

        return div


my_func_div = create_operation("division")
print(my_func_div(32, 2))

square = lambda x, y: x ** y
print(square(7, 2))


def square_def(x, y):
    return x ** y


print(square_def(7, 2))


class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b

    def __str__(self):
        return 'Стороны: {}, {}\nПлощадь: {}'.format(self.a, self.b, self.__call__())


rect = Rect(2, 4)
print(rect)
