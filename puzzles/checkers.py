import ast

def sample(n=3):
    board = ["R"]*n + ["_"] + ["B"]*n
    prompt = (
        f"Checkers Jumping with {n} reds and {n} blues.\n"
        f"Initial: {board}\nGoal: {['B']*n + ['_'] + ['R']*n}\n"
        "Return exactly:\n"
        "moves = [[piece, from_idx, to_idx], ...]"
    )
    return board, prompt

def grade(board, reply):
    try:
        moves = ast.literal_eval(reply.split("moves =")[-1].strip())
        b = list(board); n=(len(b)-1)//2
        for p,src,dst in moves:
            if b[src]!=p or b[dst]!="_": return False
            step = dst-src
            if p=="R":
                if step==1: pass
                elif step==2 and b[src+1]=="B": pass
                else: return False
            else:
                if step==-1: pass
                elif step==-2 and b[src-1]=="R": pass
                else: return False
            b[dst],b[src] = b[src],"_"
        return b==["B"]*n+["_"]+["R"]*n
    except Exception:
        return False
