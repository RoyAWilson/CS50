'''

To show the use of and keyword considering grades a student should get

'''

score = int(input('What is the score: '))
if score >=90 and score <= 100:
    print('Grade: A')
elif score >= 80 and score < 90:
    print('Grade: B')
elif score >= 70 and score < 80:
    print('Grade: C')
elif score >= 60 and score < 70:
    print('Grade: C')
elif score >= 50 and score < 60:
    print('Grade: D')
else:
    print('Grade: F')
