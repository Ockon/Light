import basic
import time
import sys
import shutil

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

#Loading/Loading Animation
print("Loading Light:")

#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

#Run stuff
for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("\n")

while True:
	text = input('Light > ')
	if text.strip() == "": continue
	result, error = basic.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))