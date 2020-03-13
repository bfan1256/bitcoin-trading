from collections import deque

def getBottoms(prices, n=1):
    q = deque()
    bottoms = []
    for idx, p in enumerate(prices):
        if len(q) == 0:
            q.append(p)
        elif len(q) < n:
            if p < q[-1]:
                q.append(p)
            else:
                q.clear()
        elif len(q) == n:
            if p < q[-1]:
                q.append(p)
                bottoms.append((idx,p))
            else:
                q.clear()
        elif len(q) > n:
            if len(q) == 2*n+1:
                q.clear()
                q.append(p)
            else:
                if p > q[-1]:
                    q.append(p)
                else:
                    q.clear()
                    del bottoms[-1]
    return bottoms

def getTops(prices, n=1):
    q = deque()
    tops = []
    for idx, p in enumerate(prices):
        if len(q) == 0:
            q.append(p)
        elif len(q) < n:
            if p > q[-1]:
                q.append(p)
            else:
                q.clear()
        elif len(q) == n:
            if p > q[-1]:
                q.append(p)
                tops.append((idx,p))
            else:
                q.clear()
        elif len(q) > n:
            if len(q) == 2*n+1:
                q.clear()
                q.append(p)
            else:
                if p < q[-1]:
                    q.append(p)
                else:
                    q.clear()
                    del tops[-1]
    return tops