student_test_grades = [100, 88, 77, 66, 99]
total = 0

for number in student_test_grades:
  total += number

avg_denominator = len(student_test_grades)
avg_numerator = total
result = total / avg_denominator

print("Average score for the class is...\n" )
print(result)
