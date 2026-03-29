while True:
    attempt = 0

    while True:
        prompt = 'Please enter a new password that has at least 6 characters, one digit, one upper and one lower word.'
        password = input(prompt)

        attempt += 1

        has_upper = False
        has_lower = False
        has_digit = False
        has_symbol = False

        for ch in password:
            if ch.isupper():
                has_upper = True
            if ch.islower():
                has_lower = True
            if ch.isdigit():
                has_digit = True
            if not ch.isalnum():
                has_symbol = True

        score = 0

        if len(password) >= 6:
            score += 1
        if has_upper:
            score += 1
        if has_lower:
            score += 1
        if has_digit:
            score += 1
        if has_symbol:
            score += 1

        if score <= 4:
            print(f"Not really secure, try again\n({3 - attempt} attempts left)")
        else:
            print(f"Quite strong password ({score}/5)")
            break

        if attempt >= 3:
            print('Too many attempts, try again later')
            break

    again = input('Would you like to try again? yes or no? ')

    if again.lower() != "yes":
        print("Shutting it down...")
        break