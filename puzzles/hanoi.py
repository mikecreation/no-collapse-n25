import ast

def sample(n=3):
    init = [[i for i in range(n,0,-1)], [], []]
    prompt = (
        f"Solve Tower of Hanoi with {n} disks.\n"
        f"Initial: {init}\nGoal: peg2 same order.\n"
        "Return exactly:\n"
        "moves = [[disk, from_peg, to_peg], ...]"
    )
    return init, prompt

def grade(init, reply):
    try:
        moves = ast.literal_eval(reply.split("moves =")[-1].strip())
        st = [list(s) for s in init]
        for d,s,dst in moves:
            if not st[s] or st[s][-1]!=d:           return False
            if st[dst] and st[dst][-1] < d:         return False
            st[s].pop(); st[dst].append(d)
        return st == [[],[],init[0]]
    except Exception:
        return False
