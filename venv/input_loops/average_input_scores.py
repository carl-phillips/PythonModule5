def average(score_list):
    sum = 0
    list_length = len(score_list)
    for scores in score_list:
        sum += scores

    avg = sum / list_length
    return avg


if __name__ == '__main__':
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    age = input("Enter your age: ")
    score1 = input("Enter score 1: ")
    score2 = input("Enter score 2: ")
    score3 = input("Enter score 3: ")
    print(fname + " " + lname + " Your average score is " + str(average([int(score1), int(score2), int(score3)])))
