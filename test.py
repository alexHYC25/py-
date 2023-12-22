
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