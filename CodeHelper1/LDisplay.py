import Tkinter as tk
        
class SimpleInputOutputFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, width=1, height=1)
        self.topFrame = ScrollableTextFrame(self)
        self.topFrame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        self.bottomFrame = ScrollableTextFrame(self)
        self.bottomFrame.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)
        self.inputT = self.bottomFrame.text
        self.outputT = self.topFrame.text
        self.outputT.config(state=tk.DISABLED)

    def pOut(self, words):
        self.outputT.config(state=tk.NORMAL)
        self.outputT.insert(tk.END, words)
        self.outputT.config(state=tk.DISABLED)

class ButtonColumnFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, width=1, height=1)
        self.curButtons = []
        
    #todo finish
    def dispButtons(self, *args):
        self.curButtons = []
        for button in args:
            self.curButtons.append(button)
        self.updateButtons()

    def updateButtons(self):
        for button in self.curButtons:
            button.pack(fill=tk.X, side=tk.BOTTOM, expand=True)
        
        
class ScrollableTextFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, width=1, height=1)
        self.text = tk.Text(self, width=1, height=1)
        self.scroller = VerticalScroller(self.text)
        self.text.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)

class VerticalScroller(tk.Scrollbar):
    def __init__(self, text):
        tk.Scrollbar.__init__(self, text.master, orient=tk.VERTICAL, command=text.yview)
        self.pack(side=tk.RIGHT, fill=tk.Y)
        text["yscrollcommand"]=self.set
