#clr s
def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

#main
def main():
    choice = int(input("Menu: \n1. Login \n2. Sign Up \nPilih menu (1/2): "))
    #clear_screen()
    
    if choice == 1:
        login():
        clear_screen()
        welcome_message()
    elif choice == 2:
        if sign_up():
            clear_screen()
            laptop_spec() 
    else:
        print("Pilihan tidak valid!")
