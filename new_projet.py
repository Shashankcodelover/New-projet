import random
from colorama import Fore, Style, init

class Overall:
    name = " "

    def calculator(self):
        print("You chose the calculator.")
        print("\nChoices: 1-Add, 2-Subtract, 3-Multiply, 4-Divide, 5-Remainder, 6-Floor division.")
        num = int(input())

        a = int(input("Enter the value for the 1st number: "))
        b = int(input("Enter the value for the 2nd number: "))

        if num == 1:
            print(f"\nThe result is: {a + b}\n")
        elif num == 2:
            print(f"\nThe result is: {a - b}\n")
        elif num == 3:
            print(f"\nThe result is: {a * b}\n")
        elif num == 4:
            if b != 0:
                print(f"\nThe result is: {a / b}\n")
            else:
                print("Error: Cannot divide by zero.")
        elif num == 5:
            print(f"\nThe result is: {a % b}\n")
        elif num == 6:
            if b != 0:
                print(f"\nThe result is: {a // b}\n")
            else:
                print("Error: Cannot divide by zero.")
        else:
            print("Invalid option.")

    def lcm(self):
        print("\nYou chose LCM calculation.")
        a = int(input("Enter the value for the 1st number: "))
        b = int(input("Enter the value for the 2nd number: "))

        greater = max(a, b)
        while True:
            if greater % a == 0 and greater % b == 0:
                print(f"\nThe LCM of {a} and {b} is {greater}.")
                break
            greater += 1

    def number_game(self):
        print("\nYou chose the number guessing game.")
        secret_number = random.randint(0, 50)
        attempts = 0

        while attempts < 10:
            guess = int(input("Guess the number (0-50):\n you have only 10 chanches  "))
            attempts += 1

            if guess == secret_number:
                print(Fore.GREEN + f"\nCongratulations! You guessed the number in {attempts} tries." + Style.RESET_ALL)
                break
            elif guess < secret_number:
               print(Fore.RED + f"{attempts}. Too low! Try again." + Style.RESET_ALL)
            else:
                print(Fore.RED + f"{attempts}. Too high! Try again." + Style.RESET_ALL)

        if attempts == 10:
            print(f"\nSorry, the correct number was {secret_number}.")

    def basic_python_operations(self):
        a, b = int(input("Enter the value for a: ")), int(input("Enter the value for b: "))
        print(f"Basic operations: a + b = {a + b}, b - a = {b - a}, a * b = {a * b}, b / a = {b / a:.2f}, a % b = {a % b}")

        # Swapping without a third variable
        a, b = a + b, a - b
        a -= b
        print(f"Swapped values: a = {a}, b = {b}")

        # String manipulations
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        print(f"\nHello {name}, your age is {age}.\n")

        sentence = input("Enter a sentence: ")
        print(f"\nUppercase: {sentence.upper()}\nLowercase: {sentence.lower()}\nReplaced spaces: {sentence.replace(' ', '_')}\nStripped: {sentence.strip()}")

        # More basic operations
        a, b = int(input("Enter the value for a: ")), int(input("Enter the value for b: "))
        print(f"\na == b: {a == b}\na != b: {a != b}\na >= b: {a >= b}\na <= b: {a <= b}")
        print(f"\nLogical checks:\na > 0 and b < 0: {a > 0 and b < 0}\na > 0 or b < 0: {a > 0 or b < 0}\nnot (a < 0): {not (a < 0)}")
        
        print('sh' in name, 'sh' not in name)

        a = int(input("checking either you are minor or adult \n Age: "))
        if a < 18:
                  print("You are a minor\n\n")
        else:
                  print("You are an adult\n\n")

        z = int(input(" checking some binary operation \n Enter value for z: "))
        y = int(input("\n Enter value for y: "))

        print(f"\nz & y={z & y}\n  //z | y\n {z | y} //~y\n {~y} // z << y\n{z << y} //z >> y\n {z >> y} //~z\n {~z} // {z ^ y}\n\n")

        lst = [23, "hello", True, [2, 2, 43, 8]]
        print(f" it is a list.and operation  \n\n   {lst} \n{lst[1]} \n{lst[3][2]}\n\n")

        lst.pop(0)
        print(lst)

        lst.append("hi")
        print(f"\n{lst}")

        lst.remove("hello")
        print(f"\n{lst}")

        lst.pop()
        lst.remove(True)
        print(f"\n{lst}")

        lst.insert(1, [12, 23, 54])
        print(f"\n{lst}")

        lst.clear()
        print(f"\n{lst}")

        lst = (2, 32, 1, 0, 78, 4)
        print(f"\n{lst}")

        z = sorted(lst)
        print(z)

        z.reverse()
        print(f"\n{z}")

        w = (12, 22, 87, 88)
        w1 = (33, 22, 23)

        d = {12, 23, 98, 4}
        d1 = {12, 23, 66, 88}

        print(f"\n it  is list   {w}")
        print(f"\n it is truple  {d}")

        w3 = w + w1
        d1.discard(1)

        print(f"\n{w}")
        print(f"\n{w1}")
        print(f"\n{w3}")
        print(f"\n it is truple operation   {d}")
        print(f"\n{d1}")
        print(f"\n{d | d1}")
        print(f"\n{d & d1}")
        print(f"\n{d ^ d1}")
        print(f"\n{d - d1}")

        a = {
        "arjun": "08/77",
        "sh": "23/23",
        8: 46,
        75: "sh"
    }

        print("it is dictionary  and its operation \n\n"+str(a))
        print(f"\n{type(a)}\n\n")
        print(f"\n\n{a.values()}\n\n")
        print(f"\n\n{a.keys()}\n\n")
          
        op = {
        "hello": "hi",
        "good": "morning",
        "goal": "night"
    }

        print(op)
        print(f"\n\n\n{op.values()} \n\n\n{op.keys()}\n\n\n{op.items()}\n\n")
        print(op["hello"])

        y = input("Enter the key to search: ")
        print(f"\n{op.get(y, 'not found')}\n\n")

        op["go"] = "bye"
        print(f"\n\n{op}\n\n")

        op["goal"] = "is good"
        print(f"\n\n {op} \n\n ")
              
        ops={"see you" : "bye"}
              
        op.update(ops)
        print(f"\n\n {op} \n\n ")

        age=int(input(" simple enquiry for ticket discount  \n\nenter the your age  "))
        if age<=18:
              print("\n\nyour ticket is half")
        elif age >=18 and age <=60:
              print("\n\n your ticket isfull ")
        else:
                   print("\n\nyour ticket is half")


    def for_funtion(self):
         a= str(input("give a sentence to check vowels or not :" ))
         for i in a:
              print(i)
