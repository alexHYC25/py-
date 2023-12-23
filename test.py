'''
import tkinter as tk

def get_text():
    content = text_widget.get("1.0", "end-1c")
    print(content)

root = tk.Tk()
root.title("Text Widget Example")

# 創建 Text 控件
text_widget = tk.Text(root, wrap="word", height=10, width=40)
text_widget.pack(padx=10, pady=10)

# 插入初始文本
text_widget.insert("1.0", "這是一個Text控件。\n可以多行輸入和顯示。")

# 創建一個按鈕，當按下時取得 Text 內容
button = tk.Button(root, text="取得 Text 內容", command=get_text)
button.pack(pady=10)




root.mainloop()

import tkinter as tk
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

# 启动主循环
root.mainloop()
'''

import tkinter as tk
from tkinter import ttk

def on_select(event):
    selected_value = combo_var.get()
    print(f"Selected value: {selected_value}")

# 創建主視窗
root = tk.Tk()
root.title("下拉式選單範例")

# 創建一個變數來存儲選擇的值
combo_var = tk.StringVar()

# 創建下拉式選單
combo = ttk.Combobox(root, textvariable=combo_var, values=["選項1", "選項2", "選項3"])
combo.pack(pady=20)

# 設定預設值
combo.set("選擇一個選項")

# 設定選擇事件
combo.bind("<<ComboboxSelected>>", on_select)

# 啟動主迴圈
root.mainloop()