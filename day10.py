import re

with open("d10i.txt", "r") as file:
    lines = [line.rstrip() for line in file]

non_corrupt_lines = []

# Part 1
consec_complete_brackets_regex = "\(\)|\[\]|{}|<>"

ILLEGAL_CHAR_TO_POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

score = 0
for line in lines:
    while re.search(consec_complete_brackets_regex, line):
        line = re.sub(consec_complete_brackets_regex, "", line)
    first_illegal_char = ""
    for char in line:
        if char in ")]}>":
            first_illegal_char = char
            break
    if first_illegal_char:
        score += ILLEGAL_CHAR_TO_POINTS[first_illegal_char]
    else:
        non_corrupt_lines.append(line)

print("Total score:", score)

# Part 2
AUTOCOMPLETED_CHAR_TO_POINTS = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

scores = []
for line in non_corrupt_lines:
    while re.search(consec_complete_brackets_regex, line):
        line = re.sub(consec_complete_brackets_regex, "", line)
    mapping_table = line.maketrans("([{<", ")]}>")
    missing_characters = line.translate(mapping_table)[::-1]
    score = 0
    for char in missing_characters:
        score *= 5
        score += AUTOCOMPLETED_CHAR_TO_POINTS[char]
    scores.append(score)

scores.sort()
middle_score = scores[len(scores) // 2]
print("Middle score:", middle_score)
