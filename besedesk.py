from calen_gui import *


class basedesk():
    def __init__(self, master):
        self.root = master
        self.root.config()
        self.root.title('时间管理器')
        canlenframe(self.root)


root = Tk()

basedesk(root)
root.mainloop()
