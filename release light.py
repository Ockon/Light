from asyncore import write
import time
import sys
import shutil
import random
import os
import colorama
from colorama import Fore, Back, Style

colorama.init()

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
print_center("OCKON")
print_center("")
print_center("A REVOLUTIONARY WAY TO CODE")
print_center("")
print_center("----------------------------------------------------------------------------------")
print_center("")
print("\n")

slashn = ''
looper = 1
while looper == 1:
    toplooper = 1
    while toplooper == 1:
        print_center('CREATE (1) / OPEN (2) / COMMAND (3) / EXIT (4)')
        qtype = input(' > ')
        if qtype == '3':
            command = input('COMMAND > ')
            if command == 'HELP':
                print('')
                print('Possible commands:')
                print('-----------------------------')
                print('CMD:')
                print('"PRINT", "RANDOM", "RENAME"')
                print('')
                print('SETTINGS:')
                print('"TEXT COLOR"')
                print('')
                print('Others:')
                print('"EXIT", "HELP", "DOCUMENTATION", "BUILD"')
                looper = 1
                toplooper = 1
            elif command == 'PRINT':
                prnt = input('print > ')
                print(prnt)
                looper = 1
                toplooper = 1
            elif command == 'RANDOM':
                print(random.randint(0,9999))
                looper = 1
                toplooper = 1
            elif command == 'EXIT':
                exit()
            elif command == 'DOCUMENTATION':
                print('Ockon.com/documentation')
                print('')
                print('you can currently find documentation at https://github.com/Ockon/Light/blob/main/Documentation/Documentation.MD')
                print('')
                looper = 1
                toplooper = 1
            elif command == 'BUILD':
                print('')
                print('VERSION:')
                print('ALPHA 2.0')
                print('')
                print('RELEASE DATE:')
                print('SEPTEMBER 10, 2022')
                print('')
                looper = 1
                toplooper = 1
            elif command == 'TEXT COLOR':
                tcolor = input('TEXT COLOR > ')
                if tcolor == 'RED':
                    print(Fore.RED)
                    looper = 1
                    toplooper = 1
                elif tcolor == 'BLUE':
                    print(Fore.BLUE)
                    looper = 1
                    toplooper = 1
                elif tcolor == 'CYAN':
                    print(Fore.CYAN)
                    looper = 1
                    toplooper = 1
                elif tcolor == 'WHITE':
                    print(Fore.WHITE)
                    looper = 1
                    toplooper = 1
                elif tcolor == 'BLACK':
                    print(Fore.BLACK)
                    looper = 1
                    toplooper = 1
                elif tcolor == 'GREEN':
                    print(Fore.GREEN)
                    looper = 1
                    toplooper = 1
                elif tcolor == 'YELLOW':
                    print(Fore.YELLOW)
                    looper = 1
                    toplooper = 1
                elif tcolor == 'MAGENTA':
                    print(Fore.MAGENTA)
                    looper = 1
                    toplooper = 1
                else:
                    print(Fore.RED)
                    print('ERROR, UNSUPORTED COLOR')
                    print(Fore.RESET)
                    looper = 1
                    toplooper = 1
                looper = 1
                toplooper = 1
            elif command == 'RENAME':
                cname = input('FILE NAME > ')
                nname = input('NEW NAME  > ')
                os.rename(cname, nname)
                toplooper = 1
            else:
                print(Fore.RED)
                print('ERROR, UNKNOWN COMMAND')
                print(Fore.RESET)
                looper = 1
                toplooper = 1
        elif qtype == '1':
            filename = input('FILE NAME > ')
            filetype = input('FILE EXTENSION > ')
            if filetype.__contains__('.'):
                filetyp = filetype.replace('.', '')
            fp = open(filename + '.' + filetype, 'w')
            #looper = 2
            toplooper = 2
            slashn = ''
        elif qtype == '2':
            filename = input('FILE NAME > ')
            filetype = input('FILE EXTENSION > ')
            if filetype.__contains__('.'):
               filetype = filetype.replace('.', '')
            try:
                fp = open(filename + '.' + filetype, 'r')
                fp.close()
            except:
                print(Fore.RED)
                print('ERROR, FILE NOT FOUND')
                print(Fore.RESET)
            cncate = input('TRUNCATE (1) / START FROM LAST LINE (2) > ')
            if cncate == '1':
               fp.truncate(0)
               toplooper = 2
            elif cncate == '2':
               toplooper = 2   
            else:
                print(Fore.RED)
                print('ERROR, UNKNOWN TRUNCATE TYPE')
                print(Fore.RESET)
                looper = 1
                toplooper = 1
            with open(filename + '.' + filetype, 'r') as fp:
                print('')
                print(fp.read(), '\r')
                print(Fore.RED + '                < ')
                print(Fore.RESET)
            fp.close()
            fp = open(filename + '.' + filetype, 'a')
            slashn = '\n'
        elif qtype == '4':
            exit()
        else:
            None
        qtypestr = 1
        try:
            qtypestr = int(qtype)
        except:
            print(Fore.RED)
            print('ERROR, UNRECOGNIZED TYPE 1')
            print(Fore.RESET)
            looper = 1
            toplooper = 1

        if qtypestr >= 5:
            print(Fore.RED)
            print('ERROR, UNRECOGNIZED TYPE 2')
            print(Fore.RESET)
            looper = 1
            toplooper = 1

    slashn2 = ''
    #looper = 2
    y = 1
    while y == 1:
        text = input('      > ')
        if text.strip() == "": continue
        line2 = ''
        if text.__contains__('//'):
            x = 1
            while x == 1:
                line2 = input('      > ')
                if line2.__contains__('//'):
                    slashn2 = '\n'
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
      
        textstr = str(slashn + text + slashn2 + line2)
        fp.write(textstr)
        print('Processing')
        time.sleep(1)
        print('Completed')
        fp.close()
        x = 2
        ext = input('Exit? (y/n) > ')
        if ext == 'y':
            looper = 2
            exit()
        else:
            looper = 1
            toplooper = 1
            y = 2
            qtype = None