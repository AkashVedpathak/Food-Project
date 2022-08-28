class  Food_items:
    
    def __init__(self,food_id,food_name,quantity_food,price_food,discount_food,stock_food):
        self.food_id=food_id
        self.food_name=food_name
        self.quantity_food=quantity_food
        self.price_food=price_food
        self.discount_food=discount_food
        self.stock_food=stock_food

    def __str__(self):
        return f" Food ID: {self.food_id} \nFood Name : {self.food_name} \nFood Quantity :{self.quantity_food} \nFood Price {self.price_food} \nFood Discount {self.discount_food} \nFood Stock {self.stock_food}"
    
    def set_food_id(self,food_id):
        self.food_id=food_id

    def get_food_id(self):
        return self.food_id

    def set_food_name(self,food_name):
        self.food_name=food_name
        
    def get_food_name(self):
        return self.food_name
    
    def set_quantity_food(self,quantity_food):
        self.quantity_food=quantity_food

    def get_quantity_food(self):
        return self.quantity_food

    def set_price_food(self,price_food):
        self.price_food=price_food

    def get_price_food(self):
        return self.price_food
    
    def set_discount_food(self,discount_food):
        self.discount_food=discount_food

    def get_discount_food(self):
        return self.discount_food

    def set_stock_food(self,stock_food):
        self.stock_food=stock_food

    def get_stock_food(self):
        return self.stock_food

