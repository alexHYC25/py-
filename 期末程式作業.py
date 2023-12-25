from tkinter import Tk
from tkinter import messagebox,Button, Frame,Listbox, Scrollbar
import tkinter as Tk
from PIL import Image, ImageTk
from tkinter import ttk, simpledialog
from datetime import date, timedelta
from tkcalendar import Calendar
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

def run_once():
    global total_amount
    global total_cost
    global label_income_num
    global global_photo
    global run_once_has_run
    if not run_once_has_run:
        print("This will only run once")
        run_once_has_run = True
        total_amount = 0
        total_cost=0
        label_income_num = None
        global_photo = None
        
run_once_has_run = False  # 初始化標記為False，表示尚未運行

#更新本月收入金額
def update_income_label(new_amount):
    global label_income_num
    global root
    label_income_num.config(text=str(new_amount))
    root.update()
    root.update_idletasks()

# 設置中文字體
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 將字體設置為支援中文的字型，例如 'Arial Unicode MS'
plt.rcParams['axes.unicode_minus'] = False  # 解決負數無法正常顯示的問題

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
    global label_income_num
    global global_photo
    global root
    index = Tk.Toplevel(root)
    index.title("首頁")
    index.attributes('-fullscreen', True)   # 全螢幕
    index.bind('<Escape>', toggle_fullscreen) # 按Esc切換全螢幕模式

    bg_image_index = Image.open("首頁.jpg")  # 替換為你的背景圖片檔案名稱或路徑
    bg_photo_index = ImageTk.PhotoImage(bg_image_index)
    bg_label_index = Tk.Label(index, image=bg_photo_index)
    bg_label_index.place(relwidth=1, relheight=1)

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
    button_frame.place(x=5,y=50)

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
    label_cost_num = Tk.Label(frame_labels_income, text=total_amount)
    label_cost_num.pack(side=Tk.TOP)
    #本月盈餘金額計算
    # 創建一個 Frame 作為框起來的區域
    frame_labels_surplus = Tk.Frame(index, bd=2, relief=Tk.GROOVE)
    frame_labels_surplus.place(x=25, y=400, width=150, height=100)
    # 創建本月盈餘金額Label
    label = Tk.Label(frame_labels_surplus, text="本月盈餘金額", font=("Arial", 16))
    label.pack(side=Tk.TOP, pady=5)
    # 創建盈餘金額顯示 Label
    label_cost_get = Tk.Label(frame_labels_surplus, text="此處放盈餘金額")
    label_cost_get.pack(side=Tk.TOP)

    #全部期間收支金額計算
    # 創建一個 Frame 作為框起來的區域
    frame_labels_all = Tk.Frame(index, bd=2, relief=Tk.GROOVE)
    frame_labels_all.place(x=25, y=500, width=150, height=100)
    # 創建全部期間收支金額Label
    label = Tk.Label(frame_labels_all, text="全部期間收支金額", font=("Arial", 12))
    label.pack(side=Tk.TOP, pady=5)
    # 創建全部期間收支金額顯示 Label
    label_cost_get = Tk.Label(frame_labels_all, text="此處放全部期間收支金額")
    label_cost_get.pack(side=Tk.TOP)

    image_path = "歡迎使用個人記帳管理系統.jpg"  # 替換為您的圖片檔案路徑
    original_image = Image.open(image_path)
    resized_image = original_image.resize((300, 300))
    global_photo = ImageTk.PhotoImage(resized_image)

    

    # 在視窗中顯示圖片
    image_label = Tk.Label(index, image=global_photo)
    image_label.image = global_photo  # 保留對 PhotoImage 的引用，防止被垃圾回收
    image_label.place(x=500, y=150)  # 調整 x 和 y 的值以控制圖片的位置
    
    index.mainloop()





