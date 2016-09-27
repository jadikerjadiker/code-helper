import re
from decimal import *

def editText(text):
    timeWorked = Decimal(0)
    dollarsPerHour = Decimal(10)
    for line in text.split('\n'):
        if line.find('min')>=0: #if min is in the line
            timeWorked+=Decimal(re.search(r'\d+', line).group(0))
    
    hours = timeWorked/Decimal(60.0)
    print("Total time worked was {} minutes, which is {} hours.".format(timeWorked, hours))
    print("At ${} per hour, that gives you ${} for the time you've worked. Good job!".format(dollarsPerHour, (hours)*dollarsPerHour))

if __name__ == "__main__":
    while True:
        sentinel = "..."
        inputText = '\n'.join(iter(raw_input, sentinel))
        ans = editText(inputText) or None
        if ans!=None:
            print(ans)

