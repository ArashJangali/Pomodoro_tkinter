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
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    label_Timer.config(text="Timer")
    label_check.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = 60 * WORK_MIN
    short_break_sec = 60 * SHORT_BREAK_MIN
    long_break_sec = 60 * LONG_BREAK_MIN

    if reps % 2 != 0:
        count_down(work_sec)
        label_Timer["fg"] = GREEN
        label_Timer["text"] = "Work"
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_Timer["fg"] = PINK
        label_Timer["text"] = "Break"
    elif reps == 8:
        count_down(long_break_sec)
        label_Timer["fg"] = RED
        label_Timer["text"] = "Break"
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✓"
        label_check.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 50, "bold"))
canvas.grid(column=1, row=2)



start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=3)

reset = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset.grid(column=2, row=3)

label_Timer = Label(text="Timer",bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40))
label_Timer.grid(column=1, row=0)
label_check = Label(fg=GREEN, bg=YELLOW)
label_check.grid(column=1, row=4)

window.mainloop()