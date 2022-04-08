from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
CHECK = "☑"
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    section_label.config(text="START")
    check_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps +=1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps == 8:
        section_label.config(text="BREAK", fg=RED)
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        section_label.config(text="BREAK", fg=PINK)
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)
        count_down(short_break_sec)
    else:
        section_label.config(text="WORK", fg=GREEN)
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    count_mins = math.floor(count / 60)
    count_seconds = count % 60

    if count_mins < 10:
        count_mins = f"0{count_mins}"

    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_mins}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "☑ "
        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
tomato = PhotoImage(file="tomato.png")
window.title("Pomodoro")
window.config(padx=20, pady=20, bg=YELLOW)
window.iconphoto(False, tomato)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=0)

start_button = Button(text="start", font=(FONT_NAME, 10, "bold"), command=start_timer)
start_button.grid(column=0, row = 1)

section_label = Label(text="START", font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
section_label.grid(column=1, row=1)

reset_button = Button(text="reset", font=(FONT_NAME, 10, "bold"), command=reset_timer)
reset_button.grid(column=2, row = 1)

check_label = Label(bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=2)

window.mainloop()