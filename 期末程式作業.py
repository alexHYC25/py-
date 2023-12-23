
from tkinter import Tk
from tkinter import messagebox,Button, Frame,Listbox, Scrollbar
import tkinter as Tk
from PIL import Image, ImageTk
from tkinter import ttk, simpledialog
from datetime import date, timedelta
from tkcalendar import Calendar

def toggle_fullscreen(event=None): # 切換全螢幕模式
    state = not root.attributes('-fullscreen')
    root.attributes('-fullscreen', state)
    root.geometry('{0}x{1}+0+0'.format(root.winfo_screenwidth(), root.winfo_screenheight()))


def check_login():# 檢查登入資料
    username = entry_username.get()
    password = entry_password.get()

    if username == "1" and password == "1":
        messagebox.showinfo("登入成功", "歡迎回來，{}".format(username))
        open_index()
    else:
        messagebox.showerror("登入失敗", "使用者名稱或密碼錯誤")

##以下為首頁程式選擇介面
def open_index():  # 開啟首頁
    index = Tk.Toplevel(root)
    index.title("首頁")
    index.attributes('-fullscreen', True)   # 全螢幕
    index.bind('<Escape>', toggle_fullscreen) # 按Esc切換全螢幕模式

    #設定日期
    current_date = date.today()  # 取得當前日期
    date_label = Tk.Label(index, text=current_date.strftime("日期: %Y-%m-%d"), font=("Arial", 40))
    date_label.place(x=440, y=50)

    #設定支出按鈕
    button_cost = Tk.Button(index, text="支出", command=open_cost, font=("Arial", 16), bg="white", fg="black", padx=10, pady=5, relief="raised", bd=2)
    button_cost.pack()
    button_cost.place(x=500, y=500,width=100, height=50)
    
    
    #設定收入按鈕
    button_income = Tk.Button(index, text="收入", command=open_income, font=("Arial", 16), bg="white", fg="black", padx=10, pady=5, relief="raised", bd=2)
    button_income.pack()
    button_income.place(x=700, y=500,width=100, height=50)

    # 創建一個 Frame 作為表格容器
    button_frame = Frame(index)
    button_frame.place(x=1000,y=30)

    #設定財務目標按鈕
    button_goal = Tk.Button(button_frame , text="財務目標", command=open_goal, font=("Arial", 16), bg="white", fg="black", padx=10, pady=5, relief="raised", bd=2,borderwidth=10)
    button_goal.grid(row=0, column=0, sticky="ew")

    #設定財務圖表分析按鈕
    button_analysis = Tk.Button(button_frame , text="財務圖表分析", command=open_analysis, font=("Arial", 16), bg="white", fg="black", padx=10, pady=5, relief="raised", bd=2,borderwidth=10)
    button_analysis.grid(row=1, column=0, sticky="ew")

    #財務分析與建議按鈕
    button_suggestion = Tk.Button(button_frame , text="財務分析與建議", command=open_suggestion, font=("Arial", 16), bg="white", fg="black", padx=10, pady=5, relief="raised", bd=2,borderwidth=10)
    button_suggestion.grid(row=2, column=0, sticky="ew")

    button_frame.grid_columnconfigure(0, weight=1, uniform="equal") # 設定欄寬

    #本月支出金額計算
    # 創建一個 Frame 作為框起來的區域
    frame_labels_cost = Tk.Frame(index, bd=2, relief=Tk.GROOVE)
    frame_labels_cost.place(x=480, y=590, width=150, height=120)

    # 創建第一個 Label
    label_cost = Tk.Label(frame_labels_cost, text="本月支出金額", font=("Arial", 16))
    label_cost.pack(side=Tk.TOP, pady=5)

    # 創建第二個 Label
    label_cost_num = Tk.Label(frame_labels_cost, text="此處放支出金額")
    label_cost_num.pack(side=Tk.TOP)
    
    #本月收入金額計算
    # 創建一個 Frame 作為框起來的區域
    frame_labels_income = Tk.Frame(index, bd=2, relief=Tk.GROOVE)
    frame_labels_income.place(x=680, y=590, width=150, height=120)
    # 創建本月收入金額Label
    label = Tk.Label(frame_labels_income, text="本月收入金額", font=("Arial", 16))
    label.pack(side=Tk.TOP, pady=5)
    # 創建收入金額顯示 Label
    label_cost_num = Tk.Label(frame_labels_income, text="此處放收入金額")
    label_cost_num.pack(side=Tk.TOP)

    #本月盈餘金額計算
    # 創建一個 Frame 作為框起來的區域
    frame_labels_surplus = Tk.Frame(index, bd=2, relief=Tk.GROOVE)
    frame_labels_surplus.place(x=1050, y=400, width=150, height=100)
    # 創建本月盈餘金額Label
    label = Tk.Label(frame_labels_surplus, text="本月盈餘金額", font=("Arial", 16))
    label.pack(side=Tk.TOP, pady=5)
    # 創建盈餘金額顯示 Label
    label_cost_get = Tk.Label(frame_labels_surplus, text="此處放盈餘金額")
    label_cost_get.pack(side=Tk.TOP)

    #全部期間收支金額計算
    # 創建一個 Frame 作為框起來的區域
    frame_labels_all = Tk.Frame(index, bd=2, relief=Tk.GROOVE)
    frame_labels_all.place(x=1050, y=500, width=150, height=100)
    # 創建全部期間收支金額Label
    label = Tk.Label(frame_labels_all, text="全部期間收支金額", font=("Arial", 12))
    label.pack(side=Tk.TOP, pady=5)
    # 創建全部期間收支金額顯示 Label
    label_cost_get = Tk.Label(frame_labels_all, text="此處放全部期間收支金額")
    label_cost_get.pack(side=Tk.TOP)

