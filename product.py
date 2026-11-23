
def product_details(product_id, name, quantity, price):
    return (
        "Product ID: " + str(product_id) + "\n"
        "Product Name: " + name + "\n"
        "Quantity: " + str(quantity) + "\n"
        "Price: Rs." + str(price)
    )


# Main program
result = product_details(101, "Laptop", 5, 45000)
print(result)


