import datetime
from datetime import date, datetime, time


# Allocate memory for temporary db
events = {}

def add_event():
    event_name = input('Enter Event Name: ')
    date_input = input('Enter Event Date (yyyy-mm-dd): ')

    # Error handling block
    try:
        # Convert string into a date time object with '.strptime()'
        # used .date() to remove the timestamp but keep the date
        event_date = datetime.strptime(date_input, '%Y-%m-%d').date()
        print(event_date)
    
    except ValueError:
        print('Invalid Date Format. Please use yyyy-mm-dd')
        return # this return exits the function
    
    events[event_name] = event_date
    print(f'Successully Added {event_name} to events')

# Helper function to use as key function for sorting
def get_event_date(tup):
# return the date from the (eventname, eventDate)
    return tup[1]

def list_events():
    if len(events) == 0:
        print('No upcomming events')
        return

    print('\n Upcoming Events!')

    # sorted events by date
    # items() method makes a dictionary into a list of tuples
    sorted_events = sorted(events.items(), key=get_event_date)

    # Loop over our sorted_events list, prints name and date of event
    for e_name, e_date in sorted_events:
        today = date.today()
        days_remaining = (e_date - today).days

        print(f'{e_name} - {e_date} - {days_remaining} days until event!')
        

# Create a delete function
    # check if event exists in object
    # if exists del
    # let user
def delete_event():
    eventtodelete = input("Enter the event name to delete: ")

    if eventtodelete in events:
        del events[eventtodelete]
        print(f"{eventtodelete} has been deleted.")
    else:
        print("Event not found.")


def main():
    while True:
        print('\n Event Management System')
        print('1. Add Event')
        print('2. List Event')
        print('3. Delete Event')
        print('4. Quit')

        choice = input('Enter your choices: ')


        if choice == "1":
            add_event()
        elif choice == "2":
            list_events()
        elif choice == "3":
            delete_event()
        elif choice == "3":
            print('Program Closed')
            break
        else:     
            print('Invalid Option. Try again.')

# This makes sure function doesnt automatically run on import
if __name__ == '__main__':
    main()