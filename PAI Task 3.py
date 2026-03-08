# Rules Applied at Each Step

# Fill Jug 1 completely

# Fill Jug 2 completely

# Empty Jug 1

# Empty Jug 2

# Pour water from Jug 1 to Jug 2 until Jug 2 becomes full or Jug 1 becomes empty

# Pour water from Jug 2 to Jug 1 until Jug 1 becomes full or Jug 2 becomes empty
def dfs(jug1, jug2, goal, visited, path):
    
    if (jug1, jug2) in visited:
        return False

    visited.add((jug1, jug2))
    path.append((jug1, jug2))

    if jug1 == goal or jug2 == goal:
        print("Solution Path:")
        for step in path:
            print(step)
        return True

    possible_states = [
        (4, jug2),           
        (jug1, 3),           
        (0, jug2),           
        (jug1, 0),           
        (jug1 - min(jug1, 3-jug2), jug2 + min(jug1, 3-jug2)),  
        (jug1 + min(jug2, 4-jug1), jug2 - min(jug2, 4-jug1))   
    ]

    for state in possible_states:
        if dfs(state[0], state[1], goal, visited, path):
            return True

    path.pop()
    return False


visited = set()
dfs(0,0,2,visited,[])