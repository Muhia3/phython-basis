yourname = input("name ")
whatyear = input ("Which year is it ")
print(yourname,"thinks it is " , whatyear)

print("uh , oh , you have been given a ", "\033[32m", "warning", "\033[0m", "for being a bad person ")

#if statement
myname = input("Whats your name ")
if myname == "Richard": #colon at the end indicates if that is fulllfilled the go on and ...
    print ("welcome bigman")
    print("you are one of the coolest guy ever seen niggah")
else:
    print("who the fuck are you even dude")

#3. elif .. after if buh b4 else since else means everything
print("SECURE LOGIN")
username = input("username ")
if username == "Richard":
    print("welcome mr ")
elif username == "suzanne":
    print("hey madam")
else:
    print("404 error try again please")


        #4. adding some password to the code
print("""
SECURE LOGIN
To the number one platform
++++++++++++
""")
username = input("username ")
password = input("passsword ")

if username == "Richard" and password == "richard":
    print("welcome mr safaricom is for you! ")
elif username == "suzanne" or password == "suzanne":
    print("hey madam, welcome to safaricom customer care services ")
else:
    print("404 error try again please")

            # 5. nested if .. just noted that 2 inputs (diferent if else)
matthika = input ("Which is you best matatu from thika to nairobi ")
if matthika == "2nk":
    print ("You value time!")
    favourite = input ("who is your all time driver ")
    if favourite == "keith Njamah":
        print ("Nice taste")
    else:
        print("maybe havent met yours")
elif matthika ==  "supermetro":
    print("You value your safety")
else:
    print("Thats unroad worthy")



     #day 6 of hundred days
x = int(input("Enter value of x "))
y = int(input("Enter value of y "))
z = int(input("Enter the value of z"))

if x < y :
     print("x is less than y")

elif x > y:
    print("x is greater than y")

elif x== y:
        print("x is equal to y")
else:
    print("its like your input aint working out")
          
    #7. power of assigning variables.. assign each
name = input("Please enter the subscriber name ")
if name == "Davie" or name == "davie":
    print("hello programmer")
else: print("Introduce yourself to the freelancers first")


print([1,2,3,4,5,6]*3)

#Day 7 
favouriteTv = input ("whats your favourite tv mr idler??? ")
if favouriteTv  == "Inooro":
    print("your must be a kikuyu")
    favouritePart = input("Which show just makaes you tuned in inooro ")
    if favouritePart == "jera ino ciitu":
        print("sawa kijana ya huruma")
    else:
        print("you have different taste from the many")
elif favouriteTv == "citizen":
    print ("you are aging up my G")
elif favouriteTv == "mutongoi":
 print("sawa wa kwitu")
else:
    print( " This is a free country for your Tv choice")


#7. assignment project
print("fake fun finder")
anime = input(" whats your favourite anime")
 
if anime == "one piece":
    print("oh really")
    actor = input("name me any character")
    if actor == "nami":
        print("you got that but on pure chance")
        job = input("okaythen, what is her role in the ship")
        if job == "navigator":
            print("Hmph")
        bounty = input("what was her first  bounty then ")
        if bounty == "ummm":
#             print ("seee fake piece of fun")
   
computer_science = float(input("kindly enter your marks "))
if computer_science > 100:
    print("""
    Try again
    maximum score is 100 please
    """)
elif  computer_science >=90:
    print( "A+ , excellent you must be happy ")
elif  computer_science>=80:
    print ("A-")
elif computer_science >=70:
    print ("which is a B")
else:
    print("Below avrege")


    #8 Trial
name = input("Enter your name master ")
if name == "muhia" or name == "kyalo":
    print ("Hello", name)
   
 
19. Epic move game

while exit != "yes":
    print ("mmmh")
    exit =input("Exit?: ")


# #while infinite loop ...if itss running them its definitely looped otherwise it exits
while True:
    print("This program is running ")
    goagain = input ("Go again?: ")
    if goagain ==  "no":
     break 
print("aww , i was having a good codimg time ")

# # simple calculator by the use of while loop
counter = 0
while True:
    answer = int (input("Enter number: "))  
    # print("Adding it up!")
    counter += answer
    print("current total is", counter)
    addanother = input("Add another? ")  #yes or no
    if addanother == "no":
        break
    print ("bye MR:")

spam_amount =0
spam_amount = spam_amount + 4
if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam Spam Spam"
print(viking_song)


#for loop to loop if we know how many times to repeat
#with the syntax: for (new_var) in range (no. of values):
for counter in range(10):
    print(counter)
    principal = 1000
    monthly_rate = 0.05* 0.12 #monthly rate 
    duration = 10*12 #loan amount in 12 months

    
principal = 1000  # Loan principal amount
interest_rate = 0.05/12  # Annual interest rate
loan_duration = 10*12  # Loan duration in years

monthly_payment = (principal *interest_rate) / (1 - (1 + interest_rate) ** -loan_duration)

print("Loan payment amount after 10 years:", round(monthly_payment, 2))

#using of a for loopnh 
monthly_payment = 0

for i in range(loan_duration):
    monthly_payment += (principal * interest_rate) / (1 - (1 + interest_rate) ** -loan_duration)

print("Loan payment amount after 10 years:", round(monthly_payment, 2))
