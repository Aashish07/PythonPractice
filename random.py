def create_adder(x):
    def adder(y):
        print (x)
        print (y)
        return x+y
    return adder

add_15 = create_adder(15)
print (add_15(0))
print("New---------------")
print (add_15(10))
