### conditionals

age = 18
adult_age = 18
driver_license_age = 20

if age >= adult_age and age >= driver_license_age:
    print("You can drive")
elif age >= adult_age:
    print("You are an adult")
else:
    print("You are a minor")

# one line conditional
message = "You are an adult" if age >= adult_age else "You are an minor"

# False conditional values (0, None, '', [])


