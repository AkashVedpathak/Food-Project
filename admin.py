from food_item import Food_items
from User import User_register

class Admin_class:

    def __init__(self,full_name,email_id,password): 
        self.full_name=full_name
        self.email_id=email_id
        self.password=password
   
    def __str__(self):
        return f"\nFull Name :{self.full_name} \nEmail ID: {self.email_id} \n Password :{self.password}"
   
    def set_full_name(self,full_name):
        self.full_name=full_name

    def get_full_name(self):
        return self.full_name
    
    def set_email_id(self,email_id):
        self.email_id=email_id

    def get_email_id(self):
        return self.email_id

    def set_password(self,password):
        self.password=password

    def get_password(self):
        return self.password

# Admin functionalities
class Admin_functionalities:
    register_list=[] 
    food_ID=3  
    food_list=[]

    def admin_register(self): 
        full_name =input("Enter Your Full Name : ")
        email_id=input("Enter Your Email ID : ")
        password=input("Enter Your Password : ")
        admin_obj=Admin_class(full_name,email_id,password)
        self.register_list.append(admin_obj) 
        print("\n Admin Register Succesful ! \n")
    
    def admin_login(self):
        email_id=input("Enter Your Email : ")
        password=input("Enter Your password : ")
        for i in self.register_list:
            if i.email_id == email_id and i.password == password:
                print("\n Admin Login Sucessful !\n")
                return True       
        else:
            print("\nPlease Enter Valid Email ID or Password \n")
            return False
 
    def add_food(self):
                food_name=input("Enter the Food Name : ")
                quantity_food=input("Enter the Quantity of food : ")
                price_food=(input("Enter the price of Food : "))
                discount_food=(input("Enter Discount Amount in Rs : "))
                stock_food=(input("Amount left in stock in the restaurant : "))
                self.food_ID=self.food_ID+1
                food_id=self.food_ID
                food=Food_items(food_id,food_name,quantity_food,price_food,discount_food,stock_food)
                new_food=f"{food_name} ({quantity_food}) [INR: {price_food}] [Discount amount : {discount_food}]"
                User_register.menu[food_id]=new_food
                self.food_list.append(food)
                print()
                print("\n Food has been added sucessfully \n")

    def edit_food(self):
        edit_input=int(input("Enter Food Id For Edit Food Items :"))
        print()
        for food in self.food_list:
            if edit_input == food.get_food_id():
                    food_name=input("Enter Food Name : ")
                    quantity_food=input("Enter Quantity of food : ")
                    price_food=(input("Enter the price of Food : "))
                    discount_food=(input("Enter Discount Amount in Only Rs : "))
                    stock_food=(input("Amount left in stock in the restaurant : "))
                    food.set_food_name(food_name)
                    food.set_quantity_food(quantity_food)
                    food.set_price_food(price_food)
                    food.set_discount_food(discount_food)
                    food.set_stock_food(stock_food) 
                    print("Food Edited sucessfullly !") 
                    break                  
        else:
            print("Food is Not Listed ")        

    def view_food(self):
        if self.food_list:
            for i in self.food_list:
                print(i)
                print()           
        else:
            print("\n No food items \n")

    def delete_food(self):
        input_delete=int(input("Enter food Id to Delete the particular food : "))
        print()
        for food in self.food_list:
            if input_delete == food.get_food_id():
                self.food_list.remove(food)
                print("Food Deleted sucessfully ! \n")
                break
        else:
            print("\n Food Id Not Found \n")


