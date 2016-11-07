#yup! This totally works. So when defining a environment function, this is the form it should be in.
class test():
    def __init__(self):
        def _():
            print("hello")
        setattr(self, "say hello", _)
        
        def _():
            print("goodbye!")
        setattr(self, "say goodbye", _)
        
        
if __name__ == "__main__":
    t = test()
    getattr(t, "say hello")()
    getattr(t, "say goodbye")()
