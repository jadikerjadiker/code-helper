#yup, this works!

import test1

t = test1.Hello()

setattr(t, "hi there!", "bonjour")

print(getattr(t, "hi there!"))
setattr(t, "new", 1506)
print(t.new)