###-----支出頁面-----###
def open_cost():  # 開啟支出介面
    global combo
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
    
    record_listbox = Listbox(cost, width=50, height=10)
    record_listbox.place(x=650, y=150)
    # 創建一個函式用來取得選擇的日期
    def get_selected_date():
        selected_date = cal.get_date()
        selected_date_label.config(text=f"選擇的日期: {selected_date}")

    def add_record():
        global total_amount
        date_str = selected_date_label.cget("text")
        category = combo_var.get()
        amount_str = cost_money_entry.get()

        try:
            # 將輸入的金額轉換為浮點數
            amount = float(amount_str)

            # 更新總金額變數
            total_amount += amount

            # 更新列表
            record = f"{date_str}, 項目: {category}, 金額: {amount}"
            record_listbox.insert(Tk.END, record)

            # 清空輸入框
            cost_money_entry.delete(0, Tk.END)

            # 顯示目前總金額
            目前_累計金額_顯示.config(text= total_amount)

        except ValueError:
            # 處理金額不是有效數字的情況
            print("請輸入有效的金額。")
    
    def delete_selected():
        global total_amount

        selected_index = record_listbox.curselection()
        if selected_index:
            # 獲取刪除的項目資訊
            deleted_item = record_listbox.get(selected_index)
        
            # 切割資訊以獲取金額
            amount_str = deleted_item.split("金額:")[1].strip()

            try:
                # 將刪除的金額轉換為浮點數
                deleted_amount = float(amount_str)

                # 更新總金額變數
                total_amount -= deleted_amount

                # 刪除列表中的項目
                record_listbox.delete(selected_index)

                # 顯示更新後的總金額
                目前_累計金額_顯示.config(text=total_amount)

            except ValueError:
                # 處理金額不是有效數字的情況
                print("金額格式錯誤。")

    # 在返回按钮的回调函数中更新标签文本
    def open_cost_pie_chart():
        cost_pie_chart = Tk.Toplevel(root)
        cost_pie_chart.title("支出圓餅圖")

        # 獲取支出列表中的項目和金額
        items = []
        amounts = []
        for item in record_listbox.get(0, Tk.END):
            parts = item.split(", ")
            items.append(parts[1].split(": ")[1])  # 項目
            amounts.append(float(parts[2].split(": ")[1]))  # 金額

        # 設置圓餅圖資料
        labels = items  # 各部分的標籤
        sizes = amounts  # 各部分的大小（百分比）
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']  # 顏色
        explode = tuple(0.1 if i == max(amounts) else 0 for i in amounts)
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        ax.axis('equal')
        ax.set_title('支出圓餅圖')

        canvas = FigureCanvasTkAgg(fig, master=cost_pie_chart)
        canvas.draw()
        canvas.get_tk_widget().pack()
        
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

    # 創建新增紀錄的按鈕
    btn_add_record = Tk.Button(cost, text="新增紀錄", command=add_record, font=("Arial", 12))
    btn_add_record.place(x=1100, y=200)

    # 創建刪除所選項目的按鈕
    btn_delete_record = Tk.Button(cost, text="刪除選定項目", command=delete_selected, font=("Arial", 12))
    btn_delete_record.place(x=1100, y=250)

    #本月金額計算
    目前_累計金額 = Tk.Label(cost, text="目前支出總金額", font=("Arial", 18))
    目前_累計金額 .place(x=1100, y=500)
    目前_累計金額_顯示 = Tk.Label(cost,font=("Arial", 18))
    目前_累計金額_顯示.place(x=1150, y=550)

    # 創建新增圓餅圖的按鈕
    btn_add_record = Tk.Button(cost, text="新增圓餅圖", command=open_cost_pie_chart, font=("Arial", 12))
    btn_add_record.place(x=1100, y=300)

    


