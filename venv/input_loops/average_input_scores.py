"""Carl Phillips, gets user information and calculates average scores"""
def average(score_list):
    sum = 0
    list_length = len(score_list)
    for scores in score_list:
        sum += int(scores)

    avg = sum / list_length
    return avg


if __name__ == '__main__':
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    age = input("Enter your age: ")
    user_input = 0
    score_list = []
    try:
        while not user_input == -1:
            user_input = int(input("Add score (-1 to end): "))
            if user_input == -1:
                break
            else:
                score_list.append(user_input)
    except ValueError:
        print("Invalid input")

    avg_scores = average(score_list)
    print(last_name + ", " + first_name + " Grade: " + "{:6.2f}".format(avg_scores))


# example output Phillips, Carl Grade:   7.00
# testing to expect an average, and expecting an error
