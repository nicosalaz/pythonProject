def concatenar(*args, sep="/"):
    return sep.join(args)

arguments = ("tierra", "marte", "venus")
print(concatenar(*arguments))
print(concatenar(*arguments, sep="."))