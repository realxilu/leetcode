def foo():
    x = 100
    def inside():
        def in2():
            print(x)
        return in2
    return inside


foo()()()