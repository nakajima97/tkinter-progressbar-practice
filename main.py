from time import sleep
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import time
import threading

def button_click(event):
  thread1 = threading.Thread(target=wait_10_second)
  thread1.start()
  progressbar.start()

def wait_10_second():
  time.sleep(10)
  messagebox.showinfo("処理終了", "10秒経過しました。")
  progressbar.stop()
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
  progressbar = ttk.Progressbar(frame, maximum=100, mode="indeterminate")

  # bind
  button.bind("<Button-1>", button_click)

  # 各種ウィジェットの設置
  button.grid(row=0, column=0)
  progressbar.grid(row=1, column=0)

  root.mainloop()