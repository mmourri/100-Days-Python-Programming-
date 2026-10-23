students_scores = [ 150, 142, 185, 120, 172, 184, 24, 149, 59, 68, 199, 78, 67, 89, 86, 55, 35, 91, 64, 89]

total_exam_score = sum(students_scores)
print(total_exam_score)

sum_of_scores = 0
for score in students_scores:
    sum_of_scores += score

print(sum_of_scores)

max_score = 0
for score in students_scores:
    if score > max_score:
        max_score = score

print(max_score)
