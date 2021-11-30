
class Product:
    product_count = 0

    def __init__(self, name, price, category,store):
        self.name = name
        self.price = price
        self.category = category
        store.add_product(name)
        Product.product_count += 1
        
        
        

    def update_price(self,percent_change, is_increased):
        if is_increased == True:
            self.price += round( self.price * percent_change, 2)
        elif is_increased == False:
            self.price -= round(self.price * percent_change, 2)
        return self
        
    def print_info(self):
        print(self.name, self.price, self.category)

    def __delete__(self):
            Product.product_count -= 1
            self.name=""
            self.price = 0
            self.category = "None"
            

    @classmethod
    def count(cls):
        print(cls.product_count)