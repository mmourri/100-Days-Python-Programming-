bmi = 84 / 1.65 ** 2
print(bmi)

# Flooring
print(int(bmi))

# Rounding
print(round(bmi))

print(round(bmi, 2))

print("====================")

# += -= *= /=
score = 0

# User score a point
score += 1
print(score)

print("====================")
# f-strings

print("Your score is : " + str(score))

score = 0
height = 1.8
is_wining = True

print(f"Your score is {score}, your height is  {height}. You are wining is {is_wining}")
