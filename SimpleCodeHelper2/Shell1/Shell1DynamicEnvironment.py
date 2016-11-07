import re

class Shell1DynamicEnvironment():
    def __init__(self):
        self.inputSentinel = "..."
        self.defaultModule = "Shell1Environment"
        
        #prints and returns the result of the addition of the two numbers, num1 and num2 together.
        def _(num1, num2):
            print(num1 + num2)
            return (num1 + num2)
        setattr(self, "add two nums", _)
        
    def __getattr__(self, attribute):
        if re.match(r"^\d*\.?\d+$", attribute): #match a number with or without a decimal
            return eval(attribute)
        else:
            raise AttributeError("Shell1Environment does not have the attribute '{}'".format(attribute))