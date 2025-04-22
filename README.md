# discount-calculator

## **Description** 
* Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
* Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.

# Sample Outputs
## **Discount Applied**
- Enter the original price of the item (kshs): 1000
- Enter the discount percentage: 25
- Final price after 25.0% discount: kshs 750.00

The price drops from kshs 1000 to kshs 750 because the 25% discount is applied.

## **No Discount**
- Enter the original price of the item (kshs): 500
- Enter the discount percentage: 10
- No discount applied (discount < 20%). Final price: kshs 500.00

The price stays kshs 500 because the 10% discount is too small.

## **Wrong Input**
- Enter the original price of the item (kshs): abc
- Invalid input. Please enter numeric values for price and discount percentage.
