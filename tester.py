from random import randint
import time

from tkinter import *
from tkinter import messagebox
from tkinter import ttk


#Изображения================================================
#Переменные================================================
bg_general = 'gray100' #общий фон

#пример
action = '*'
first_number = 0
second_number = 0
answer = 0
txt_example = (f'{first_number} {action} {second_number}')

#Количество ответов
right_answer = -1
number_right_answer = 150
txt_right_answer = (f'Правильных ответов: {right_answer}/{number_right_answer}')
#Ошибки
wrong_answer = 0
number_wrong_answer = 3
txt_wrong_answer = (f'Ошибок: {wrong_answer}/{number_wrong_answer}')


#Окно=======================================================
root_maths = Tk()
root_maths.resizable(False, False)
root_maths.title('Математика')
#root_maths.iconphoto(False, PhotoImage(file='C:/users/Дмитрий/Google Диск/programs/python/Maths/lib/ico_mini.png'))
root_maths.geometry(f'{400}x{400}+{200}+{200}')
root_maths.config(bg = bg_general)


#Команды===================================================
def place_menu():
	frame_menu.pack()

def forget_menu():
	frame_menu.pack_forget()

def place_game():
	lbl_example.pack(expand = True)
	lbl_timer.pack(side = BOTTOM)
	btn_exit_menu.place(relx = 0.78, rely = 0.835)
	
	frame_stat.place(relx = 0, rely = 0)
	frame_btn_game.pack(side = BOTTOM, pady = 10)
	
def forget_game():
	lbl_example.pack_forget()
	lbl_timer.pack_forget()
	btn_exit_menu.place_forget()
	frame_stat.place_forget()
	frame_btn_game.pack_forget()

def button_menu():
	btn_menu.pack_forget()
	place_menu()

def new_stat():
	global wrong_answer, right_answer, txt_right_answer, txt_wrong_answer
	forget_game()

	right_answer = -1
	wrong_answer = 0

	txt_right_answer = (f'Правильных ответов: {right_answer}/{number_right_answer}')
	lbl_right_answer.config(text = txt_right_answer)

	txt_wrong_answer = (f'Ошибок: {wrong_answer}/{number_wrong_answer}')
	lbl_wrong_answer.config(text = txt_wrong_answer)

def game():
	global txt_example, first_number,second_number, answer, right_answer, txt_right_answer, wrong_answer
	forget_menu()
	place_game()
	
	right_answer +=1
	txt_right_answer = (f'Правильных ответов: {right_answer}/{number_right_answer}')
	lbl_right_answer.config(text = txt_right_answer)

	if (right_answer == number_right_answer): #Победа
		btn_menu.config(text = 'Вы выйграли!')
		btn_menu.pack(fill = BOTH, expand = True)
		new_stat()

	if(action == '*'):
		first_number = randint(1,10)
		second_number = randint(1,10)
		answer = first_number * second_number
			
	elif (action == '/'):
		first_number = randint(1,10)
		second_number = randint(1,10)

		answer = first_number * second_number
		first_number = answer
		answer = int(first_number / second_number)
	
	elif (action == '+'):
		first_number = randint(1,100)
		second_number = randint(1,100)

		answer = first_number + second_number

	else:
		first_number = randint (1,100)
		second_number = randint (1,100)
		answer = first_number + second_number

		first_number = answer
		answer = first_number - second_number

	txt_example = (f'{first_number} {action} {second_number}')
	lbl_example.config(text = txt_example)

	button_answer()

def lose():
	global wrong_answer, txt_wrong_answer, right_answer
	wrong_answer += 1

	txt_wrong_answer = (f'Ошибок: {wrong_answer}/{number_wrong_answer}')
	lbl_wrong_answer.config(text = txt_wrong_answer)

	lbl_timer.config(bg = 'darkred')

	if (wrong_answer == number_wrong_answer):
		btn_menu.config(text = 'Вы проиграли')
		btn_menu.pack(fill = BOTH, expand = True)
		new_stat()

def exit_menu():
	forget_game()
	place_menu()
	new_stat()

def factor():
	global action
	action = '*'
	game()

def divide():
	global action
	action = '/'
	game()

def plus():
	global action
	action = '+'
	game()

def minus():
	global action
	action = '-'
	game()

