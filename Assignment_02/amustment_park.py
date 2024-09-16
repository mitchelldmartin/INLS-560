# This lesson teaches how to test if else statements, order matters.

age = 101

if age < 4:
    print("Admission is $0")
elif age < 18:
    print("Admission is $25")
elif age > 100:
    print("Admission is $0 and you get a free beer")
    
elif age > 60:
    print("Admission is $35")
    # this is not going to work here, put it above 60
# elif age > 100:
    # print("Admission is $0 and you get a free beer")
else:
    print("Amission price is $40")
    
    