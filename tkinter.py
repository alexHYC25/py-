#主視窗（Tk）：
import tkinter as tk

root = tk.Tk()


#標籤（Label）：
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

#按鈕（Button）：
button = tk.Button(root, text="Click Me", command=callback_function)
button.pack()

#輸入框（Entry）：
entry = tk.Entry(root)
entry.pack()

#文本框（Text）：
text_widget = tk.Text(root)
text_widget.pack()

#列表框（Listbox）：
listbox = tk.Listbox(root)
listbox.pack()

#滾動條（Scrollbar）：
scrollbar = tk.Scrollbar(root)

#菜單（Menu）：
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

#對話框（Dialog）：
from tkinter import messagebox
messagebox.showinfo("Title", "Message")

#顏色對話框：
color = tk.colorchooser.askcolor()

#文件對話框：
from tkinter import filedialog

file_path = filedialog.askopenfilename()

#圖像元件（Canvas）：
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

#框架（Frame）：
frame = tk.Frame(root)
frame.pack()

#進度條（Progressbar）：
progress = tk.Progressbar(root, orient="horizontal", length=100, mode="determinate")
progress.pack()