###-----收入頁面-----###
def open_income():  # 開啟收入介面
    income = Tk.Toplevel(root)
    income.title("收入")
    #income.attributes('-fullscreen', True)   # 全螢幕
    label_income = Tk.Label(income, text="請選擇收入日期", font=("Arial", 16))
    label_income.place(x=300, y=50)
    # 創建日期選擇器
    cal = Calendar(income, selectmode="day", year=date.today().year, month=date.today().month, day=date.today().day)
    cal.place(x=270, y=100)
    # 創建一個 Label 用來顯示選擇的日期
    selected_date_label = Tk.Label(income, text="", font=("Arial", 16))
    selected_date_label.place(x=270, y=350)
    
    record_listbox = Listbox(income, width=50, height=10)
    record_listbox.place(x=650, y=150)

    def on_income_close():
        global total_amount
        global label_income_num
        global root
        update_income_label(total_amount)
        income.destroy()
        label_income_num.update_idletasks()
        root.update_idletasks()
        root.update()
        print("收入介面已關閉，更新首頁")

    # 創建一個函式用來取得選擇的日期
    def get_selected_date():
        selected_date = cal.get_date()
        selected_date_label.config(text=f"選擇的日期: {selected_date}")

    def add_record():
        global total_amount

        date_str = selected_date_label.cget("text")
        category = combo_var.get()
        amount_str = income_money_entry.get()

        try:
            # 將輸入的金額轉換為浮點數
            amount = float(amount_str)

            # 更新總金額變數
            total_amount += amount

            # 更新列表
            record = f"{date_str}, 項目: {category}, 金額: {amount}"
            record_listbox.insert(Tk.END, record)

            # 清空輸入框
            income_money_entry.delete(0, Tk.END)

            # 顯示目前總金額
            目前_累計金額_顯示.config(text= total_amount)

        except ValueError:
            # 處理金額不是有效數字的情況
            print("請輸入有效的金額。")
    
    def delete_selected():
        global total_amount

        selected_index = record_listbox.curselection()
        if selected_index:
            # 獲取刪除的項目資訊
            deleted_item = record_listbox.get(selected_index)
        
            # 切割資訊以獲取金額
            amount_str = deleted_item.split("金額:")[1].strip()

            try:
                # 將刪除的金額轉換為浮點數
                deleted_amount = float(amount_str)

                # 更新總金額變數
                total_amount -= deleted_amount

                # 刪除列表中的項目
                record_listbox.delete(selected_index)

                # 顯示更新後的總金額
                目前_累計金額_顯示.config(text=total_amount)

            except ValueError:
                # 處理金額不是有效數字的情況
                print("金額格式錯誤。")
    
    # 創建一個按鈕用來取得選擇的日期
    btn_get_date = Tk.Button(income, text="獲取日期", command=get_selected_date, font=("Arial", 14))
    btn_get_date.place(x=330, y=300)

    #以下為收入項目選擇
    income_variety = Tk.Label(income, text="請選擇收入項目", font=("Arial", 14))
    income_variety.place(x=650, y=50)
    combo_var = Tk.StringVar()# 創建一個變數來存儲選擇的值
    combo = ttk.Combobox(income, textvariable=combo_var, values=["薪水", "獎金", "投資", "其他" ])
    combo.place(x=850, y=50)

    def on_select(event):
        selected_value = combo_var.get()
        print(f"Selected value: {selected_value}")
    
    def add_custom_category():
        new_category = simpledialog.askstring("新增收入項目", "請輸入新的收入項目:")
        if new_category:
            combo['values'] = list(combo['values']) + [new_category]
            combo.set(new_category)
            print(f"新增的收入項目: {new_category}")

    def open_income_pie_chart():
        income_pie_chart = Tk.Toplevel(root)
        income_pie_chart.title("收入圓餅圖")

        # 獲取收入列表中的項目和金額
        items = []
        amounts = []
        for item in record_listbox.get(0, Tk.END):
            parts = item.split(", ")
            items.append(parts[1].split(": ")[1])  # 項目
            amounts.append(float(parts[2].split(": ")[1]))  # 金額

        # 設置圓餅圖資料
        labels = items  # 各部分的標籤
        sizes = amounts  # 各部分的大小（百分比）
        colors = ['#' + ''.join(random.choices('0123456789ABCDEF', k=6)) for _ in range(len(labels))]  # 顏色
        explode = tuple(0.1 if i == max(amounts) else 0 for i in amounts)
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        ax.axis('equal')
        ax.set_title('收入圓餅圖')

        canvas = FigureCanvasTkAgg(fig, master=income_pie_chart)
        canvas.draw()
        canvas.get_tk_widget().pack()

    add_custom_button = Tk.Button(income, text="自訂", command=add_custom_category, font=("Arial", 12))
    add_custom_button.place(x=1050, y=45)

    #以下為收入金額輸入
    income_num = Tk.Label(income, text="請輸入收入金額", font=("Arial", 14))
    income_num.place(x=650, y=80)
    income_money_entry = Tk.Entry(income,width=22)
    income_money_entry.place(x=850, y=80)

    # 創建返回的按鈕
    btn_return = Tk.Button(income, text="返回", command=on_income_close ,font=("Arial", 12))
    btn_return.place(x=1100, y=400)
    # 創建新增紀錄的按鈕
    btn_add_record = Tk.Button(income, text="新增紀錄", command=add_record, font=("Arial", 12))
    btn_add_record.place(x=1100, y=200)

    # 創建刪除所選項目的按鈕
    btn_delete_record = Tk.Button(income, text="刪除選定項目", command=delete_selected, font=("Arial", 12))
    btn_delete_record.place(x=1100, y=250)

    #本月金額計算
    目前_累計金額 = Tk.Label(income, text="目前收入總金額", font=("Arial", 18))
    目前_累計金額 .place(x=1100, y=500)
    目前_累計金額_顯示 = Tk.Label(income,font=("Arial", 18))
    目前_累計金額_顯示.place(x=1150, y=550)

    # 創建新增圓餅圖的按鈕
    btn_add_record = Tk.Button(income, text="新增圓餅圖", command=open_income_pie_chart, font=("Arial", 12))
    btn_add_record.place(x=1100, y=300)
    income.protocol("WM_DELETE_WINDOW", on_income_close)
