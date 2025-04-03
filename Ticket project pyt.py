age = int(input("Enter your age: \n"))
if age <= 0:
    print("error! age cannot be less than or equal to 0")
    
else:
    if age >= 65:
        age_group = "senior"
        price = 600
    elif age >= 18 and age <= 64:
        age_group = "adult"
        price = 1000
    elif age>=13 and age <= 17:
        age_group = "teenager"
        price = 700
    elif age <= 12:
        age_group = "child"
        price = 500
        
time = int(input("Enter time of movie in 24-hour format (e.g., 1300 for 1:00 PM): "))

if time>=0000 and time <= 2359:
    if time <= 1200:
        price -= 200
        print(f"Discounted ticket price for {age_group} is: {price} KES")
    else:
        print(f"Ticket price for {age_group} is: {price} KES")
else:
    print("Invalid time entered please try again.")