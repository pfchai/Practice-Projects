#!/usr/bin/env python
# encoding: utf-8

import sys
import Tkinter as tk
import ScrolledText as st
import tkMessageBox
import tkFileDialog as tf
import fileinput

def open_file():
    start = tk.END
    openName = tf.askopenfilename()
    if openName:
        for line in fileinput.input(openName):
            scrolledText.insert(start, line)
        root.title(openName)

def save_file():
    saveName = tf.asksaveasfilename()
    if saveName:
        with open(saveName, 'w') as f:
            f.write(scrolledText.get(1.0, tk.END))
        root.title(saveName)

def close():
    root.destroy()

def die():
    sys.exit(0)

def about():
    tkMessageBox.showinfo("Text Editor", "Tkinter notepad\n")

root = tk.Tk()

frame = tk.Frame(root,width=512)
frame.pack(expand=1)

scrolledText = st.ScrolledText(root, background="white")
scrolledText.pack()

menuBar = tk.Menu(root)

fileMenu = tk.Menu(menuBar)
fileMenu.add_command(label="打开", command=open_file)
fileMenu.add_command(label="保存", command=save_file)
fileMenu.add_command(label="关闭", command=close)
fileMenu.add_separator()
fileMenu.add_command(label="退出", command=die)

helpMenu = tk.Menu(menuBar)
helpMenu.add_command(label="关于",command=about)

menuBar.add_cascade(label="文件",menu=fileMenu)
menuBar.add_cascade(label="帮助",menu=helpMenu)
root.config(menu=menuBar)

root.mainloop()

