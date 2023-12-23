import tkinter as tk
from tkinter import ttk, simpledialog

def on_select(event):
    selected_value = combo_var.get()
    print(f"Selected value: {selected_value}")

def add_custom_category():
    new_category = simpledialog.askstring("新增支出項目", "請輸入新的支出項目:")
    if new_category:
        combo['values'] = list(combo['values']) + [new_category]
        combo.set(new_category)
        print(f"新增的支出項目: {new_category}")

# 創建主視窗
root = tk.Tk()
root.title("支出")

cost_variety = tk.Label(root, text="請選擇支出項目", font=("Arial", 14))
cost_variety.place(x=700, y=50)

combo_var = tk.StringVar()  # 創建一個變數來存儲選擇的值
combo = ttk.Combobox(root, textvariable=combo_var, values=["飲食", "日常用品", "交通"])
combo.place(x=850, y=50)

# 設定預設值
combo.set("選擇一個選項")

# 設定選擇事件
combo.bind("<<ComboboxSelected>>", on_select)

# 添加"自訂"按鈕
add_custom_button = tk.Button(root, text="自訂", command=add_custom_category, font=("Arial", 12))
add_custom_button.place(x=950, y=50)

# 啟動主迴圈
root.mainloop()

#此為測試共用功能!!!!!黃彥誠
#此為測試共用功能!!!!!黃彥誠2

