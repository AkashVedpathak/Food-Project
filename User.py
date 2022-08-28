class User:
    
    def __init__(self,full_name,phone_no,email_id,address,password):
        self.full_name=full_name
        self.phone_no=phone_no
        self.email_id=email_id
        self.address=address
        self.password=password

    def __str__(self):
        return f"Full Name :{self.full_name} \nPhone Number :{self.phone_no} \nEmail ID: {self.email_id} \nAddress :{self.address} \nPassword :{self.password}"
    
    def set_full_name(self,full_name):
        self.full_name=full_name

    def get_full_name(self):
        return self.full_name

    def set_phone_no(self,phone_no):
       self.phone_no=phone_no

    def get_phone_no(self):
        return self.phone_no
    
    def set_email_id(self,email_id):
        self.email_id=email_id

    def get_email_id(self):
        return self.email_id

    def set_address(self,address):
        self.address=address

    def get_address(self):
        return self.address

    def set_password(self,password):
        self.password=password

    def get_password(self):
        return self.password

# User functionalities        
class User_register:
    user_list=[] 
    orders=[]
    current_user_email=""
    menu={1:"Tandoori Chicken (4 pieces) [INR 240]" , 2:"Vegan Burger (1 Piece) [INR 320]" , 3:"Truffle Cake (500gm) [INR 900]"}
    
    def user_register_function(self):
        full_name =input("Enter Your Full Name : ")
        phone_no =int(input("Enter Your your Phone Number : "))
        email_id =input("Enter Your Email Address : ")
        address =input("Enter Your Address : ")
        password =input("Enter Your Password : ")
        admin_obj1=User(full_name,phone_no,email_id,address,password)
        self.user_list.append(admin_obj1)
        print("User Register succesfully !")
    
    def user_login_function(self):
        Email_id=input("Enter Your Email : ")
        password=input("Enter Your password : ")
        for i in self.user_list:
            if i.email_id == Email_id and i.password== password:
                print()
                print("User  Login Sucessfully ! \n")
                self.current_user_email=Email_id
                return True
        else:
            print("\n Please Enter Valid Email ID or Password ")
            return False
    
    def place_order(self):
            for Item in self.menu.items():
                print(Item)
                print()
            foodId=input("Enter the Food ID you want to order separated by comma:").split(",")
            print()
            orderlist =[]
            for id in foodId :
                if int(id) in self.menu.keys() :
                    orderlist.append(self.menu[int(id)])
                else :
                    print("Invalid Food Item ")
            if len(orderlist) > 0 :
                print("Current Order : \n")
                print(orderlist)
                inputTwo = int(input("\n 1. Confirm and place the Order \n 2. Exit \n"))
                print()
                if inputTwo == 1 : 
                    self.orders.append(orderlist)
                    print("Your order has been placed successfully \n!")  
                else : print("Order cancelled!!")
                
    def order_history(self):
        for j in self.orders :
            print()
            for k in j : 
                print(k)
            print()

    def update_profile(self):
        for i in self.user_list:
            if i.email_id==self.current_user_email:
                full_name =input("Enter Your Full Name : ")
                phone_no =int(input("Enter Your your Phone Number : "))
                email_id =input("Enter Your Email Address : ")
                address =input("Enter Your Address : ")
                password =input("Enter Your Password : ")
                 
                i.set_full_name(full_name)
                i.set_phone_no(phone_no)
                i.set_email_id(email_id)
                i.set_address(address)
                i.set_password(password)
                print("profile Updated Sucessfully !")
                break
        else:
            print("No Profile Found")    
    




