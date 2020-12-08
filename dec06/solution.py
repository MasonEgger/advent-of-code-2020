def sum_survey_at_least_one(answers):
    total = 0
    answer_set = set()
    for answer in answers:
        if answer == "":
            total += len(answer_set)
            answer_set = set()
        else:
            for let in answer:
                answer_set.add(let)
    return total


def sum_survey_every_one(answers):
    total = 0
    answer_set = None
    for answer in answers:
        if answer == "":
            total += len(answer_set)
            answer_set = None
        else:
            if answer_set is None:
                answer_set = set(answer)
            else:
                tmp_set = set(answer)
                answer_set = answer_set.intersection(tmp_set)
    return total


if __name__ == "__main__":
    with open("input.txt", "r") as fh:
        answers = fh.read().split("\n")

    answers.append("''")
    print(sum_survey_at_least_one(answers))
    print(sum_survey_every_one(answers))