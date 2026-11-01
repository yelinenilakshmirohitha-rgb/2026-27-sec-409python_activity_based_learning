# Attendance Recovery Computation

attended = int(input("Enter classes attended: "))
total = int(input("Enter total classes: "))
target = float(input("Enter required attendance percentage: "))

percentage = (attended / total) * 100

print("Current Attendance:", percentage, "%")

if percentage >= target:
    print("You are eligible")
else:
    future = 0
    while ((attended + future) / (total + future)) * 100 < target:
        future = future + 1

    print("You need to attend", future, "more classes")