###-----財務目標頁面-----###
def open_goal():
    global selected_cost_limit_label, selected_income_goal_label,selected_cost_limit,selected_income_goal
    goal = Tk.Toplevel(root)
    goal.title("財務目標")
    #goal.attributes('-fullscreen', True)   # 全螢幕
    label_goal = Tk.Label(goal, text="財務目標", font=("Arial", 40))
    label_goal.place(x=100, y=150)
    #設定支出上限按鈕
    button_cost_limit = Tk.Button(goal, text="設定支出上限", command=open_cost_limit, font=("Arial", 16), bg="white", fg="black", padx=10, pady=5, relief="raised", bd=2,borderwidth=10)
    button_cost_limit.pack()
    button_cost_limit.place(x=100, y=300,width=200, height=80)
    #設定儲蓄目標按鈕
    button_income_goal = Tk.Button(goal , text="設定儲蓄目標", command=open_income_goal, font=("Arial", 16), bg="white", fg="black", padx=10, pady=5, relief="raised", bd=2,borderwidth=10)
    button_income_goal.pack()
    button_income_goal.place(x=100, y=400,width=200, height=80)
    # 創建一個 Label 用來顯示目前支出
    selected_cost_limit = Tk.Label(goal, text="0", font=("Arial", 16))
    selected_cost_limit.place(x=500, y=325)
    # 創建一個 Label 用來顯示目前收入
    selected_income_goal = Tk.Label(goal, text="0", font=("Arial", 16))
    selected_income_goal.place(x=500, y=425)
    # 創建一個 Label 用來顯示/
    selected_slash1 = Tk.Label(goal, text="/", font=("Arial", 16))
    selected_slash1.place(x=600, y=425)
    # 創建一個 Label 用來顯示/
    selected_slash2 = Tk.Label(goal, text="/", font=("Arial", 16))
    selected_slash2.place(x=600, y=325)
    # 創建一個 Label 用來顯示設定的支出上限
    selected_cost_limit_label = Tk.Label(goal, text="0", font=("Arial", 16))
    selected_cost_limit_label.place(x=700, y=325)
    # 創建一個 Label 用來顯示設定的儲蓄目標
    selected_income_goal_label = Tk.Label(goal, text="0", font=("Arial", 16))
    selected_income_goal_label.place(x=700, y=425)
    # 創建一個 Label 用來顯示「目標」
    show_goal = Tk.Label(goal, text="目標", font=("Arial", 20))
    show_goal.place(x=680, y=280)

    # 創建一個 Label 用來顯示「目前」
    show_now = Tk.Label(goal, text="目前", font=("Arial", 20))
    show_now.place(x=470, y=280)

