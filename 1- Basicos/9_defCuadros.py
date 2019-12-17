import turtle

def main():
	window= turtle.Screen() #creo una ventana para la tortuga
	manuel = turtle.Turtle() # creo la tortuga
	number_square = int(input("Ingrese cantidad de cuadros \n"))	
	length = int(input("Ingrese largo del cuadro \n")) #pido datos del largo del cuadro
	make_square(manuel, length, number_square) #llamo a funcion que crea cuadrado pasando datos la tortuga y el largo del cuadro
	turtle.mainloop()

def make_square(t, l, n):#funcion que hace al cuadrado
	for e in range(n):
		for i in range(4): #ciclo que realiza cuatro veces las instrucciones siguientes
			t.forward(l)
			t.left(90)
		t.forward(l)




if __name__=='__main__':
	main()