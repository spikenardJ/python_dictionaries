# Question 2: Python Programming Challenges for Customer Service Data Handling

# Task 1: Customer Service Ticket Tracker

import sys
from termcolor import colored

def open_new_service_ticket(tickets, ticket_number, customer, issue):
    if ticket_number not in tickets:
        tickets[ticket_number] = {"Customer": customer, "Issue": issue, "Status": "open"}
        print(f"{ticket_number} has been added to service tickets.")

    else:
        print(f"{ticket_number} already exists in service tickets.")

def update_service_ticket_status(tickets, ticket_number):
    if ticket_number in tickets:
        status = input(f"Ticket status update. Write (open/closed) to change status of {ticket_number}: ").lower()
        tickets[ticket_number]["Status"] = status
        print(f"The status of {ticket_number} has been changed to {status}.")
    else:
        print(f"Ticket {ticket_number} does not exist in service tickets.")

def display_service_tickets(tickets):
    print(colored("\nOPEN TICKETS", "red", attrs=["bold"]))
    print(colored("----------------", "red", attrs=["bold"]))
    for ticket_number, customer in tickets.items():
        if customer["Status"] == "open":
            print(f"\n{ticket_number}")
            print(f"Customer: {customer['Customer']}")
            print(f"Issue: {customer['Issue']}")
            print(colored(f"Status: {customer['Status']}", "red"))
    print(colored("\nCLOSED TICKETS", "blue", attrs=["bold"]))
    print(colored("----------------", "blue", attrs=["bold"]))
    for ticket_number, customer in tickets.items():
        if customer["Status"] == "closed":
            print(f"\n{ticket_number}")
            print(f"Customer: {customer['Customer']}")
            print(f"Issue: {customer['Issue']}")
            print(colored(f"Status: {customer['Status']}", "blue"))

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

open_new_service_ticket(service_tickets, "Ticket003", "Jim", "Password not updating")
open_new_service_ticket(service_tickets, "Ticket004", "Pam", "Server not connecting")
open_new_service_ticket(service_tickets, "Ticket005", "Cory", "Too many emails")
update_service_ticket_status(service_tickets, "Ticket003")
display_service_tickets(service_tickets)
