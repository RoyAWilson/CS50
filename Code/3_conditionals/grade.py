'''

To show the use of and keyword considering grades a student should get

'''

score = int(input('What is the score: '))
if 90 <= score <= 100:
    print('Grade: A')
elif 80 <= score < 90:
    print('Grade: B')
elif 70 <= score < 80:
    print('Grade: C')
elif 60 <=score < 70:
    print('Grade: C')
elif 50 <= score < 60:
    print('Grade: D')
else:
    print('Grade: F')
