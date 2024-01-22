# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

# pseudocode

# Check the first condition
# if product <= 1000:
# Output if product is less than or equal to 1000
# else:
# # Output if product is greater than 1000
# Calculate the sum
# condition one
# condition two
# result

# calculate product of two number
def calculate_product_or_sum(number1, number2):
    product = number1 * number2

# if product <= 1000:
# Output if product is less than or equal to 1000  
    if product <= 1000:
        result = product
        output_message = f"The result is {result}"
# else:
# # Output if product is greater than 1000
    else:
        result = number1 + number2
        output_message = f"The result is {result}"
# Calculate the sum       
    return output_message

# condition 1
number1_1 = 20
number2_1 = 30
output_1 = calculate_product_or_sum(number1_1, number2_1)
print(output_1)



    