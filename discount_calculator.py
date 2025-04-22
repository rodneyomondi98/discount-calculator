def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if discount_percent >= 20%.
    
    Args:
        price (float): The original price of the item
        discount_percent (float): The discount percentage
        
    Returns:
        float: The final price after discount (or original price if discount < 20%)
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    return price

def main():
    try:
        # Prompt user for input
        price = float(input("Enter the original price of the item (kshs): "))
        discount_percent = float(input("Enter the discount percentage: "))
        
        # Validate inputs
        if price < 0 or discount_percent < 0:
            print("Price and discount percentage cannot be negative.")
            return
            
        # Calculate final price
        final_price = calculate_discount(price, discount_percent)
        
        # Print result
        if discount_percent >= 20:
            print(f"Final price after {discount_percent}% discount: kshs {final_price:.2f}")
        else:
            print(f"No discount applied (discount < 20%). Final price: kshs {final_price:.2f}")
            
    except ValueError:
        print("Invalid input. Please enter numeric values for price and discount percentage.")

if __name__ == "__main__":
    main()