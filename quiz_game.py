print('Welcome to  the QUIZ!')
playing = (input('Would you like to play? ')).upper().strip()

if playing != 'YES':
    quit()

print('Thank you for playing! Lets GO! ')
score = 0

answer = input('What is the Capital city of Malawi?  ')
if answer.upper() == 'LILONGWE':
    print('Correct!')
    score += 1


answer = input('What is the Capital city of Zimbabwe  ')
if answer.upper() == 'HARARE':
    print('Correct!')
    score += 1

# answer = input('What is the Capital city of South Africa?  ')
# if answer.upper() == 'JOHANNESBURG':
#     print('Correct!')
#     score += 1

answer = input('What is the Capital city of Nigeria?  ')
if answer.upper() == 'LAGOS':
    print('Correct!')
    score += 1

print('YOUR SCORE:' +str(score)+' out of '+str(3)+' questions correct')
print(str((score/3)*100)+'%')