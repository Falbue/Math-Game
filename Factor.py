from random import randint
import time

from tkinter import *
from tkinter import messagebox
from tkinter import ttk


#переменные-----
corX_root_maths = 400
corY_root_maths = 400
corX_root_maths_place = 200
corY_root_maths_place = 200

clr_bg = '#effbe3'

x = 0 # 
y = 0 # пример
z = 0 #

txt_quest = ' * '
quest_granMin = 3
quest_granMax = 9

txt_win = 'Тест сдан' #Текст выйгрыша

btn_1 = 1 #
btn_2 = 2 # кнопки ответа
btn_3 = 3 #
o = 0

true = 0  #правильных ответов
false = 0 #ошибок
true_end = 150
false_end = 0


chisl = 0           #  
text_btn_false1 = 0 # числа на кнопках-ошибках
text_btn_false2 = 0 #

corX_menu = 0.25
corY_menu = 0.1
corY_menu_plus = 0.18

corX_human = 250
corY_human = 50


#таймер
seconds = 10	
SQR_seconds = 32
factor_timerX = (corX_root_maths / seconds)
factor_after = int(512)

tick = 0
timerX = 0
i = 0

txt_diff = 'Легко'
diff_gran = 3
diff = 0




#команды;
def difficute(): #Трудность
	global txt_diff, true_end, false_end, clr_bg

	if (txt_diff == 'Легко'):
		txt_diff = 'Трудно'
		btn_diff.config(text = txt_diff)
		root_maths.config(bg = "#f8eded")
		clr_bg = "#f8eded"
		color_difficute()

	elif (txt_diff == 'Трудно'):
		txt_diff = 'Легко'
		btn_diff.config(text = txt_diff)
		true_end = 150
		root_maths.config(bg = "#effbe3")
		clr_bg = "#effbe3"
		color_difficute()

	setting_timer()
	stat_new()

def color_difficute():
	string_menu.config(bg = clr_bg)

	btn_factor.config(bg = clr_bg)
	btn_divide.config(bg = clr_bg)

	lbl_diff.config(bg = clr_bg)
	btn_diff.config(bg = clr_bg)
	scl_setting_timer.config(bg = clr_bg)

	btn_exit_menu.config(bg = clr_bg)
	
	string_quest.config(bg = clr_bg)
	string_true.config(bg = clr_bg)
	string_false.config(bg = clr_bg)
	lbl_timer.config(bg = clr_bg)
	lbl_timer.config(bg = clr_bg)

	btn_new.config(bg = clr_bg)

def place_menu(): #установка меню
	string_menu.place(relx = corX_menu, rely= corY_menu)

	btn_factor.place(relx = corX_menu, rely= corY_menu + corY_menu_plus*1)
	btn_divide.place(relx = corX_menu, rely= corY_menu + corY_menu_plus*2)

	lbl_diff.place(relx = corX_menu, rely = corY_menu + corY_menu_plus*3)
	btn_diff.place(relx = corX_menu+0.28, rely = corY_menu + corY_menu_plus*3- 0.005)

	if (txt_diff == 'Трудно'):
		scl_setting_timer.place(relx = corX_menu, rely = corY_menu + corY_menu_plus*3.3)

def forget_menu(): #скрытие меню
	string_menu.place_forget()

	btn_factor.place_forget()
	btn_divide.place_forget()

	lbl_diff.place_forget()
	btn_diff.place_forget()

	scl_setting_timer.place_forget()

def place_game(): #установка игры
	forget_menu()

	lose_button.place_forget()

	btn_exit_menu.place(relx = 0.75, rely = 0.87)
	
	string_quest.place(relx = 0.4, rely= 0.3,)
	string_true.place(relx = 0.01, rely = 0.05)
	string_false.place(relx = 0.01, rely = 0.090)
	lbl_timer.place(x = 0, y = 380)
	lbl_timer.config(bg = 'green')

	btn_new.grid(padx = 50)
	btn_answer.grid(padx = 2,pady = 300,row = 1,column = btn_1)
	btn_false1.grid(padx = 2,row = 1,column = btn_2)
	btn_false2.grid(padx = 2,row =1 ,column = btn_3)

def forget_game(): #скрытие всех виджетов
	btn_exit_menu.place_forget()

	string_quest.place_forget()
	string_true.place_forget()
	string_false.place_forget()
	lbl_timer.place_forget()

	btn_new.grid_forget()

	btn_answer.grid_forget()
	btn_false1.grid_forget()
	btn_false2.grid_forget()

def exti_menu(): #выход в меню
	btn_exit_menu.config(font = 'Arial 8 bold')
	stat_new()
	forget_game()
	place_menu()
	string_win.place_forget()
	after_cancel = 1
	if(txt_diff == 'Трудно'):
		root_maths.after_cancel(tick)


