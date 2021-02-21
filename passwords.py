def evaluate_password(list):

    with open('input.txt') as f:
        total_passwords = 0
        for line in f:
            split_line = line.split(" ")

            password = split_line[2]
            chosen_letter_with_colon = split_line[1]
            range = split_line[0]

            split_range = range.split("-")

            min_range = int(split_range[0])
            max_range = int(split_range[1])

            chosen_letter = chosen_letter_with_colon[0]

            letter_count = 0

            for password_letter in password:
                if password_letter == chosen_letter:
                    letter_count += 1

            password_count = 0
            
            if min_range <= letter_count <= max_range:
                password_count += 1
        
            try:
                total_passwords += int(password_count)
            except ValueError:
                pass

        print(total_passwords)

print(evaluate_password(list))
