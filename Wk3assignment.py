def calculate_discount():
    price = float(input('Enter the price of the item :'))
    discount = float(input("Enter the item discount in % :"))
    if discount >= 20:
        final_price = price-(price*discount/100)

    else:
        final_price = price

    return final_price, discount


final_price, discount = calculate_discount()
if discount >= 20:
    print(f"Discount applied! Final price: {final_price:.2f}")
else:
    print(f"No discount applied. Price remains: {final_price:.2f}")