# first_number = float(input("enter first number:"))
# second_number =float (input("enter second number:"))

# sum = first_number+second_number
# print("sum:" +  str(sum))


course = "applied statistics with computing"
print(course.replace('with', "eyuige"))
print(course.find("y"))

t = 10 + 5 * 4
print(t)

price = 25
print(price>9 and price<20)

temperature =45

if temperature > 30 :
    print("""
           drink water
    the temperatures are so high for babies""")
elif temperature  < 25:
    print("have a sweater for some warmth")
else:
    print("Temperatures are moderate for your body person")

  

i= 1
while i<=5:
    print(i ,end='')
    i = i +1
   
i= 1
while i<=5:
    print(i * '*')
    i = i +1
    
names = ["manu", "bob", "sham", 'keith']
names [0] = "manuela"
print(names)
print(len(names))

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
for item in thisset:
 print("banana" in thisset)
 print(item)
 

for i in range(6):
     print(i * '*')
i = i +1


x = int(input("Enter value of x "))
y = int(input("Enter value of y "))
z = int(input("Enter value of z "))

if x < y :
     print("x is less than y")

elif x > y:
    print("x is greater than y")

elif x== y:
        print("x is equal to y")
else:
    print("its like your input aint working out")


print("""
my name is richard muhia 
named after the famous kimondiu
current attached at machakos level five hospital
and am third year at karatina university""")