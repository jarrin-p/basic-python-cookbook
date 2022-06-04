# creating a class
class SomeClass:
    # `__init__` is the reserved word for a class constructor in python
    # when defining additional methods for a class, be sure to pass in
    # `self` as the first parameter.
    def __init__(self, param_1, param_2, param_3):
        self.param_1 = param_1
        self.param_2 = param_2
        self.param_3 = param_3

    def get_set_params(self):
        return [self.param_1, self.param_2, self.param_3]

