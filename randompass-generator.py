import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
highercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
character = "!@#$%^&*"

mixed = lowercase + highercase + number + character

password = ''.join(random.sample(mixed, 16))

print(f"Here's your password : {password}")
