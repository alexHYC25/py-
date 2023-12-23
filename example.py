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

#可以使用 pack, grid 或 place 等方法來自行決定物件的位置。以下是三種方法的簡單示例(以按鈕為例)：
#使用 pack 方法：
login_button = tk.Button(root, text="登入", command=check_login, font=("Arial", 18), bg="#4CAF50", fg="white", padx=15, pady=8)
login_button.pack(side="bottom", pady=30)
#在這個例子中，side="bottom" 表示將按鈕放在底部，pady=30 表示在按鈕下方添加 30 個像素的垂直間距。

#使用 grid 方法：
login_button = tk.Button(root, text="登入", command=check_login, font=("Arial", 18), bg="#4CAF50", fg="white", padx=15, pady=8)
login_button.grid(row=1, column=0, pady=30)
#在這個例子中，row=1 和 column=0 表示按鈕將位於第二行（索引從 0 開始）的第一列，pady=30 表示在按鈕下方添加 30 個像素的垂直間距。


#使用 place 方法：
login_button = tk.Button(root, text="登入", command=check_login, font=("Arial", 18), bg="#4CAF50", fg="white", padx=15, pady=8)
login_button.place(relx=0.5, rely=0.9, anchor="s")
#在這個例子中，relx=0.5 和 rely=0.9 表示按鈕將位於視窗寬度和高度的 50% 和 90% 的位置，anchor="s" 表示按鈕將在其定位點的底部。

#日期選擇器：
from tkcalendar import DateEntry
def get_selected_date():
    selected_date = cal.get_date()
    print("Selected Date:", selected_date)
# 创建主窗口
root = tk.Tk()
root.title("Date Picker Example")
# 创建日期选择器
cal = DateEntry(root, width=12, background="darkblue", foreground="white", borderwidth=2)
cal.pack(padx=10, pady=10)
# 创建按钮以获取选定的日期
btn_get_date = tk.Button(root, text="Get Selected Date", command=get_selected_date)
btn_get_date.pack(pady=10)


# 創建下拉式選單
combo = ttk.Combobox(root, textvariable=combo_var, values=["選項1", "選項2", "選項3"])
combo.pack(pady=20)