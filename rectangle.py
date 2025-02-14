
class Rectangle :
    def __init__ (self, name, width, length):
        self.name = name
        self.width = width
        self.length = length
    
    def calc_surface(self):
        print("----------------")
        return f"the surface of {self.name} is {self.width * self.length} m²"
        print("----------------")

    def calc_perimeter(self):
        return f"The perimeter of {self.name} is {(self.width + self.length)*2} m"
    
    def display(self):
        print("----------------")
        print(f"this is {self.name} ")
        print(f"it has a length of : {self.length} m ")
        print(f"it has a width of : {self.width} m")


class  Polyedre(Rectangle):
    def __init__(self, name, width, length, height):
        super().__init__(name, width, length)
        self.height = height

    def volume(self):
        print(f"the volume of {self.name} is {self.height*self.width*self.length}m³" )
    def display(self):
        super().display()
        print(f"It has a height of {self.height} m")

     
polyedres = []
rectangles = []

def create():
    print("----------------")
    name = input("Enter the name of the rectangle ")
    width = int(input("Enter the width of the rectangle "))
    length = int(input("Enter the length of the rectangle "))
    rectangle = Rectangle(name, width, length)
    rectangles.append(rectangle)
    print("New rectangle created successfully ")
    print("----------------")
    print()

def create1():
    print("----------------")
    name = input("Enter the name of the polyedre ")
    width = int(input("Enter the width of the polyedre "))
    length = int(input("Enter the length of the polyedre "))
    height = int(input("Enter the height of the polyedre "))
    polyedre = Polyedre(name, width, length, height)
    polyedres.append(polyedre)
    print("New polyedre created successfully ")
    print("----------------")
    print()


def surface():
    rectangle = input ("Enter the rectangle name ")
    print("--------------")

    if not rectangles :
        print("there is no rectangle saved yet ")
    else :
        for element in rectangles :
            if element.name == rectangle :
                print(element.calc_surface())
            else :
                print("There is no a rectangle with such a name ")
    print("--------------")
    



def perimeter():
    rectangle = input ("Enter the rectangle name ")
    print("--------------")
    if not rectangles :
        print("there is no rectangle saved yet ")
    else :
        for element in rectangles :
            if element.name == rectangle :
                print(element.calc_perimeter())
            else :
                print("There is no a rectangle with such a name ")
    print("--------------")
    
def volume():
    polyedre = input ("Enter the polyedre name ")
    print("--------------")
    if not polyedres :
        print("there is no polyedre saved yet ")
    else :
        for element in polyedres :
            if element.name == polyedre :
                element.volume()
            else :
                print("There is no a rectangle with such a name ")
    print("--------------")
    

def info():
    if choice == 1 :
        print("-------------")
        if not rectangles :
            print("There is no rectangle saved yet ")
        else :
            for rectangle in rectangles : 
                rectangle.display()
        print("-------------")
    elif choice == 2 :
        print("-------------")
        if not polyedres :
            print("There is no rectangle saved yet ")
        else :
            for polyedre in polyedres : 
                polyedre.display()
        print("-------------")

def change_diameter():
    if choice == 1 :
        rectangle = input("Enter the rectangle name ")
        print("---------------")
        if not rectangles :
            print("There is no rectangle saved yet ")
        else : 
            n_width = int(input("Enter the new width : "))
            n_length = int(input("Enter the new length : "))

            for element in rectangles:
                if element.name == rectangle :
                    element.width = n_width
                    element.length = n_length
                    print("length and width changed successfully ")
                else :
                    print("There is no a rectangle with such a name ")
        print("---------------")
    elif choice == 2 :
        polyedre = input("Enter the polyedre name ")
        print("---------------")
        if not polyedres :
            print("There is no polyedre saved yet ")
        else : 
            n_width = int(input("Enter the new width : "))
            n_length = int(input("Enter the new length : "))
            n_height = int(input("Enter the new height : "))

            for element in polyedres:
                if element.name == polyedre :
                    element.width = n_width
                    element.length = n_length
                    element.height = n_height
                    print("height and width and length changed successfully ")
                else :
                    print("There is no a polyedre with such a name ")
        print("---------------")

def main_menu():
    print("1. Rectangle section ")
    print("2. Polyedre section ")
    print("3. Exit")

def menu1():
    print("1. Create a new rectangle ")
    print("2. calculate the surface ")
    print("3. calculate the perimeter ")
    print("4. display info ")    
    print("5. change rectangle diameter")
    print("6. Return ..")

def menu2():
    print("1. add a new polyedre ")
    print("2. calculate the volume of the polyedre ")
    print("3. display info ")
    print("4. change polyedre diameter")
    print("5. Return ..")


while True :
    print("Welcome in this shape system ")
    main_menu()
    try :
        choice = int(input("Enter a number between (1-2) : "))
    except Exception: 
        print("Error, please enter a valid number ")

    if choice == 1 :
        while True:
            print("------------------")
            print("Welcome in rectangle section ")
            menu1() 
            try :
                choice1 = int(input("Enter a number between (1-6) : "))
                
                if choice1 == 1 :
                    create()
                elif choice1 == 2 :
                    surface()
                elif choice1 == 3 :
                    perimeter()
                elif choice1 == 4 :
                    info()
                elif choice1 == 5 :
                    change_diameter()
                elif choice1 == 6 :
                    print("Return back")
                    break
                else :
                    print("Your number is out of range")
                    continue

            except ValueError : 
                print()
                print("Please enter a valid number ")
                print()

    elif choice == 2 :
        while True :
            print("-------------------")
            menu2()
            try :
                choice2 = int(input("Enter a number between (1-6) : "))
                    
                if choice2 == 1 :
                    create1()
                elif choice2 == 2 :
                    volume()
                elif choice2 == 3 :
                    info()
                elif choice2 == 4 :
                    change_diameter()
                elif choice2 == 5 :
                    print("Thanks for testing our program ")
                    break
                else :
                    print("Your number is out of range")

            except ValueError : 
                print()
                print("Please enter a valid number ")
                print()
    elif choice == 3:
        break
    else :
        print("Your number is out of the range ")
        
