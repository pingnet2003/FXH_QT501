#倒计时
from turtle import *
import time
def drawGap():  #实现每一段数码管间隔分割5像素
	penup()
	fd(5)
def drawLine(line):	#画数码管
	pendown() if line else penup()
	fd(40)
	right(90)
def drawDigit(digit):
	drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)  
	#数码管（1）如digit为真，向前画40，并且旋转90度，否则不画，其中[2,3,4,5,6,8,9]不是数码管编号（数码管编号是drawLine(True)这行，第一行执行的是数码管(1))，而是需要显示的数字0-9
	drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False) #数码管（2）
	drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)    #数码管3）
	drawLine(True) if digit in [0,2,6,8] else drawLine(False) 			#数码管（4）
	left(90)  	#因为数码管4执行后，按照drawLine(draw)函数，会再执行完向右旋转90，而数码管（4）到数码管（5），不用旋转，因此需要反向旋转90度，确保直行画笔
	drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)  #数码管(5)
	drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)   #数码管(6)
	drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False) 		#数码管 (7)
	seth(0) #方向重置默认方向
	penup()   
	bk(40)   #回到原点
# '''#以2为例，输入2，分别位于数码管（1、3、4、6、7），则数码管（1）为真，画40并旋转90——>旋转后数码管（2）为假，不画，但是需要前进40，并旋转90
# ——>旋转90后，数码管（3）为真,则画40并旋转90，一直循环7次数码管，得到数字2'''
# '''#即显示2时，按照drawLine(True)，执行顺序，分别执行了第1、3、4、6、7行代码，对应数码管1、3、4、6、7'''
def drawDate(date):
	for i in range(10):
		i = 9 - i
		drawDigit(i) 
		hideturtle()
		time.sleep(1)
		clear() #画完数字后，清理，重画
def main():
	setup(800,700,100,100)
	penup()
	fd(-300)
	pensize(5)
	drawDate(1)
	hideturtle()
	done()
# main()
