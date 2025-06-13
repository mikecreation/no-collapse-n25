import ast

def sample(n=3):
    half=n//2
    s0=[chr(65+i) for i in range(half)]
    s1=[chr(65+half+i) for i in range(n-half)]
    init=[s0,s1,[]]
    goal=[[*reversed(s1),*reversed(s0)],[],[]]
    prompt=(
        f"Blocks World with {n} blocks.\n"
        f"Initial: {init}\nGoal: {goal}\n"
        "Return exactly:\n"
        "moves = [[block, from_stack, to_stack], ...]"
    )
    return {"init":init,"goal":goal},prompt

def grade(inst,reply):
    try:
        moves=ast.literal_eval(reply.split("moves =")[-1].strip())
        st=[list(s) for s in inst["init"]]
        for b,s,d in moves:
            if not st[s] or st[s][-1]!=b: return False
            st[s].pop(); st[d].append(b)
        return st==inst["goal"]
    except Exception:
        return False