def stat_new():#обновление статистики
	global true
	global false
	true = 0
	false = 0

	string_true.config(text = 'Правильных ответов: ' + str(true) + '/' + str(true_end))
	string_false.config(text = 'Ошибок: ' + str(false) + "/3") #


def quest(): #программа игры
	global text_btn_false1,text_btn_false2, txt_quest, seconds
	
	x = randint(quest_granMin,quest_granMax)
	y = randint(quest_granMin,quest_granMax)
	z = x*y

	chisl = 0 

	if (txt_quest == ' * '):
		if ((x or y) == 5): chisl = 5
		else:
			chisl = randint(1,2)
			if (chisl == 1): chisl = x
			else: chisl = y

		string_quest.config(text = str(x) + str(txt_quest) + str(y))

		btn_answer.config(text = z)
		text_btn_false1 = z + chisl
		o = randint(1,2)
		if(o == 1): text_btn_false2 = z + chisl * 2
		elif(o == 2): text_btn_false2 = z - chisl
		


	elif (txt_quest == " / "):
		chisl = randint(1.,5)

		string_quest.config(text = str(z) + str(txt_quest) + str(y))
		
		btn_answer.config(text = x)
		text_btn_false1 = x + chisl
		text_btn_false2 = x - chisl

	btn_false1.config(text = text_btn_false1)
	btn_false2.config(text = text_btn_false2)

	btn_false_normal()

def answer(): #ответ
	global true
	true +=1

	string_true.config(text = 'Правильных ответов: ' + str(true) + '/' + str(true_end))

	random_btn()
	btn_false_normal()
	quest()
	win()
	timer_answer()


def error(): #Ошибка
	global false

	timer_error()

	false +=1

	string_false.config(text = 'Ошибок: ' + str(false) + "/3")

	if (false ==3):
		lose()

def lose(): #проигрыш
	stat_new()
	forget_game()
	if(txt_diff == 'Трудно'):
		root_maths.after_cancel(tick)

	lose_button.place(x = 0,y = 0) 
def win(): #победа
	if(txt_diff == "Легко"):
		o = 150
	elif(txt_diff == "Трудно"):
		o = 50  
	if(true == o):
		forget_game()
		btn_exit_menu.config(font = 'Arial 20 bold')
		btn_exit_menu.place(relx = 0.25,rely = 0.8)
		string_win.place(relx = 0.3,rely = 0.3)
		if(o==50):
			root_maths.after_cancel(tick)

		if (txt_quest == ' * '):
			btn_factor.config(state = 'disabled')

		elif (txt_quest == ' / '):
			btn_divide.config(state = 'disabled')

def setting_timer():
	if (txt_diff == 'Трудно'):
		scl_setting_timer.place(relx = corX_menu, rely = corY_menu + corY_menu_plus*3.3)
	else:
		scl_setting_timer.place_forget()

def set_seconds():
	global seconds, true_end
	seconds = scl_setting_timeer.get()
	true_end = seconds*10

def watch(): #время таймера
	global timerX, i, tick, seconds

	seconds = 10
	i += 1

	lbl_timer.place(x = timerX, y =380)

	timerX += factor_timerX

	tick = root_maths.after(factor_after, watch)

	if(timerX >= corX_root_maths + factor_timerX):
		root_maths.after_cancel(tick)
		error()

def timer_answer(): #правильный ответ
	global timerX, time, i
	lbl_timer.config(bg = 'green') 

	timerX = 0
	if(i >= 1): 
		root_maths.after_cancel(tick)
	if(txt_diff == 'Трудно'):
		watch()
def timer_error(): lbl_timer.config(bg = 'darkred')


def random_btn(): #установка кнопок ответа
	btn_1 = randint(1,3)
	btn_answer.grid(pady = 300,row = 1,column = btn_1)

	if (btn_1==3):
		btn_2 = randint(1,2)
		btn_false1.grid(rowspan = 100,row = 1,column = btn_2)
		if (btn_2 == 1):
			btn_3 = 2
			btn_false2.grid(rowspan = 100, row =1 ,column = btn_3)
		else:
			btn_3 = 1
			btn_false2.grid(rowspan = 100, row =1 ,column = btn_3)

	elif (btn_1 == 2):
		btn_2 = randint(1,3)
		if (btn_2 == 2):
			btn_2 = 3
			btn_false1.grid(rowspan = 100,row = 1,column = btn_2)
			btn_3 = 1
			btn_false2.grid(rowspan = 100, row =1 ,column = btn_3)
		else:
			btn_2 = 1
			btn_false1.grid(rowspan = 100,row = 1,column = btn_2)
			btn_3 = 3
			btn_false2.grid(rowspan = 100, row =1 ,column = btn_3)

	else:
		btn_2 = randint(2,3)
		btn_false1.grid(rowspan = 100,row = 1,column = btn_2)
		if (btn_2 == 2):
			btn_3 = 3
			btn_false2.grid(rowspan = 100, row =1 ,column = btn_3)
		else:
			btn_3 = 2
			btn_false2.grid(rowspan = 100, row =1 ,column = btn_3)

