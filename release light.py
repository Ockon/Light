import time
import sys
import shutil
import random

def print_center(s):
    print(s.center(shutil.get_terminal_size().columns))

#Logo
print_center("")
print_center("        :::         :::::::::::       ::::::::       :::    :::  :::::::::::: ")
print_center("       :+:             :+:          :+:    :+:      :+:    :+:       :+:      ") 
print_center("      +:+             +:+          +:+             +:+    +:+       +:+       ")       
print_center("     +#+             +#+          :#:             +#++:++#++       +#+        ")        
print_center("    +#+             +#+          +#+   +#+#      +#+    +#+       +#+         ")        
print_center("   #+#             #+#          #+#    #+#      #+#    #+#       #+#          ")          
print_center("  ##########  ###########       ########       ###    ###       ###           ")
print_center("")
print_center("")
print_center("A REVOLUTIONARY WAY TO CODE")
print_center("")
print_center("----------------------------------------------------------------------------------")
print_center("")

print("Loading Light:")

animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("\n")

looper = 1

while looper == 1:

    qtype = input('CREATE (1) / OPEN (2) / COMMAND (3) > ')

    if qtype == '3':

        command = input('COMMAND > ')

        if command == 'HELP':
            print('')
            print('Possible commands:')
            print('-----------------------------')
            print('CMD')
            print('"PRINT", "RANDOM"')
            print('')
            print('Others:')
            print('"EXIT", "HELP", "DOCUMENTATION", "BUILD"')
            looper = 1

        if command == 'PRINT':
            prnt = input('print > ')
            print(prnt)
            looper = 1

        if command == 'RANDOM':
            print(random.randint(0,9999))
            looper = 1

        if command == 'EXIT':
            exit()

        if command == 'DOCUMENTATION':
            print('Ockon.com/documentation')
            print('')
            print('As of alpha 1.0 the website is not online, we apologise for any inconvenience')
            print('you can currently find documentation at https://github.com/Ockon/Light/blob/main/Documentation.MD')
            print('')
            looper = 1

        if command == 'BUILD':
            print('')
            print('VERSION:')
            print('ALPHA 1.0')
            print('')
            print('RELEASE DATE:')
            print('SEPTEMBER 4, 2022')
            print('')
            looper = 1

    else:
        None

    if qtype == '1':
        filename = input('FILE NAME > ')
        fp = open(filename + '.py', 'w')
        looper = 2

    else:
        None

    if qtype == '2':
        filename = input('FILE NAME > ')
        fp = open(filename + '.py', 'a')
        looper = 2

    else:
        None

    qtypestr = str(qtype)

    if qtypestr >= '4':
        print('ERROR, UNRECOGNIZED TYPE')
        looper = 1

y = 1

while y == 1:
    text = input('Light > ')
    text2 = text
    if text.strip() == "": continue

    line2 = ''

    if text.__contains__('//'):
        x = 1
        while x == 1:
            line2 = input('      > ')
            if line2.__contains__('//'):
                text = (text.replace('//', '') + '\n' + line2)
                x = 1

            else:
                x = 2
                y = 2  

        if text.__contains__('//'):
            text = text.replace('//', '')
            y = 2
        else:
            None
            y = 2
       
    textstr = str('\n' + text + '\n' + line2)
    fp.write(textstr)
    print('Processing')
    time.sleep(1)
    print('Completed')
    fp.close()
    x = 2

ext = input('Exit? > ')
if ext == 'y' or 'yes' or 'Y' or 'YES':
    exit()

else:
    print("then what do you want to do? there is no way to do anything else. Shoulda just exited. It's fine, I'll just do it for you")
    time.sleep(1)
    exit()