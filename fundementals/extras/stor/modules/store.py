

class Store:

    def __init__(self, store_name ):
        self.store_name = store_name
        self.product_list = []

    def add_product(self, name ):
        self.product_list.append(name)
        

    def sell_product(self, product_name):
        for i in range(len(self.product_list)):
            if self.product_list[i] == product_name.name:
                del self.product_list[i]
                product_name.__delete__()

    def inflation(self, percent_increased, product):
        product.update_price(percent_increased, True)

    def set_clearance(self, percent_decreased, product):
        product.update_price(percent_decreased, False)


