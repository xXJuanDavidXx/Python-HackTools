import requests                                                                                                                      

#La Función clona una web
def clonar(url):
    data = requests.get(url) # Hace una petición get al sitio web para que devuelva el codigo 

    guardar = open("templates/index.html", "wb") #Crea el archivo .html en modo escritura binaria

    guardar.write(data.content) #El content es para que se guarde todo el contenido, si usamos solo data no se va a guardar
    guardar.close() #Cerramos el archivo

    return "Se ha clonado el sitio web"


input = input("Ingresa la URL de la web a copiar: ")

clonar(input)
