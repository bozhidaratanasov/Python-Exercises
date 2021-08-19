import math
number_of_snowballs = int(input())
max_snowball_snow = None
max_snowball_time = None
max_snowball_quality = None
max_snowball_value = -99999999999
for n in range (1, number_of_snowballs + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = int(math.pow((snowball_snow/snowball_time), snowball_quality))
    if snowball_value > max_snowball_value:
        max_snowball_value = snowball_value
        max_snowball_snow = snowball_snow
        max_snowball_time = snowball_time
        max_snowball_quality = snowball_quality
print(f'{max_snowball_snow} : {max_snowball_time} = {max_snowball_value} ({max_snowball_quality})')