class Restaurant: 
    menu = ["chicken nuget", "salmon", "lettuce"]
    reserved_tables = {
        "A": "",
        "B": "tamma",
        "C": "",
        "D": "",
        "E": ""

    }
    command_u = []
    @staticmethod  
    def add_dish( *dish):
        Restaurant.menu.extend(dish) #unpack the tuple when using it 
        print(Restaurant.menu)

    @staticmethod
    def reserved_table(table, name):  
        if table in Restaurant.reserved_tables:
            if Restaurant.reserved_tables[table] == "":  
                Restaurant.reserved_tables[table] = name  
                print(f"✅ Table {table} has been reserved for {name}.")  
            else:
                print(f"❌ Sorry, table {table} is already reserved by {Restaurant.reserved_tables[table]}.")
        else:
            print("⚠️ Invalid table selection.")

    @staticmethod
    def show_reserved_table():
        for x,y in Restaurant.reserved_tables.items():
            if y != "": 
                print(f"the table {x} is reserved by {y}")
            else:
                print("this table is not reserved XXX") 

    @staticmethod
    def show_menu():
        print(" , ".join(Restaurant.menu))
        
    @staticmethod
    def take_commands(*commands):
        for command in commands:
            if command not in Restaurant.menu:
                print("You command does not exist on the menu sir .")
            else : 
                Restaurant.command_u.append(command)
        # in python an empty list is considered as False 
        if Restaurant.command_u:        
            print("You commands sir are :")
            print(",".join(Restaurant.command_u))



    
print("les plats ajouté son :")   
Restaurant.add_dish("fish", "meat", "rise")

Restaurant.reserved_table("A", "Omar")
Restaurant.show_reserved_table()

print("------------")
Restaurant.show_menu()
print("-------------")

Restaurant.take_commands("lettuce", "meat", "chicken ")


#The solution is (better version): 

"""
class Restaurant:
    def __init__(self):
        self.menu_dishes = {}
        self.reserved_tables = []
        self.client_orders = []

    def add_dishes_to_menu(self, dish, price):
        self.menu_dishes[dish] = price

    def reserve_table(self, table_id):
        self.reserved_tables.append(table_id)

    def client_orders(self, table_id, order):
        order_info = {'table_id': table_id, 'order': order}
        self.client_orders.append(order_info)

    def display_menu_dishes(self):
        for dish, price in self.menu_dishes.items():
            print("{}: {}".format(dish, price))

    def display_reserved_tables(self):
        for table in self.reserved_tables:
            print("Table {}".format(table))

    def display_client_orders(self):
        for order in self.client_orders:
            print("Table {}: {}".format(order['table_id'], order['order']))

restaurant = Restaurant()

# Add dishes
restaurant.add_dishes_to_menu("Pizzas", 9.99)
restaurant.add_dishes_to_menu("Salad", 8)
restaurant.add_dishes_to_menu("Crepes", 19.99)
restaurant.add_dishes_to_menu("Sandwiches", 3.99)
restaurant.add_dishes_to_menu("Fish & Chips", 15)

# Reserve tables
restaurant.reserve_table(1)
restaurant.reserve_table(2)
restaurant.reserve_table(3)

# Take orders
restaurant.client_orders(1, "Pizzas")
restaurant.client_orders(1, "Crepes")
restaurant.client_orders(2, "Sandwiches")
restaurant.client_orders(2, "Crepes")

print("\nRestaurant dishes and their prices:")
restaurant.display_menu_dishes()

print("\nReserved tables in the restaurant:")
restaurant.display_reserved_tables()

print("\nDisplay client orders:")
restaurant.display_client_orders()

"""