#cheking the vowels      
              if i=='a' or i=='e'or i=='i' or i=='o' or i=='u':
                  print("\nit is vowels ")
              else:
                  print("\n it is constanent ")
          
         l=[12,32,23]
         dis={"sh":8,
         "pre":5,
         15:244}
         print(f"it is distionary {dis}  ")
         w=str(input("\n if u want to stop at pre enter s "))
         for index,num in enumerate(l):
             print(index," ",num)
     
#for loop with else      
         for key,value in dis.items():
             print(key, " " ,value)
     
             if key=="pre" and w=="s":
                   break
         else:
              print(" \nfull printed ")
# printing right angled triangle     
         j=int(input("\n printing right angled triangle   and how many nu of line it should print(n-1)   "))
         for i in range(j):
              print("*"*i)     
#using nested loop 
         for i in range(1):
              for j in range(1):
                        print("\nis done and it is nested loop \n")    

         l=[12,32,76,89]
         print(str(l)+"\nit is list and adding the num of this list \n")
         total=0
         for i in l:
              print(total)
              total+=i
         print(total)  

         dl=[]
         print(str(dl)+"\n here we are adding this to another list double the list of\n "+str(l))
         for i in l:
              dl.append(i*2)
         print(dl)
#addimg 2 list 
         l1=["sh","pr","as","ja"]
         l2=[8,5,30,16]
         l={}
         print(f"\n ee are adding 3 list to make 1 distonary \n{l1}=1st list\n{l2}=2nd list ")
         for i in range(len(l1)):
              l[l1[i]]=l2[i]
              print(l)
     
#list comprehition
         ll=[i for i in range(5)]
         print("\n we are doing list comprehition in formate \n dl=[expr for item incollection]\n //ll=[i for i in range(5)]\n"+str(ll)+
" ×3=")
#dl=[expr for item incollection]
         dl=[i*3 for i in ll]
         print(dl)
         print(str(2**3)+" it is power of  2**3 2 power 3 ")
#dictionary  comprehition
         print("\n we are doing dictionary comprehition in formate \n new_dict = {key_expression: value_expression for item in iterable if condition}\n //ll=[i for i in range(5)]\n")
         l=[1,2,3,4,5]
         dl={i*2:i**2 for i in l}
         print(dl)
         print("printing the dictionary who's population is >10 ")

         city_population = {
    "Bengaluru": 84,
    "Mysuru": 11,
    "Hubballi": 9,
    "Mangaluru": 5
}
         print(city_population)
         large_cities = {city: population for city, population in city_population.items() if population > 10}
         print(large_cities)
    
    def user_arthematic_operation_by_own(self):
         result = eval(input("enter the expretion "))
         print(result)
# Example input: 2 + 3 * 5
# Output: 17

         l = [int(num) for num in       input("enter the integer list ").split()]
         print(l,"   it is your list.  ")
# Example input: 10 20 30
# Output: [10, 20, 30]
             
    
    def call_function(self):
        init(autoreset=True)

        while True:
            print("\nSelect an option: 1-Calculator, 2-LCM, 3-Number game, 4-Basic Python operations,5-for funtions , 6-user_arthematic_operation_by_own. ,7--Exit")
            option = int(input())

            if option == 1:
                self.calculator()
            elif option == 2:
                self.lcm()
            elif option == 3:
                self.number_game()
            elif option == 4:
                self.basic_python_operations()
            elif option == 5:
                self.for_funtion()
            elif option == 6:
                self.user_arthematic_operation_by_own()    
            elif option == 7:
                print(Fore.GREEN + "Exiting the program. Goodbye!" + Style.RESET_ALL)
                break
            else:
                print(Fore.RED + "\nInvalid function selected." + Style.RESET_ALL)
                
                        
# Main function
ob = Overall()
ob.call_function()