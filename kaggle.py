

#  #  functions ...continuation of kaggle 
# def add_three(input_var):
#     out_var = input_var + 3
#     return out_var

# def age_to_vote(age):
#     """Can someone of following age do voting?"""
#     return age>= 18

# print ("can do voting: ", age_to_vote(65))

# #for loops where we use with known number of looping ..under range 
# #has the syntax : for (newvar) in range (no of loops):
# for counter in range(10):
#     print(counter)
  
# total = 44
# print("The other code for the totas is")

# for number in range (20):
#     total += number
#     print(total)
  

#   #assignment
# loan = 1000
# for payment in range(10):
#     payment = loan*0.01
#     print(payment)


#     import numpy
# import matplotlib.pyplot as plt

# x = numpy.random.normal(5.0, 1.0, 100000)

# plt.hist(x, 100)
# plt.show()

#creation of patterns using for loop
mystring = "kimonideou"
x = 0
for i in mystring:
    x = x+1
    print (mystring[0:x])
for i in mystring:
    x = x-1
    print (mystring[0:x])