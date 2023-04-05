import string
import random

password_dict = {}

def generate_passwords(form_data):
    names = [form_data[f'word_{i+1}'] for i in range(5)]
    numbers = [form_data[f'number_{i+1}'] for i in range(2)]
    punctuations = string.punctuation.replace("[", "").replace("]", "").replace("'", "")
    specialchars = {"a": "@", "s": "$", "i": "!", "r": "#", "x": "%", "q": "&", "c": "(", "j": ")", "o": "0", "e": "£", "b": "8", "k": "<", "l": "|"}
    passwords = []
    for i in range(1, 6):
        words = random.sample(names, 2)
        number = random.choice(numbers)
        password = "".join(random.choice([str.upper, str.lower])(c) for c in "".join(words))
        password = "".join([specialchars.get(c, c) for c in password])
        password = f"{password}{number}{random.choice(punctuations)}"
        password = "".join(random.sample(password, len(password)))
        password = password[:12] # limit password length to 12 characters
        passwords.append(password)
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return key, passwords

def recover_passwords(form_data, password_dict):
    names = [form_data[f'word_{i+1}'] for i in range(5)]
    numbers = [form_data[f'number_{i+1}'] for i in range(2)]
    key = form_data['key']
    recovered_passwords = []
    if key in password_dict:
        passwords = password_dict[key]
        for i, password in enumerate(passwords):
            words = ''.join(names)
            number = ''.join(numbers)
            password = password.replace(number, "")
            password = password.replace(words.lower(), "")
            password = password.replace(words.upper(), "")
            password = password.replace(words.capitalize(), "")
            password = password.replace(words.title(), "")
            password = password.strip(string.punctuation)
            recovered_passwords.append(password)
    else:
        print("Invalid key.")
    return recovered_passwords
