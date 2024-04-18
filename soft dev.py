class Ticket:
    ticket_counter = 0
    tickets_created = 0
    tickets_resolved = 0
    tickets_open = 0

    def __init__(self, creator_name, staff_id, contact_email, issue_description):
        Ticket.ticket_counter += 1
        Ticket.tickets_created += 1
        self.ticket_number = Ticket.ticket_counter + 2000
        self.creator_name = creator_name
        self.staff_id = staff_id
        self.contact_email = contact_email
        self.issue_description = issue_description
        self.response = "Not Yet Provided"
        self.status = "Open"
        Ticket.tickets_open += 1

    def resolve_ticket(self, response=None):
        if "Password Change" in self.issue_description:
            new_password = self.staff_id[:2] + self.creator_name[:3]
            self.response = f"New password generated: {new_password}"
        else:
            if response:
                self.response = response
        self.status = "Closed"
        Ticket.tickets_resolved += 1
        Ticket.tickets_open -= 1

    def reopen_ticket(self):
        self.status = "Reopened"
        Ticket.tickets_resolved -= 1
        Ticket.tickets_open += 1

    def provide_response(self, response):
        self.response = response

    @staticmethod
    def display_ticket_statistics():
        print("\nDisplaying Ticket Statistics\n")
        print(f"Tickets Created: {Ticket.tickets_created}")
        print(f"Tickets Resolved: {Ticket.tickets_resolved}")
        print(f"Tickets To Solve: {Ticket.tickets_open}")

    def display_ticket_info(self):
        print("\nPrinting Ticket:\n")
        print(f"Ticket Number: {self.ticket_number}")
        print(f"Ticket Creator: {self.creator_name}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Email Address: {self.contact_email}")
        print(f"Description: {self.issue_description}")
        print(f"Response: {self.response}")
        print(f"Ticket Status: {self.status}")


# Main program
if __name__ == "__main__":
    # Create tickets
    tickets = [
        Ticket("Inna", "INNAM", "inna@whitecliffe.co.nz", "My monitor stopped working"),
        Ticket("Maria", "MARIAH", "maria@whitecliffe.co.nz", "Request for a videocamera to conduct webinars"),
        Ticket("John", "JOHNS", "john@whitecliffe.co.nz", "Password change")
    ]

    # Resolve some tickets
    tickets[0].resolve_ticket("The monitor has been replaced.")
    tickets[1].resolve_ticket()

    # Display ticket statistics
    Ticket.display_ticket_statistics()

    # Display ticket information
    for ticket in tickets:
        ticket.display_ticket_info()

    # Reopen some resolved tickets
    tickets[0].reopen_ticket()

    # Display ticket statistics after reopening tickets
    Ticket.display_ticket_statistics()

    # Display ticket information after reopening tickets
    for ticket in tickets:
        ticket.display_ticket_info()
