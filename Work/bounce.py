# bounce.py
#
# Exercise 1.5
initial_height = 100
bounce_backup_height = 3/5
number_of_bounces = 10

for bounce in range(number_of_bounces):
    bounce_number = bounce+1
    height = round(initial_height*bounce_backup_height, 4)
    initial_height = height
    print(bounce_number, height)