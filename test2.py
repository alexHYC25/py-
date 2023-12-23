'''
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

#此為測試共用功能!!!!!黃彥誠2

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




#此為測試共用功能!!!!!李峻硯
'''

from tkinter import Tk, ttk, simpledialog, Listbox
from tkcalendar import Calendar
from datetime import date

root = Tk()

# 設定全域變數
record_listbox = None

# 計算總金額的函數
def calculate_total():
    total_amount = 0
    for record in record_listbox.get(0, Tk.END):
        # 提取金額部分
        amount_str = record.split("金額:")[1].strip()
        try:
            # 將金額轉換為浮點數並加總
            total_amount += float(amount_str)
        except ValueError:
            # 處理金額不是有效數字的情況
            print("金額格式錯誤。")

    # 顯示總金額
    目前_累計金額_顯示.config(text=total_amount)

###-----收入頁面-----###
def open_income():  # 開啟收入介面
    global record_listbox

    income = Tk.Toplevel(root)
    income.title("收入")
    #income.attributes('-fullscreen', True)   # 全螢幕
    label_income = ttk.Label(income, text="請選擇收入日期", font=("Arial", 16))
    label_income.place(x=300, y=50)
    # 創建日期選擇器
    cal = Calendar(income, selectmode="day", year=date.today().year, month=date.today().month, day=date.today().day)
    cal.place(x=270, y=100)
    # 創建一個 Label 用來顯示選擇的日期
    selected_date_label = ttk.Label(income, text="", font=("Arial", 16))
    selected_date_label.place(x=270, y=350)
    
    record_listbox = Listbox(income, width=50, height=10)
    record_listbox.place(x=650, y=150)
    
    # ...以下省略...

    # 創建新增紀錄的按鈕
    btn_add_record = ttk.Button(income, text="新增紀錄", command=add_record, font=("Arial", 12))
    btn_add_record.place(x=1100, y=200)

    # 創建刪除所選項目的按鈕
    btn_delete_record = ttk.Button(income, text="刪除選定項目", command=delete_selected, font=("Arial", 12))
    btn_delete_record.place(x=1100, y=250)

    # 本月金額計算
    目前_累計金額 = ttk.Label(income, text="目前收入總金額", font=("Arial", 18))
    目前_累計金額.place(x=1100, y=500)
    目前_累計金額_顯示 = ttk.Label(income, font=("Arial", 18))
    目前_累計金額_顯示.place(x=1150, y=550)

###-----支出頁面-----###
def open_cost():  # 開啟支出介面
    global record_listbox

    cost = Tk.Toplevel(root)
    cost.title("支出")
    #cost.attributes('-fullscreen', True)   # 全螢幕
    label_cost = ttk.Label(cost, text="請選擇支出日期", font=("Arial", 16))
    label_cost.place(x=300, y=50)
    # 創建日期選擇器
    cal = Calendar(cost, selectmode="day", year=date.today().year, month=date.today().month, day=date.today().day)
    cal.place(x=270, y=100)
    # 創建一個 Label 用來顯示選擇的日期
    selected_date_label = ttk.Label(cost, text="", font=("Arial", 16))
    selected_date_label.place(x=270, y=350)
    
    record_listbox = Listbox(cost, width=50, height=10)
    record_listbox.place(x=650, y=150)
    
    # ...以下省略...

    # 創建新增紀錄的按鈕
    btn_add_record = ttk.Button(cost, text="新增紀錄", command=add_record, font=("Arial", 12))
    btn_add_record.place(x=1100, y=200)

    # 創建刪除所選項目的按鈕
    btn_delete_record = ttk.Button(cost, text="刪除選定項目", command=delete_selected, font=("Arial", 12))
    btn_delete_record.place(x=1100, y=250)

    # 本月金額計算
    目前_累計金額 = ttk.Label(cost, text="目前支出總金額", font=("Arial", 18))
    目前_累計金額.place(x=1100, y=500)
    目前_累計金額_顯示 = ttk.Label(cost, font=("Arial", 18))
    目前_累計金額_顯示.place(x=1150, y=550)

root.mainloop()
