import time
import threading
from tkinter import Tk, Button, Label, mainloop
from playsound import playsound
# To do:
# - Add a progress bar or a visible clock
# - Add customize work period (seconds) and relax period (seconds)
# - Add customize start time
# - Add start/stop/reset button
# - Add sound effects
# Need 2 more tabs:
# - Add customize playlist
# - Add customize list for exercises

start_time = time.time()
wait_time = 5
rep_count = -1


def state_change_sound():
    playsound('relax.mp3')


def clock():
    global rep_count, start_time, wait_time
    seconds = int(time.time() - start_time)
    if seconds < wait_time:
        string = 'Wait time: ' + str(wait_time - seconds).zfill(2)
    else:
        seconds = (seconds - wait_time) % 60
        string = 'Rep Count: ' + str(rep_count) + ' '
    seconds_str = str(int(seconds)).zfill(2) if int(
        seconds) <= 44 else str(int(seconds) - 45).zfill(2)
    t = threading.Thread(target=state_change_sound)
    if seconds_str == '00' and rep_count != -1:
        t.start()
    if 'time' not in string:
        string += ('Work ' +
                   seconds_str) if int(seconds) <= 44 else ('Relax ' + seconds_str)

    if seconds == 0:
        rep_count += 1
    if rep_count >= 10:
        string = 'Done for Today'
    lbl.config(text=string)
    lbl.after(1000, clock)


def reset_sound():
    playsound('bell.mp3')


def reset():
    global rep_count, start_time
    rep_count = 0
    start_time = time.time()
    t = threading.Thread(target=reset_sound)
    t.start()


root = Tk()
root.title('Clock')
reset_button = Button(root, font=('calibri', 20),
                      text='Reset', command=reset)
reset_button.grid(column=0, row=1)

lbl = Label(root, font=('calibri', 100, 'bold'),
            background='purple',
            foreground='white')

lbl.grid(column=0, row=0)
clock()

mainloop()
