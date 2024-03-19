def view():
    masterkey= input("To access the usernames and passwords enter the masterkey: ").lower()

    if masterkey == "vishwas":
        with open('passwords.txt', 'r') as f:
            for line in f.readlines(): # f.readlines not f.readline- that prints each string ona  diff line
                data = line.rstrip() # rstrip is for striping the /n in the add function
                Website, username, password = data.split(" | ")
                print("Website: ", Website, "| Username: ", username, "| Password: ", password)
    else:
        print("Invalid masterkey")
            
            
def add():

    Website = input("What website is the username and password for: ").upper()
    username = input("Username: ")
    password = input("Password: ")

    # a mode is for appending to an existing file, w = write overwrite it and r is for read mode.
    with open('passwords.txt', 'a') as f:
        f.write(Website + " | " + username + " | " + password + "\n")

while True:
    mode = input("Would you like to view existing passwords, add new password or press q to quit the program (view, add, q)? ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid Input Try again")
        continue