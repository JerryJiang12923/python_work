import tkinter
import windnd
from tkinter.messagebox import showinfo
def dragged_files(files):
    msg = '\n'.join((item.decode('gbk') for item in files))
    print(msg)
tk = tkinter.Tk()
tk.title("请拖放文件")
windnd.hook_dropfiles(tk,func=dragged_files)
tk.mainloop()
