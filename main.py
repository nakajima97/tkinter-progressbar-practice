from time import sleep
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import time
import threading

def button_click(event):
  thread1 = threading.Thread(target=wait_10_second)
  thread1.start()

def wait_10_second():
  time.sleep(10)
  messagebox.showinfo("処理終了", "10秒経過しました。")
  return "break"

if __name__ == '__main__':
  # rootメインウィンドウの設定
  root = tk.Tk()
  root.title("tkinter application")
  root.geometry("200x100")

  # メインフレームの作成と設置
  frame = ttk.Frame(root)
  frame.pack(fill = tk.BOTH, padx=20,pady=10)

  # 各種ウィジェットの作成
  button = tk.Button(frame, text="ボタン")

  # bind
  button.bind("<Button-1>", button_click)

  # 各種ウィジェットの設置
  button.pack()

  root.mainloop()