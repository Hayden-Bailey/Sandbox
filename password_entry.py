"""
Hayden Bailey
"""

password = input('Input password (min 6 characters): ')
while len(password) <= 5:
    password = input('Incorrect length. Input password: ')

for char in range(len(password)):
    print('*', end='')
