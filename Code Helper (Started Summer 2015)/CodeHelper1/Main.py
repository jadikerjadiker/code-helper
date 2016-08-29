import Tkinter as tk
import CodeHelperVer1 as CH

root=tk.Tk()
theHelper = CH.CodeHelper(root)
theHelper.pack(fill=tk.BOTH, expand=True)

root.bind("<Control-g>", theHelper.go)
root.mainloop()
