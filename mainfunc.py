from Tickets import Ticket
def create_ticket():
 #ticket info
    ticket_creator = input("Enter ticket creator: ")
    staff_id = input("Enter staff ID: ")
    email_address = input("Enter email address: ")
    description = input("Enter description: ")

    ticket = Ticket(ticket_creator, staff_id, email_address, description)
    return ticket

def resolve_ticket(ticket):
    response = input("Enter response: ")
    ticket.resolve_ticket(response)

def generate_password(ticket):
    curr_password = input("Enter current password: ")
    if curr_password == ticket.ticket_number:
        new_password = input("Enter new password: ")
        ticket.generate_password(new_password)
    else:
        print("wrong password. Failed to generate password.")

#menu
def menuLoad():

    print('1.Create ticket\n2.Resolve ticket\n3.Display Ticket Statistics\n4.Printing tickets\n5.Generate Password\n6.Reopen\n0.Exit')

    return input("Enter Choice Number: ")


tickets = []

while True:
    choice = menuLoad()
    if choice == '1':
        ticket = create_ticket()
        print("Ticket created successfully.")
    elif choice == '2':
        ticket_number = Ticket.ticket_count
        print("Ticket resolved successfully.")
    elif choice == '3':
        print("Display Ticket Statistics ")
    elif choice == '4':
       # tickets.append(ticket)
        for ticket in tickets:
         print("Printing Tickets: ")
    elif choice == '5':
        ticket_number = int(input("Enter the ticket number to generate password: "))
        print("Ticket number not found.")
    elif choice== '6':
        ticket_number =int(input("Enter ticket to reopen: "))
        print("ticket reopened success")
    elif choice == '0':
        break
    else:
        print(" Invalid choice")