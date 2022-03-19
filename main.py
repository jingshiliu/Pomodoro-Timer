import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
timer_on = False

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    check_mark_label['text'] = ''
    title_label['text'] = 'Timer'
    global reps
    reps = 0
    global timer_on
    timer_on = False

# ---------------------------- TIMER MECHANISM ------------------------------- #


# This func is to resolve the problem when user press start_button while timer is on
#
def timer_starter():
    global timer_on
    if timer_on:
        pass
    else:
        timer_on = True
        start_timer()


def start_timer():
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)
    global reps
    if reps % 8 == 0:
        check_mark_label['text'] = ''
    if reps % 2 == 0:
        check_mark_label['text'] += '✔'

    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text='Rest', foreground=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text='Break', fg=PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text='Study', fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    if math.floor(count / 60) < 10:
        minute = f'0{math.floor(count / 60)}'
    else:
        minute = math.floor(count / 60)
    if count % 60 < 10:
        second = f'0{count % 60}'
    else:
        second = count % 60

    time_text = f'{minute}:{second}'

    canvas.itemconfig(timer_text, text=time_text)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomodoro')
window.config(padx=50, pady=50, bg=YELLOW)
window.geometry('+490+230')
window.resizable(width=False, height=False)

canvas = Canvas(width=520, height=520, bg=YELLOW, highlightthickness=0)
# Note: must create an PhotoImage object that takes image then pass it in. Otherwise, won't work
tomato_image = PhotoImage(file='apple.png')
canvas.create_image(260, 260, image=tomato_image)

# *args unlimited positional arguments, **kwargs unlimited keyword arguments
timer_text = canvas.create_text(260, 280, text='00:00', fill=GREEN, font=(FONT_NAME, 60, 'bold'))

canvas.grid(row=1, column=1)

# Buttons

start_button = Button(command=timer_starter, text='Start', font=(FONT_NAME, 12, 'normal'), bg=YELLOW, highlightbackground=YELLOW)
start_button.grid(row=2, column=0)

reset_button = Button(command=reset_timer, text='Reset', font=(FONT_NAME, 12, 'normal'), bg=YELLOW, highlightbackground=YELLOW)
reset_button.grid(row=2, column=2)

# Check Mark

check_mark_label = Label(text='', fg=GREEN, bg=YELLOW)
check_mark_label.grid(row=3, column=1)

title_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, 'normal'))
title_label.grid(row=0, column=1)

window.mainloop()
