def editText(text):
    ans = ""
    text = text.replace('minutes', '+').replace('minute', '+').replace('min', '+').replace('m', '+').replace('hours', '*60+').replace('hour', '*60+').replace('h', '*60+')
    text+='0'
    #print("Converted text: {}".format(text))
    minutes = eval(text)
    ans = "Time: {} hours and {} minutes".format(minutes//60, minutes%60)
    return ans

if __name__ == "__main__":
    while True:
        print("Enter time. Press enter when done.")
        inputText = raw_input()
        try:
            print(editText(inputText)+'\n')
        except Exception as e:
            print("We got an error.")
            print(e)
            print("Sorry, that didn't work. Try again. (Check spelling?)")


