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
    bg_image_index = Image.open("使用者驗證介面2.jpg")  # 替換為你的背景圖片檔案名稱或路徑
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
    label_income_num = Tk.Label(frame_labels_income, text=total_amount)
    label_income_num.pack(side=Tk.TOP)

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


    image_path = "歡迎使用個人記帳管理系統.jpg"  # 替換為您的圖片檔案路徑
    original_image = Image.open(image_path)
    resized_image = original_image.resize((300, 300))
    global_photo = ImageTk.PhotoImage(resized_image)

    



