#Find score letter
grade = int(input("Please enter your grade\n8"))

if grade >= 90:
    score_letter = "A"
    if grade >= 95:
        score_letter = "A+"
elif grade >= 80:
    score_letter = "B"
    if grade >= 85:
        score_letter = "B+"
else:
    score_letter = "C"

print(f"Your Score letter is {score_letter}.")