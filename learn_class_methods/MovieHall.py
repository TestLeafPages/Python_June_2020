class Movie_Hall:

    # variable   - instance nd class level
    # methods    - instance, class and static
    # constructors

    def ticket_booking(self, scr):
        if(scr == 1):
            print("Darbar")
        elif(scr == 2):
            print("Master")
        else:
            print("show is full")


per1 = Movie_Hall()
per1.ticket_booking(111)


print(Movie_Hall.mro())