def btn_false1_error():
	error()
	btn_false1.config(state = 'disabled', bg = 'darkred')
def btn_false2_error():
	error()
	btn_false2.config(state = 'disabled', bg = 'darkred')
def btn_false_normal():
	btn_false1.config(state = 'normal', bg = '#F0F0F0')
	btn_false2.config(state = 'normal', bg = '#F0F0F0')


def factor():
	global txt_quest
	txt_quest = ' * '
	place_game()
	quest() 

def divide():
	global txt_quest
	txt_quest = ' / '
	place_game()
	quest()


#Окно===============================================================
root_maths = Tk()
root_maths.resizable(False, False)
root_maths.title('Математика')
#root_maths.iconphoto(False, PhotoImage(file='C:/users/Дмитрий/Google Диск/programs/python/Maths/lib/ico_mini.png'))
root_maths.geometry(f'{corX_root_maths}x{corY_root_maths}+{corX_root_maths_place}+{corY_root_maths_place}')
root_maths.config(bg = "#effbe3")


#МЕНЮ================================================================
#строки-----
string_menu = Label(text = 'Выберите режим:',font = 'Arial 16 bold', height = 1)
string_menu.place(relx = corX_menu, rely= corY_menu)

#кнопки-----
btn_exit_menu = Button(
	text = 'выйти в меню',
	font = 'Arial 8 bold',
	command = exti_menu)

btn_factor = Button(
	text = 'Умножение',
	font = 'Arial 20 bold',
	border = 3,
	width = 10,
	command = factor) 
btn_factor.place(relx = corX_menu, rely = corY_menu + corY_menu_plus*1) #expand кидает на центр контейнера, fill заполняет куда надо

btn_divide = Button(
	text = 'Недоступно',
	font = 'Arial 20 bold',
	border = 3,
	width = 10,
	state = 'disabled',
	command = divide)
btn_divide.place(relx = corX_menu, rely = corY_menu + corY_menu_plus*2)


lbl_diff = Label(text = 'Cложность:', font = 'Arial 12 bold')
lbl_diff.place(relx = corX_menu, rely = corY_menu + corY_menu_plus*3)

btn_diff = Button(
	text = txt_diff,
	font = 'Arial 12 bold underline',
	border = 0,
	command = difficute)
btn_diff.place(relx = corX_menu+0.28, rely = corY_menu + corY_menu_plus*3- 0.005)

scl_setting_timer = Scale(
	orient = "horizontal",
	font = 'Arial 10 bold',
	from_ = 2,
	to = 10,
	width = 17,
	length= 175,
	tickinterval=1,
	sliderlength = 30,
	bg = clr_bg,
	showvalue = 1,
	#command = set_seconds
	)
scl_setting_timer.set(5)
#seconds = scl_setting_timer.get()


#ИГРА==============================================================
#строки------------------------------------------------------------
string_quest = Label(
	text = 'none',
	font ='Arial 26 bold')

string_win = Label(text = txt_win, font = 'Arial 26 bold')

string_true = Label(text = 'Правильных ответов: ' + str(true) + '/' + str(true_end))

string_false = Label(text = 'Ошибок: ' + str(false) + '/3')

lbl_timer = Label(bg = 'green', width = 60)

#кнопки----------------------------------------------------------------
lose_button = Button(
	text = 'Вы проиграли',
	font = 'Arial 32 bold',
	relief = 'flat',
	border = 0,
	padx = 35,
	pady = 160,
	command = factor)

btn_answer = Button(
	text = '0',
	font = 'Consolas 12 bold',
	bg = '#F0F0F0',
	width = 5,
	height = 2,
	command = answer) #команда должна меняться
  #-column, -columnspan, -in, -ipadx, -ipady, -padx, -pady, -row, -rowspan, or -sticky

btn_false1 = Button(
	text = text_btn_false1,
	font = 'Consolas 12 bold',
	width = 5,
	height = 2,
	command = btn_false1_error)

btn_false2 = Button(
	text = text_btn_false2,
	font = 'Consolas 12 bold',
	width = 5,
	height = 2,
	command = btn_false2_error)

btn_new = Button( #скрытая кнопка
	relief = 'flat',
	text = '',
	border = 0)

color_difficute()
root_maths.mainloop()