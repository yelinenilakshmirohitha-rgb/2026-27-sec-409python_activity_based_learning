# Mobile Plan Cost Optimization

usage = float(input("Enter data usage in GB: "))
days = int(input("Enter validity days: "))
budget = float(input("Enter your budget: "))

p1 = 199
p2 = 299
p3 = 399

if usage > 2:
    p1 = p1 + (usage - 2) * 50

if usage > 5:
    p2 = p2 + (usage - 5) * 30

if usage > 10:
    p3 = p3 + (usage - 10) * 20

print("Plan 1 Cost:", p1)
print("Plan 2 Cost:", p2)
print("Plan 3 Cost:", p3)

if days > 28:
    print("No plan satisfies the validity requirement")
elif p1 <= budget:
    print("Plan 1 is the cheapest eligible plan")
elif p2 <= budget:
    print("Plan 2 is the cheapest eligible plan")
elif p3 <= budget:
    print("Plan 3 is the cheapest eligible plan")
else:
    print("No plan is within your budget")
