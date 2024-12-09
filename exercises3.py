def arithmetic_operations(num1, num2):
    addition= num1 + num2
    subtraction= num1 - num2
    multiplication= num1 * num2
    division = num1 / num2
    modulus = num1 % num2
    
    result = f"{addition}\n{subtraction}\n{multiplication}\n{division}\n{modulus}"
    return result


print(arithmetic_operations(10, 5))
# 15
# 5
# 50
# 2.0 
# 0