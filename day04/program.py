from tqdm import trange


def check_validity(potential):
    """Check if the potential has two digits."""
    work_string = str(potential)

    doubles_count = 0
    previous_double = []
    already_removed = []

    for i, char in enumerate(work_string):
        if i < len(work_string)-1:
            # print(f"Comparing {char} to {work_string[i+1]}")
            if char == work_string[i+1]:
                if char in previous_double:
                    if not char in already_removed:
                        doubles_count -= 1
                        already_removed.append(char)
                else:
                    doubles_count += 1
                    previous_double.append(char)
            if int(char) > int(work_string[i+1]):
                return False

    if doubles_count > 0:
        return True
    return False


def work_password():

    test_data = [
        111111,
        223450,
        123789,
        112233,
        123444,
        111122,
    ]
    for test_num in test_data:
        is_valid = check_validity(test_num)
        if is_valid:
            print(f"{test_num} is valid.")
        else:
            print(f"{test_num} is not valid.")

    minimum = 171309
    maximum = 643603

    valid_count = 0

    for potential in trange(minimum, maximum):
        is_valid = check_validity(potential)
        if is_valid:
            valid_count += 1

    print(f"Found {valid_count} valid passwords.")

if __name__ == "__main__":
    work_password()