from time import sleep
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import time

def wait_10_second(event):
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
  button.bind("<Button-1>", wait_10_second)

  # 各種ウィジェットの設置
  button.pack()

  root.mainloop()