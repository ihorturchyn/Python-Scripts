#!/usr/bin/env python3
while True:
    print('Who are you?')
    name = input()
    if name == 'Ihor':
        print('Hello Ihor. What is a password?')
    else:
        print('Incorrect username')
        break
    passwd = input()
    if passwd == 'password':
        print('Access granted')
        break
    else:
        print('please try to put correct password')
        continue