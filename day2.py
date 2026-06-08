#Day 2: 30 days of programming!!

#we start with variables and built in functions, we did a lot of this yesterday as well
import math

first_name="Vaishnavi"
print(first_name)
first_name_to_list= list(first_name)
print(first_name_to_list)

last_name="Gupta"
full_name="Vaishnavi Gupta" 
city="Noida"
country="India"
age=19
year=2026
is_married= False
is_true= True
is_light_on= True

course, friends, hobby= "ECE", 3, "football"

print (type (first_name))
print (type (first_name_to_list))
print (type (last_name))
print (type (full_name))
print (type (city))
print (type (country))
print (type (age))
print (type (year))
print (type (is_married))
print (type (is_true))
print (type (is_light_on))
print (type (course))
print (type (friends))
print (type (hobby))

print (len (first_name))

print(len(first_name) > len(last_name))   
print(len(first_name) == len(last_name))  
print(len(first_name) < len(last_name))   

num_one=5
num_two=4
total=num_one+num_two
diff= num_one-num_two
product=num_one*num_two
division=num_one/num_two
remainder=num_two%num_one
exp= num_one ** num_two
floor_division = num_one // num_two
print(total, diff, product, division, remainder, exp, floor_division)
radius=30
area_of_circle = math.pi * radius ** 2
print(area_of_circle)
circum_of_circle = 2 * math.pi * radius
print(circum_of_circle)

radius=float(input("Enter radius: "))
area_of_circle = math.pi * radius ** 2
print("Area:", area_of_circle)

first_name=input("Enter your first name:")
age=int(input("Enter your age: "))
print(f"Hello {first_name} aged {age}")

help('keywords')