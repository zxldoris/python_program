import tkinter as tk
class a(object):
    def __init__(self):
        self.yScroll = tk.Scrollbar(root, orient=tk.VERTICAL).pack()
        self.yScroll.grid(row=0, column=1, sticky=tk.N+tk.S)

        self.xScroll = tk.Scrollbar(self, orient=tk.HORIZONTAL).pack()
        self.xScroll.grid(row=1, column=0, sticky=tk.E+tk.W)

        self.listbox = tk.Listbox(root,
             xscrollcommand=self.xScroll.set,
             yscrollcommand=self.yScroll.set).pack()
        self.listbox.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        self.xScroll['command'] = self.listbox.xview
        self.yScroll['command'] = self.listbox.yview
root = tk.Tk()
b = a()
root.mainloop()
