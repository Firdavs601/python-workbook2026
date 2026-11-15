def winning(tickets, winners):
    t = set(tickets)
    w = set(winners)
    return sorted(t & w)    
    


def has_winner(tickets, winners):
    for i in tickets:
        if i in winners:
            return True
    return False