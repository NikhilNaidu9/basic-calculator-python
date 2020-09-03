# Define
class Calculator:

  fnum = 0
  snum = 0 

  #TODO: Welcome the user
  # Define 
  def greet_user(self):
    print('Welcome to the most greatest calculator ever') 
    self.user_input()
 

  #TODO: Inputs from the user
  def user_input(self):
    print('Please input two numbers')
    self.fnum = float(input('Enter first number: '))
    self.snum = float(input('Enter second number: '))
    self.user_choice()

  #TODO: Taking user's choice for operations
  def user_choice(self):
    print('Please choose the operation you want to do with the number')
    
    operation = input('Operations : \n+ = Addition \n- = Subtraction \n* = Multiplication \n/ = Division \n% = Modulus \n^ = exponential \navr = average \n')
    
    if operation == '+':
      print('Addition')
      self.addition(self.fnum, self.snum)
    elif operation == '-':
      print('Subtraction')
      self.subtraction(self.fnum, self.snum)
    elif operation == '*':
      print('Multiplication')
      self.multiplication(self.fnum, self.snum)
    elif operation == '/':
      print('Division')
      self.division(self.fnum, self.snum)
    elif operation == '%':
      print('Modulus')
      self.modulus(self.fnum, self.snum)
    elif operation == '^':
      print('Exponential')
      self.exponential(self.fnum, self.snum)
    elif operation == 'avr':
      print('Average')
      self.average(self.fnum, self.snum)
    else:
      print('Please choose a correct input')


  #TODO: Addition of numbers
  def addition(self, first_number, second_number):
    ans = first_number + second_number
    print(ans)


  #TODO: Subtraction of numbers
  def subtraction(self, first_number, second_number):
    ans = first_number - second_number
    print(ans)


  #TODO: Multiplication of numbers
  def multiplication(self, first_number, second_number):
    ans = first_number * second_number
    print(ans)


  #TODO: Division of numbers
  def division(self, first_number, second_number):
    ans = first_number / second_number
    print(ans)


  #TODO: Modulus of numbers
  def modulus(self, first_number, second_number):
    ans = first_number % second_number
    print(ans)


  #TODO: Power of numbers
  def exponential(self, base, raise_to):
    ans = base ** raise_to
    print(ans)


  #TODO: Average of numbers
  def average(self, first_number, second_number):
    ans = first_number + second_number / 2
    print(ans) 


# Calling a class means making an object
calc = Calculator() # reference_variable = ClassName() or Class constructor
calc.greet_user() # Calling the entry point
