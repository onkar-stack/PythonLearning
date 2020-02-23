# in python everything is object
# class: blueprint of plan
# Object: pPysical existence of plan
# student

# name
# roll
# age
# Above mentionwd are attributes/properties   

# read 

#behavior is represented by method

# how to define class

#class classname:
	# document
	# variable:
		# instance variable (object level var)
		# static variable (class level var)
		# loacal variable (method level var)
	# menthod:
		# instance method
		# static method
		# class method
	# def __init__(self): constructor


	# if a fuction is declared inside a class it is called method.
	# if a fuction is declared outside a class it is called fuction.

	# reference variable




class student:
	"developeped by onkar"
	def __init__(self, name, rollnum, marks):
		self. name = name
		self.rollnum = rollnum
		self.marks = marks

	def result(self):
		if self.marks > 300:
			print("pass")
		else:
			print("fail")

s1 = student("onkar", 101, 500)
print(s1.name)
print(s1.rollnum)
print(s1.marks)
s1.result()