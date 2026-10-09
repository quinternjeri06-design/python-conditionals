passed_all_classes=True
paid_sports_fee=True

if passed_all_classes and paid_sports_fee:
    print("Cleared to join the team")


x=15

if x > 20:
    print ("A")
elif x > 10:
    print("B")
else:
    print ("C")

has_physical_id = True
has_digital_id = False
if has_physical_id and has_digital_id:
    print("Student has both IDs verified.")
else:
    print("Student is missing at least one form of ID.")

age = 17
has_id = True 
if age >= 18 and has_id:
    print("Allowed")
else:
    print("Denied")

score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Fail")

def calculate(a,b):
    return a+b
print(calculate(5,3))

def greet(name="Student"):
    print("Hello",name)
greet()

def check_number(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_number(7))