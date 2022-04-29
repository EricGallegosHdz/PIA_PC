from googlesearch import search

def buscadorURL():
    busqueda = search("Werevertumorro", num_results=20, lang="es")
    busqueda = "\n".join(busqueda)

    results = open("results.txt", "w")
    results.write(busqueda)
    results.close
