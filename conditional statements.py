
marks = 70

if marks >= 50:
    print("Pass")

age = 16

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")

marks = 75

if marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")

age = 20
has_id = True

if age >= 18 and has_id:
    print("Condition satisfied")

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Access allowed")
