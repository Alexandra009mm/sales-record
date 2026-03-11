 # This program allows a store administrator to register daily sales.
# It stores details about each sale (product name, unit price, quantity sold) and calculates the total sale value.
# The program displays a menu where the user can input new sales or view a summary of all sales at the end of the day.
# The summary includes a list of all sales with the total revenue for the day.

sale = []

def register():
    product = input("\n enter the product name: ")
    price = int(input("\n enter the unit price (without dots): ")) 

    quantity = int(input("\n enter the quantity: ")) 
    total = price * quantity
    

    sale_number = {
        "product": product,
        "price": price,
        "quantity": quantity, 
        "total": total
    }
    sale.append(sale_number)
    print(f"product sold {product} \n price {price} \n quantity {quantity} \n total sale {total}")

print("\n ---------MENU-----------\n 1. enter sale \n 2. exit and show summary")
op = input("\n What do you want to do?: \n ")
    
while op == "1":
    register()
    print("\n ---------MENU-----------\n 1. enter sale \n 2. exit and show summary")
    op = input("What do you want to do?: ")


print("\n purchase summary\n ")
for i in sale:
    print(i)


#this is the example you made
total_sale = sum(i['total'] for i in sale)
print(f"\n -------The total sales amount is: --------\n {total_sale} ")