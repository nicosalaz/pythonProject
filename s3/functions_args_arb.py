def concatenar(*args, sep="/"):
    return sep.join(args)

print(concatenar("tierra", "marte", "venus"))

print(concatenar("tierra", "marte", "venus", sep="."))