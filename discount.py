def calculate_discount(price, discount_percent):
    """Calculates the final price after applying a discount if it is 20% or more."""
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    return price  


original_price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount)
print(f"The final price after discount is: {final_price:.2f}")
