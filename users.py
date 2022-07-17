import requests

USERS_SHEETY_ENDPOINT = "https://api.sheety.co/2e88557564c25945f77532971bf8961a/flightDeals/users"

print("Welcome to Suhayb's Flight Club.")
print("We find the best flight deals and email you!")

name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email?\n")
email_again = input("Type your email again.\n")

if email == email_again:
    print("You're in the club!")
else:
    print("email's do not match. Try again.")

user_inputs = {
    "user": {
        "firstName": name,
        "lastName": last_name,
        "email": email
    }
}

response = requests.post(url=USERS_SHEETY_ENDPOINT, json=user_inputs)
print(response.text)
