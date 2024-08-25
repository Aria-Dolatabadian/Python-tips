from multiprocessing import *
import cv2
import numpy as np
from time import sleep
import pyautogui
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename as save_as
import shutil
import webbrowser

# Main function to record screen
def record_screen_v(queue):
    SCREEN_SIZE = tuple(pyautogui.size())
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    fps = 1.0
    out = None
    recording = True

    while recording:
        if queue.empty():
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            if out is None:
                out = cv2.VideoWriter("Output.avi", fourcc, fps, (SCREEN_SIZE))
            out.write(frame)
            sleep(1 / fps)
        else:
            command = queue.get()
            if command == "stop":
                recording = False

    if out is not None:
        out.release()
    cv2.destroyAllWindows()

# This function starts the recording
def rec(queue):
    while True:
        if not queue.empty():
            command = queue.get()
            if command == "start":
                record_screen_v(queue)
            elif command == "exit":
                break
        sleep(1)

# Function for releasing the recorded video
def main_l(queue):
    def rls():
        filename = save_as(defaultextension=".avi", filetypes=[("AVI files", "*.avi")])
        if filename:
            shutil.move("Output.avi", filename)
            p3.place(x=150, y=1000)
            messagebox.showinfo("File saved", "Your file has been saved")

    def ply():
        queue.put("start")
        p2.place(x=15, y=80)
        p1.place(x=150, y=1000)

    def stp():
        queue.put("stop")
        p1.place(x=15, y=80)
        p3.place(x=15, y=170)
        p2.place(x=150, y=1000)

    def ghb():
        try:
            webbrowser.open("https://github.com/abhineetraj1")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    t = Tk()
    t.title("Screen Recorder")
    t.geometry("320x280")
    t.resizable(0, 0)
    Label(t, background="pink", height=5, width=500).place(x=0, y=0)
    Label(t, background="pink", text="Screen Recorder", foreground="black", font=('arial', 19)).place(x=10, y=5)
    Label(t, background="white", height=30, width=500).place(x=0, y=50)

    p1 = Button(t, text="Start Recording", font=('arial', 15), command=ply, background="pink", foreground="black", activebackground="white", activeforeground="pink")
    p2 = Button(t, text="Stop Recording", font=('arial', 15), command=stp, background="pink", foreground="black", activebackground="white", activeforeground="pink")
    p3 = Button(t, text="Release Video", font=('arial', 15), command=rls, background="pink", foreground="black", activebackground="white", activeforeground="pink")

    Button(t, text="By Aria Dolatabadian", font=('arial', 10), command=ghb, background="pink", foreground="black", activebackground="white", activeforeground="black").place(x=10, y=230)
    p1.place(x=15, y=80)
    p2.place(x=1500, y=1000)
    t.mainloop()

if __name__ == '__main__':
    queue = Queue()
    t1 = Process(target=main_l, args=(queue,))
    t2 = Process(target=rec, args=(queue,))
    t1.start()
    t2.start()
    t1.join()
    queue.put("exit")
    t2.join()

