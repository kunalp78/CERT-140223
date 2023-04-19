import operations as op
import random
import string

enter = True
while enter:
    print("Main Menu: ")
    print("1) Login")
    print("2) Register")
    print("3) Quit")
    val = input("Enter your choice between numbers 1-3")
    if val == "3":
        break
    elif val == "1":
        email = input("Enter your email address: ")
        paswd = input("Enter your password: ")
        loginstatus = op.login("user.json", email, paswd) #True
        if loginstatus == False:
            print("Invalid Credentials!!")
        else:
            print("Logged in!")
        while loginstatus:
            print("User Menu!")
            print("1) Show all movies!!")
            print("2) Show Booked Ticket History!!")
            print("3) Book Ticket")
            print("4) Quit")
            val = input("Enter your choice between 1-4: ")
            if val == "4":
                print("See you next time!!")
                break
            elif val == "1":
                print("Movie list!!")
                print("Movie Id ,Movie Name, Total seats, Price, Available Seat")
                op.show_movies("movie.json")
            elif val == "2":
                print("Show the history!!")
                print("Movie ID, Movie Name")
                op.show_booked_ticket_history("user.json", "movie.json", email)
            elif val == "3":
                tkt_id = input("Enter the ticket id: ")
                no_of_seats = int(input("Enter the number of seats you want: "))
                v = input("Do you have preffered seat y/n: ")
                if v == "y" or v == "Y":
                    pref_seat = input("enter your prefered seat with comma seperated").split(",")
                else:
                    pref_seat = []
                out = op.book_ticket("movie.json", "user.json", email, tkt_id, no_of_seats, pref_seat)
                if out:
                    print("Ticket Booked Successfully!!")
                else:
                    print("No ticket was booked!!")
            else:
                print("Enter correct choices between the numbers 1-4")
    elif val == "2":
        # Name, password, dob, number, email, gender, age, location
        name = input("Enter your Name: ")
        paswd = input("Enter your password: ")
        age = input("Enter Age: ")
        email = input("Enter Email: ")
        phn = input("Enter the phn number: ")
        user_id = ''.join(random.choices(string.ascii_lowercase+string.digits, k=5))
        #register("user.json","5479", "Sanvi", "password", "20", "anvi07@gmail.com", "8745897965")
        out = op.register("user.json", user_id, name, paswd, age, email, phn)
        if out:
            print("Registration Successfull!!")
        else:
            print("Can't Register")
    else:
        print("Enter correct choices between the numbers 1-3")