#!/usr/bin/env python
# encoding: utf-8

import sys
import Tkinter as tk
import ScrolledText as st
import tkMessageBox
import tkFileDialog as tf
import fileinput

class Editor(tk.Tk):
    """ 用 Tkinter 实现的简单文件编辑器 """

    def __init__(self):
        tk.Tk.__init__(self)
        self.frame = tk.Frame(self,width=512)
        self.frame.pack(expand=1)

        self.scrolledText = st.ScrolledText(self, background="white")
        self.scrolledText.pack()

        self.menuBar = tk.Menu(self)

        fileMenu = tk.Menu(self.menuBar)
        fileMenu.add_command(label="打开", command=self.open_file)
        fileMenu.add_command(label="保存", command=self.save_file)
        fileMenu.add_command(label="关闭", command=self.close)
        fileMenu.add_separator()
        fileMenu.add_command(label="退出", command=self.die)

        helpMenu = tk.Menu(self.menuBar)
        helpMenu.add_command(label="关于",command=self.about)

        self.menuBar.add_cascade(label="文件",menu=fileMenu)
        self.menuBar.add_cascade(label="帮助",menu=helpMenu)
        self.config(menu=self.menuBar)

    def open_file(self):
        start = tk.END
        openName = tf.askopenfilename()
        if openName:
            for line in fileinput.input(openName):
                self.scrolledText.insert(start, line)
            self.title(openName)

    def save_file(self):
        saveName = tf.asksaveasfilename()
        if saveName:
            with open(saveName, 'w') as f:
                f.write(self.scrolledText.get(1.0, tk.END))
            self.title(saveName)

    def close(self):
        self.destroy()

    def die(self):
        sys.exit(0)

    def about(self):
        tkMessageBox.showinfo("Text Editor", "Tkinter notepad\n")

if __name__ == '__main__':
    app = Editor()
    app.mainloop()
