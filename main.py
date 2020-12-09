from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import Menu

window = Tk()
window.geometry('250x180')
window.title("Death Counter")

version = '0.1'
number = 0
limit = 100
bar_value = 0


def about():
    messagebox.showinfo('Автор', 'Разработал и написал SinYaYaSoVa\nСпециально для twitch.tv/KeKuX_TM\n\nTelegram: '
                                 'SinYaYa_SoVa\nGitHub: SinYaYa-SoVa')


def ver():
    global version
    messagebox.showinfo('О программе', 'Версия программы: ' + version + '\n\nПростая программа для подсчета смертей '
                                                                        'на стриме. ')


def addition():
    global number, limit, bar_value
    number += 1
    visual_counter.configure(text=str(number))
    bar_value += number / limit * 100
    bar['value'] = bar_value


def subtraction():
    global number, limit, bar_value
    if number == 0:
        messagebox.showwarning('Внимание!', 'Счетчик и так уже на нуле!')
    else:
        number -= 1
        visual_counter.configure(text=str(number))
        bar_value -= number/limit * 100
        bar['value'] = bar_value


def limiter():
    def set_lim():
        global limit
        limit = int(limit_input.get())
        bar.pack()

    def reset_lim():
        global limit
        limit = 0

    global limit

    limiter_window = Toplevel()
    limiter_window.geometry('250x150')
    limiter_window.title("Ограничитель")

    frame_limiter = Frame(limiter_window)
    frame_limiter.pack()

    frame_limiter_bot = Frame(limiter_window)
    frame_limiter_bot.pack()

    limit_label = Label(frame_limiter, text='Введите предел по смертям:')
    limit_label.pack(side=LEFT)
    limit_input = Entry(frame_limiter, width=10)
    limit_input.pack(side=LEFT)
    set_limit = Button(frame_limiter_bot, text='Установить', command=set_lim)
    set_limit.pack(side=LEFT)
    reset_limit = Button(frame_limiter_bot, text='Очистить', command=reset_lim)
    reset_limit.pack(side=LEFT)

    # limiter_window.iconbitmap('favicon.ico')


menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='Автор', command=about)
new_item.add_command(label='О программе', command=ver)
window.config(menu=menu)
menu.add_cascade(label='About', menu=new_item)

frame = Frame(window)
frame.pack()

bar_frame = Frame(window)
bar_frame.pack()

mid_frame = Frame(window)
mid_frame.pack()

bottom_frame = Frame(window)
bottom_frame.pack()

visual_counter = Label(frame, text=str(number), font=("Courier New", 50))
visual_counter.pack(side=LEFT)

minus_btn = Button(mid_frame, text="-", command=subtraction)
minus_btn.config(height=2, width=5)
minus_btn.pack(side=LEFT)

plus_btn = Button(mid_frame, text="+", command=addition)
plus_btn.config(height=2, width=5)
plus_btn.pack(side=LEFT)

set_limit_btn = Button(bottom_frame, text="Ограничитель", command=limiter)
set_limit_btn.pack(side=BOTTOM)

bar = Progressbar(bar_frame, length=200)

# window.iconbitmap('favicon.ico')
window.mainloop()