def open_cost():  # 開啟支出介面
    cost = Tk.Toplevel(root)
    cost.title("支出")
    #cost.attributes('-fullscreen', True)   # 全螢幕
    label_cost = Tk.Label(cost, text="請選擇支出日期", font=("Arial", 16))
    label_cost.place(x=300, y=50)
    # 創建日期選擇器
    cal = Calendar(cost, selectmode="day", year=date.today().year, month=date.today().month, day=date.today().day)
    cal.place(x=270, y=100)
    # 創建一個 Label 用來顯示選擇的日期
    selected_date_label = Tk.Label(cost, text="", font=("Arial", 16))
    selected_date_label.place(x=270, y=350)
    # 創建一個函式用來取得選擇的日期
    def get_selected_date():
        selected_date = cal.get_date()
        selected_date_label.config(text=f"選擇的日期: {selected_date}")
    # 創建一個按鈕用來取得選擇的日期
    btn_get_date = Tk.Button(cost, text="獲取日期", command=get_selected_date, font=("Arial", 14))
    btn_get_date.place(x=330, y=300)
    
    #以下為支出項目選擇
    cost_variety = Tk.Label(cost, text="請選擇支出項目", font=("Arial", 14))
    cost_variety.place(x=650, y=50)
    combo_var = Tk.StringVar()# 創建一個變數來存儲選擇的值
    combo = ttk.Combobox(cost, textvariable=combo_var, values=["飲食", "日常用品", "交通", "水電瓦斯","電話網路","居家","服飾","汽車","娛樂","美容美髮" ])
    combo.place(x=850, y=50)
    
    def on_select(event):
        selected_value = combo_var.get()
        print(f"Selected value: {selected_value}")

    def add_custom_category():
        new_category = simpledialog.askstring("新增支出項目", "請輸入新的支出項目:")
        if new_category:
            combo['values'] = list(combo['values']) + [new_category]
            combo.set(new_category)
            print(f"新增的支出項目: {new_category}")

    add_custom_button = Tk.Button(cost, text="自訂", command=add_custom_category, font=("Arial", 12))
    add_custom_button.place(x=1050, y=45)
    
    #以下為支出金額輸入
    cost_num = Tk.Label(cost, text="請輸入花費的金額", font=("Arial", 14))
    cost_num.place(x=650, y=80)
    cost_money_entry = Tk.Entry(cost,width=22)
    cost_money_entry.place(x=850, y=80)

    record_listbox = Listbox(cost, width=40, height=10)
    record_listbox.place(x=650, y=150)

    def add_record():
        # 在這裡使用選擇的日期
        global selected_date
        date_str = str(selected_date)
        category = combo_var.get()
        amount = cost_money_entry.get()
        record = f"日期: {date_str}, 項目: {category}, 金額: {amount}"
        record_listbox.insert(Tk.END, record)

    def delete_record():
        selected_index = record_listbox.curselection()
        if selected_index:
            record_listbox.delete(selected_index)

    # 新增按鈕用來新增紀錄
    add_record_button = Tk.Button(cost, text="新增紀錄", command=add_record, font=("Arial", 14))
    add_record_button.place(x=650, y=300)

    # 新增按鈕用來刪除紀錄
    delete_record_button = Tk.Button(cost, text="刪除選定紀錄", command=delete_record, font=("Arial", 14))
    delete_record_button.place(x=800, y=300)


def open_income():  # 開啟收入介面
    income = Tk.Toplevel(root)
    income.title("收入")
    

def open_goal():  # 開啟財務目標介面
    goal = Tk.Toplevel(root)
    goal.title("財務目標")


def open_analysis():  # 開啟財務圖表分析介面
    analysis = Tk.Toplevel(root)
    analysis.title("財務圖表分析")


def open_suggestion():  # 開啟財務分析與建議介面
    suggestion = Tk.Toplevel(root)
    suggestion.title("財務分析與建議")


# 建立主視窗
root = Tk.Tk()
root.title("使用者登入")
root.attributes('-fullscreen', True)   # 全螢幕
root.bind('<Escape>', toggle_fullscreen) # 按Esc切換全螢幕模式

# 設定窗口背景圖片
bg_image = Image.open("使用者驗證介面.jpg")  # 替換為你的背景圖片檔案名稱或路徑
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = Tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# 使用者名稱標籤和輸入框
title = Tk.Label(root, text="個人財務管理系統", font=("Arial", 44), fg="white", bg="#000000")
title.pack(pady=20)

# 使用者名稱標籤和輸入框
label_username = Tk.Label(root, text="使用者名稱:", font=("Arial", 16), fg="white", bg="#000000")
label_username.pack(pady=10)
entry_username = Tk.Entry(root, font=("Arial", 14))
entry_username.pack(pady=10)

# 密碼標籤和輸入框
label_password = Tk.Label(root, text="密碼:", font=("Arial", 16), fg="white", bg="#000000")
label_password.pack(pady=10)
entry_password = Tk.Entry(root, show="*", font=("Arial", 14))  # 以星號顯示密碼
entry_password.pack(pady=10)

# 登入按鈕
login_button = Tk.Button(root, text="登入", command=check_login, font=("Arial", 18), bg="#4CAF50", fg="white", padx=15, pady=8)
login_button.pack(pady=30)


# 啟動主迴圈
root.mainloop()

