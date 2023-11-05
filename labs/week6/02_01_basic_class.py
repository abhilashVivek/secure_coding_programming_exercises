# make the most simple class possible


class SimpleClass:
    pass


# create an instance of your SimpleClass and print it out


# now add some functionality to your simple class


class LessSimpleClass:
    pass
    # add one class attribute
    total_iterations = 5

    # add a class method
    def iterate(self):
        for i in range(self.total_iterations):
            print(f"This is iteration no.: {i+1}")


# print out your class attribute both from an instance of the class and through the class directly
# run the method - both directly from the class and through an instance.
x = LessSimpleClass()

print(f"Total Iterations = {x.total_iterations}\n")

x.iterate()