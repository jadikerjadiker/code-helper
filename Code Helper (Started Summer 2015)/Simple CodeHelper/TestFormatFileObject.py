import FormatFileObject as ffo

o = ffo.FormatFileObject("SetterTester.txt")
#dp
print("just about to add item!")
o.addItem(["someone", "has arrived2"])
o.addItem(["London", "has done it simply!"])
print(o.getItem("London"))