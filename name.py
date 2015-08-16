import csv
from random import randint

csv_males = csv.reader(open('male.csv'))
csv_females = csv.reader(open('female.csv'))

males = []
females = []

for row in csv_males:
    males.append(row)
for row in csv_females:
    females.append(row)

sex, letter = '0', '0'

while sex != 'f' and sex != 'm' and sex != '':
    sex = raw_input('Female or Male [f/m]? ')
while not letter.isalpha() and letter != '':
    letter = raw_input('First Letter? ')

if sex == '':
    if randint(0,1) == 0:
        names = females
    else:
        names = males
elif sex == 'f':
    names = females
elif sex == 'm':
    names = males

if letter == '':
    letter = randint(0,25)
else:
    letter = ord(letter.lower()[0]) - 97
name = names[letter][randint(0,9)]
print(name)
