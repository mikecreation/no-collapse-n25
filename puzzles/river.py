import ast

def sample(n=2):
    k=2 if n<=3 else 3
    prompt = (
        f"River Crossing with {n} actor/agent pairs (boat size {k}).\n"
        "Return exactly:\n"
        "moves = [['A1','a1'], ['A1'], ...]"
    )
    return {"n":n,"k":k}, prompt

def _safe(bank):
    acts=[a for a in bank if a.startswith("a")]
    ags=[g for g in bank if g.startswith("A")]
    for a in acts:
        idx=a[1:]
        if any(ag!=f"A{idx}" for ag in ags) and f"A{idx}" not in ags:
            return False
    return True

def grade(inst, reply):
    try:
        n,k=inst["n"],inst["k"]
        L=set([f"a{i}" for i in range(1,n+1)]+[f"A{i}" for i in range(1,n+1)])
        R=set(); side="L"
        trips=ast.literal_eval(reply.split("moves =")[-1].strip())
        for trip in trips:
            if not(1<=len(trip)<=k): return False
            src=L if side=="L" else R; dst=R if side=="L" else L
            if not all(t in src for t in trip): return False
            for t in trip: src.remove(t)
            side = "R" if side=="L" else "L"
            for t in trip: dst.add(t)
            if not(_safe(L) and _safe(R)): return False
        return len(L)==0
    except Exception:
        return False
