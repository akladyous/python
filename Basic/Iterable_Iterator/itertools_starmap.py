import itertools
# -----------------------------[dev'essere iterabile]
square = itertools.starmap(pow,[[2,2],[2,3],[2,4],[2,5]])
print(list(square))
