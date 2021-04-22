# TODO: not finished
class Person():
    # class variable
    count = 0

    def __init__(self, name):
        self.name = name

    @classmethod
    def example_class_method(cls):
        pass

    @staticmethod
    def static_method_1():
        pass

    @staticmethod
    def static_method_2(param):
        pass

    def say_my_name(self):
        print('name is ' + self.name)


p1 = Person('Mason')
p2 = Person('Xi')

