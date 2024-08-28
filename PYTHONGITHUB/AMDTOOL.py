import os
import sys
import subprocess
import random
import time

#half project


print("Welcome to Windows Tool")
time.sleep(2)
print("Coded by Moogy :)")
time.sleep(2)
os.system('cls')



print("1) Check if a path exists  ")
print("2) Check if a path is a file ")
print("3) Check if a path is a directory  ")
print("4) Execute a command in a subshell ")
print("5) remove (delete) a file.")
print("6) Simple game By me ")

operation = input("Enter your Choice : ")

#if user choice is 1

if operation == "1":
    os.system('cls')
    path_to_check = input("Enter the path to check: ")
    if os.path.exists(path_to_check):
        print(f"The path '{path_to_check}' exists.")
    else:
        print(f"The path '{path_to_check}' does not exist.")
   



#if user choice 2
elif operation == "2":
    os.system('cls')
    path_to_check = input("Enter the path to check: ")
    if os.path.isfile(path_to_check):
        print(f"The path '{path_to_check}' is a file.")
    else:
        print(f"The path '{path_to_check}' is not a file.")
        sys.exit()




#if user choice 3

elif operation == "3":
    os.system('cls')
    path_to_check = input("Enter the path to check: ")
    if os.path.isdir(path_to_check):
      
      print(f"The path '{path_to_check}' is a directory.")
    else:
      print(f"The path '{path_to_check}' is not a directory.")












elif operation == "4":
    os.system('cls')
    
    print("\nNetwork Command Menu:")
    print("1. netstat - Display network connections and listening ports.")
    print("2. tracert - Trace route to a network host.")
    print("3. nslookup - Query DNS to obtain domain name or IP address mapping.")
    print("4. net use - Display or connect to network resources.")
    print("5. netsh - Network shell commands.")
    print("6. Exit - Exit the menu.")

    choice = input("Enter the number of your choice: ")

    if choice == '1':
        result = subprocess.run('netstat -an', shell=True, capture_output=True, text=True)
        print("Network Connections and Listening Ports:")
        print(result.stdout)
        if result.stderr:
         print("STDERR:")
         print(result.stderr)
        print("Exit Code:")
        print(result.returncode)

        
    elif choice == '2':
        host = input("Enter the hostname or IP address to trace: ")


        result = subprocess.run(f'tracert {host}', shell=True, capture_output=True, text=True)

        print("Trace Route Results:")
        print(result.stdout)


        if result.stderr:
         print("STDERR:")
         print(result.stderr)


        print("Exit Code:")
        
        print(result.returncode)
        












        

    
    






elif operation == "5":
    os.system('cls')
elif operation == "6":
    os.system('cls')

else:
    os.system('cls')
    print("Enter Correct Operation Number " )
    sys.exit()

