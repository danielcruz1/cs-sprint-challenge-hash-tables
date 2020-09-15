#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # Your code here
    route = [None] * length
    dest = {}
    for ticket in tickets:
        dest[ticket.source] = ticket.destination
    next = dest["NONE"]

    for i in range(0, length):
        route[i] = next
        next = dest[next]

    return route


    
    
