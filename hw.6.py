def strong_password(password):
    if len(password) < 6:
        return False
    digit=False
    upper=False
    lower=False
    special_count=0
    for char in password:
        if char.isdigit():
            digit=True
        elif char.isupper():
            upper=True
        elif char.islower():
            lower=True
        else:
            special_count=special_count+1

    if digit and upper and lower and special_count >= 2:
        return True
    else:
        return False
user_password = input("Введите пароль: ")
if strong_password(user_password):
    print("Пароль надёжный :)")
else:
    print("Пароль ненадёжный :(")

def nearest_number(numbers, target = 0):
    return min(numbers, key=lambda x:
abs(x - target))

print(nearest_number([1, 2, 3], 5))
# -> 3
print(nearest_number([-10, -2, 7], 0))
# -> -2
print(nearest_number([0.5, 2.5, 3.1], 2))
# ->2.5
print(nearest_number([10, 20, 30], 25))
# ->20



