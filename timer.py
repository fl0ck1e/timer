from tkinter import *
from tkinter.ttk import Combobox
from datetime import datetime

PAUSE = False
HOUR, MINUTE, SECOND = 0, 0, 0
action = None

def start():

    global HOUR, MINUTE, SECOND, PAUSE, action

    HOUR = int(combo_h.get())
    MINUTE = int(combo_m.get())
    SECOND = int(combo_s.get())
    SECOND +=1

    PAUSE = False
    start_button['state'] = 'disabled'
    pause_button['state'] = 'normal'
    resume_button['state'] = 'disabled'
    stop_button['state'] = 'normal'
    
    file = open('time.txt', 'w+')
    file.write('Запуск таймера в ' + datetime.now().strftime('%H:%M:%S'))
    file.close()

    if not action:
    	Counter()

def pause():

    global PAUSE, action

    PAUSE = True
    start_button['state'] = 'disabled'
    pause_button['state'] = 'disabled'
    resume_button['state'] = 'normal'

    file = open('time.txt', 'a+')
    file.write('\nПауза таймера в ' + datetime.now().strftime('%H:%M:%S'))
    file.close()

    if action:
    	root.after_cancel(action)
    	action = None

def resume():
	global PAUSE

	PAUSE = False
	start_button['state'] = 'disabled'
	pause_button['state'] = 'normal'
	resume_button['state'] = 'disabled'

	file = open('time.txt', 'a+')
	file.write('\nВозобновление таймера в ' + datetime.now().strftime('%H:%M:%S'))
	file.close()

	Counter()

def stop():

    global HOUR, MINUTE, SECOND, PAUSE, action

    PAUSE = True
    start_button['state'] = 'normal'
    pause_button['state'] = 'disabled'
    stop_button['state'] = 'disabled'
    Time['text'] = '00:00:00'

    file = open('time.txt', 'a+')
    file.write('\nОстновка таймера в ' + datetime.now().strftime('%H:%M:%S'))
    file.close()

    HOUR, MINUTE, SECOND = 0, 0, 0
    action= None

def Counter():

    global HOUR, MINUTE, SECOND, PAUSE, action

    if HOUR == MINUTE == SECOND ==0:
    	PAUSE = True

    if PAUSE is False:
    	if SECOND == 0:
    		if SECOND == MINUTE == 0:
    			HOUR -= 1
    			MINUTE = 60
    			SECOND = 60
    		MINUTE -= 1
    		SECOND = 60
    	SECOND -=1

    	Time.config(text='{}:{}:{}'.format(str(HOUR).zfill(2), str(MINUTE).zfill(2), str(SECOND).zfill(2)))
    	action = root.after(1000, Counter)


root = Tk()
root.title('Таймер')

width, height = 500, 300
pos_x = root.winfo_screenwidth() // 2 - width // 2
pos_y = root.winfo_screenheight() // 2 - height // 2

root.geometry('{}x{}+{}+{}'.format(width, height, pos_x, pos_y))

start_button = Button(root, text='Начать', font=("Arial", 16), fg='black', width=8, command=start)
start_button.place(x=0, y=80)

pause_button = Button(root, text='Пауза', font=("Arial", 16), fg='black', width=8, state='disabled', command=pause)
pause_button.place(x=100, y=80)

resume_button = Button(root, text='Возобновить', font=("Arial", 16), fg='black', width=10, state='disabled', command=resume)
resume_button.place(x=200, y=80)

stop_button = Button(root, text='Стоп', font=("Arial", 16), fg='black', width=8, state='disabled', command=stop)
stop_button.place(x=330, y=80) 

combo_h = Combobox(root, state="readonly")
combo_h['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)  
combo_h.current(0)
combo_h.place(x=0, y=25)

combo_m = Combobox(root, state="readonly")
combo_m['values'] = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,
					31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60)
combo_m.current(0)
combo_m.place(x=150, y=25)

combo_s = Combobox(root, state="readonly")
combo_s['values'] = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,
					31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60)
combo_s.current(0)
combo_s.place(x=300, y=25)

lbl_h = Label(root, text = 'Часы')
lbl_h.place(x=0, y=0)

lbl_m = Label(root, text = 'Минуты')
lbl_m.place(x=150, y=0)

lbl_s = Label(root, text = 'Секунды')
lbl_s.place(x=300, y=0)

Time = Label(root, fg='Black', text='00:00:00', font=("Helvetica", 60))
Time.place(x=80, y=150)

root.mainloop()