def open_cost_limit():
    def set_limit_cost():
        global cost_limit_value
        cost_value = cost_money_entry.get()
        # 可在這裡進行其他操作或儲存值
        cost_limit_value = cost_value  # 將值存儲到全局變數中
        selected_cost_limit_label.config(text=cost_limit_value)  # 更新主要介面的標籤
        cost_limit.destroy()
    cost_limit = Tk.Toplevel(root)
    cost_limit.title("設定支出上限")
    cost_money_entry = Tk.Entry(cost_limit, width=22)
    cost_money_entry.place(x=20, y=50)
    button_cost_limit = Tk.Button(cost_limit, text="設定", command=set_limit_cost, font=("Arial", 12), bg="white", fg="black", padx=10, pady=5, relief="raised", bd=2)
    button_cost_limit.pack()
    button_cost_limit.place(x=50, y=80, width=100, height=50)

def open_income_goal():
    def set_goal_income():
        global income_goal_value
        income_value = income_money_entry.get()
        # 可在這裡進行其他操作或儲存值
        income_goal_value = income_value  # 將值存儲到全局變數中
        selected_income_goal_label.config(text=income_goal_value)  # 更新主要介面的標籤
        income_goal.destroy()
    income_goal = Tk.Toplevel(root)
    income_goal.title("設定儲蓄目標")
    income_money_entry = Tk.Entry(income_goal, width=22)
    income_money_entry.place(x=20, y=50)
    button_income_goal = Tk.Button(income_goal, text="設定", command=set_goal_income, font=("Arial", 12), bg="white", fg="black", padx=10, pady=5, relief="raised", bd=2)
    button_income_goal.pack()
    button_income_goal.place(x=50, y=80, width=100, height=50)



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
bg_image = Image.open("使用者驗證介面2.jpg")  # 替換為你的背景圖片檔案名稱或路徑
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = Tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# 使用者名稱標籤和輸入框
title = Tk.Label(root, text="個人財務管理系統", font=("Arial", 44, "bold"), fg="black",bg="white")
title.pack(pady=20)

# 使用者名稱標籤和輸入框
label_username = Tk.Label(root, text="使用者名稱", font=("Arial", 16), fg="black",bg="white")
label_username.pack(pady=10)
entry_username = Tk.Entry(root, font=("Arial", 14))
entry_username.pack(pady=10)

# 密碼標籤和輸入框
label_password = Tk.Label(root, text="密碼", font=("Arial", 16), fg="black",bg="white")
label_password.pack(pady=10)
entry_password = Tk.Entry(root, show="*", font=("Arial", 14))  # 以星號顯示密碼
entry_password.pack(pady=10)

# 登入按鈕
login_button = Tk.Button(root, text="登入", command=check_login, font=("Arial", 18), bg="#4CAF50", fg="white", padx=15, pady=8)
login_button.pack(pady=10)

gif_path = "shuba-duck.gif"
gif_image = Image.open(gif_path)

# 定义所需的宽度和高度
new_width = 860  # 请根据您需要的宽度设置具体数值
new_height = 400  # 请根据您需要的高度设置具体数值

# 分解GIF图像为帧并调整尺寸
frames = []
for frame in range(0, gif_image.n_frames):
    gif_image.seek(frame)
    frame_image = gif_image.copy().convert("RGBA")

    # 调整每一帧的大小
    resized_frame = frame_image.resize((new_width, new_height), Image.BICUBIC)

    frames.append(resized_frame)

# 将帧转换为Tkinter可用的格式
tk_frames = [ImageTk.PhotoImage(frame) for frame in frames]

# 创建一个标签部件来显示动画GIF
gif_label = Tk.Label(root)
gif_label.pack()

# 定义显示动画的函数
def animate(frame):
    gif_label.configure(image=tk_frames[frame])
    root.after(100, animate, (frame + 1) % len(tk_frames))  
    
# 开始动画
animate(0)


root.after(0, run_once)

# 啟動主迴圈
root.mainloop()