def button_answer():
	i = answer + 2
	o = answer - 2

	y = 0
	x = randint(1,3)
	if (x == 1):
		btn_game1.config(text = answer, command = game)  #РАДМИИИИИР ВОТ СДЕСЬ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		y = randint(2,3)
		if (y == 2):
			btn_game2.config(text = i, command = lose)
			btn_game3.config(text = o, command = lose)
		else:
			btn_game2.config(text = o, command = lose)
			btn_game3.config(text = i, command = lose)
	elif (x == 2):
		btn_game2.config(text = answer, command = game)
		y = randint(3,4)
		if (y == 3):
			btn_game1.config(text = i, command = lose)
			btn_game3.config(text = o, command = lose)
		else:
			btn_game1.config(text = o, command = lose)
			btn_game3.config(text = i, command = lose)
	else:
		btn_game3.config(text = answer, command = game)
		y = randint(1,2)
		if (y == 1):
			btn_game1.config(text = i, command = lose)
			btn_game2.config(text = o, command = lose)
		else:
			btn_game1.config(text = o, command = lose)
			btn_game2.config(text = i, command = lose)

#Приложение================================================
#Меню----------------------------------
#Фреймы------------
frame_menu = Frame(bg = bg_general)

#Лейблы------------
lbl_menu = Label(
	frame_menu,
	text = 'Выберите режим',
	font = 'Arial 20 bold',
	bg = bg_general)
lbl_menu.pack(pady = 20)
#Кнопки------------
btn_factor = Button(
	frame_menu,
	text = 'Умножение',
	font = 'Arial 18 bold',
	bg = bg_general,
	width = 10,
	command = factor)
btn_factor.pack(pady = 5)

btn_divide = Button(
	frame_menu,
	text = 'Деление',
	font = 'Arial 18 bold',
	bg = bg_general,
	width = 10,
	command = divide)
btn_divide.pack(pady = 5)

btn_plus = Button(
	frame_menu,
	text = 'Сложение',
	font = 'Arial 18 bold',
	bg = bg_general,
	width = 10,
	command = plus)
btn_plus.pack(pady = 5)

btn_minus = Button(
	frame_menu,
	text = 'Вычетание',
	font = 'Arial 18 bold',
	bg = bg_general,
	width = 10,
	command = minus)
btn_minus.pack(pady = 5)


btn_setting = Button(
	frame_menu,
	text = 'Настройки',
	font = 'Arial 16 bold',
	bg = bg_general,
	width = 12,
	stat = 'disabled')
btn_setting.pack(pady = 20)


#Игра----------------------------------
#Фреймы------------
frame_stat = Frame(bg = bg_general)

frame_btn_game = Frame(bg = bg_general)

#Лейблы------------
lbl_example = Label(
	text = txt_example,
	bg = bg_general,
	font = 'Arial 26 bold')

lbl_right_answer = Label(
	frame_stat,
	text = txt_right_answer,
	bg = bg_general,
	font = 'Arial 9')
lbl_right_answer.pack()

lbl_wrong_answer = Label(
	frame_stat,
	text = txt_wrong_answer,
	bg = bg_general,
	font = 'Arial 9')
lbl_wrong_answer.pack(side = LEFT)

lbl_timer = Label(
	bg = 'green',
	width = 100)

#Кнопки------------
btn_game1 = Button(
	frame_btn_game,
	text = int(answer),
	font = 'Consolas 12 bold',
	bg = bg_general,
	height = 2,
	width = 5,
	command = game)
btn_game1.pack(side = LEFT)

btn_game2 = Button(
	frame_btn_game,
	text = int(answer),
	font = 'Consolas 12 bold',
	bg = bg_general,
	height = 2,
	width = 5)
btn_game2.pack(side = LEFT, padx = 5)

btn_game3 = Button(
	frame_btn_game,
	text = int(answer),
	font = 'Consolas 12 bold',
	bg = bg_general,
	height = 2,
	width = 5)
btn_game3.pack(side = LEFT)

btn_exit_menu = Button(
	text = 'Меню',
	font = 'Consolas 12 bold',
	bg = bg_general,
	width = 6,
	command = exit_menu)

btn_menu = Button(
	text = '',
	font = 'Aral 28 bold',
	bg = bg_general,
	border = 0,
	relief = 'flat',
	command = button_menu)

place_menu()

root_maths.mainloop()