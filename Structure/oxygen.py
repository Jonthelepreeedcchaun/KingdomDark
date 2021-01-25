class oxygen_obj:
    def __init__(self):
        self.paralax_x, self.paralax_y = 0, 0
    def breathe(self, input):
        self.paralax(input)
    def paralax(self, input, weight = 100):
        self.paralax_x, self.paralax_y = input.mx/-weight, input.my/-weight
        return(self.paralax_x, self.paralax_y)
