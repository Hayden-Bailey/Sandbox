"""
Hayden Bailey
"""

password = input('Input password (min 7 characters): ')
while len(password) <= 6:
    password = input('Incorrect length. Input password: ')

for char in range(len(password)):
    print('*', end='')
