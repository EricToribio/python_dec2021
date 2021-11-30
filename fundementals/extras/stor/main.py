from modules.product import Product

from modules.store import Store

bobs = Store("Bobs")

chicken_wing = Product("Chicken Wing", 3.99, "meat", bobs)

burgers = Product("Burger", 5.99, "meat", bobs)

lettuce = Product("Lettuce", 1.99, "vegetable", bobs)
chicken_wing.print_info()
burgers.print_info()
print(bobs.product_list)
bobs.sell_product(lettuce)
print(bobs.product_list)
bobs.inflation(.25, chicken_wing)
bobs.set_clearance(.5, burgers)
chicken_wing.print_info()
burgers.print_info()



