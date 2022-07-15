'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    fromMember_following = social_graph[from_member]['following']
    toMember_following = social_graph[to_member]['following']
    if to_member in fromMember_following and from_member in toMember_following:
        return "friends"
    elif to_member in fromMember_following:
        return "follower"
    elif from_member in toMember_following:
        return "followed by"
    else:
        return "no relationship"


def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    vertical = [list(v) for v in zip(*board)]
    updown = [board[i][i] for i in range(len(board))]
    downup = [board[len(board)-1-i][i] for i in range(len(board))]
    
    for i in range(len(board)):
    # horizontal wins
        if all([s=='X' for s in board[i]]):
            return 'X'
        elif all([s=='O' for s in board[i]]):
            return 'O'
    # vertical wins
        elif all([s=='X' for s in vertical[i]]):
            return 'X'
        elif all([s=='O' for s in vertical[i]]):
            return 'O'
    
    # diagonal wins (updown)
    if all([s=='X' for s in updown]):
        return 'X'
    elif all([s=='O' for s in updown]):
        return 'O'
    # diagonal wins (downup)
    elif all([s=='X' for s in downup]):
        return 'X'
    elif all([s=='O' for s in downup]):
        return 'O'
    # no wins
    else:
        return 'NO WINNER'

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    to_from = list(route_map.keys())
    fromStop = [x for x in zip(*to_from)][0]
    toStop = [x for x in zip(*to_from)][1]
    fromIndex = int(fromStop.index(first_stop))
    toIndex = int(toStop.index(second_stop))
    
    time_values = []
    
    if first_stop == second_stop:
        return 0
    elif fromIndex < toIndex:
        for i in range(fromIndex,toIndex+1):
            time_values.append(route_map[to_from[i]]['travel_time_mins'])
        return sum(time_values)
    elif fromIndex > toIndex:
        for i in range(fromIndex,len(to_from)):
            time_values.append(route_map[to_from[i]]['travel_time_mins'])
        for i in range(0,toIndex+1):
            time_values.append(route_map[to_from[i]]['travel_time_mins'])
        return sum(time_values)
    elif fromIndex == toIndex:
        time_values.append(route_map[to_from[fromIndex]]['travel_time_mins'])
        return sum(time_values)