paises = ['UsA', 'colomBIA', 'fRANcia', 'ARGENTIna']

paises_minusculas = map(lambda c: c.casefold(), paises)

print([i for i in paises_minusculas])

