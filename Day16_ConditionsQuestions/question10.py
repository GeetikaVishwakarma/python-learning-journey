##Take password and check if it matches "python123".
password = "python123"
attempts = 3

while attempts > 0:
    new = input("Enter password: ")

    if new == password:
        print("Access granted")
        break
    else:
        attempts -= 1
        print("Wrong password")

if attempts == 0:
    print("No more attempts")