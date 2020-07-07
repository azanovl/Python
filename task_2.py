def user_data(first_name, last_name, birth_year, city, email, phone):
       return f"User's data: {first_name}, {last_name}, {birth_year}, {city}, {email}, {phone}"

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = input("Enter your birth year: ")
city = input("Enter your city of residence: ")
email = input("Enter your e-mail: ")
phone = input("Enter your phone number: ")

print(user_data(first_name=first_name, last_name=last_name, birth_year=birth_year, city=city, email=email, phone=phone))
