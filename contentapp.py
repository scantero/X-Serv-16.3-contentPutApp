#!/usr/bin/python

"""
 contentApp class
 Simple web application for managing content

 Copyright Jesus M. Gonzalez-Barahona, Gregorio Robles 2009-2015
 jgb, grex @ gsyc.es
 TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
 October 2009 - March 2015
"""

import webapp


class contentApp (webapp.webApp):
    """Simple web application for managing content.

    Content is stored in a dictionary, which is intialized
    with the web content."""

    # Declare and initialize content
    content = {'/': 'Root page',        #Inicializo el diccionario
               '/page': 'A page'
               }

    def parse(self, request):
        """Return the resource name (including /)"""
        metodo = request.split(' ', 1)[0]
        recurso = request.split(' ', 2)[1] #Lo divido por espacios dos veces y me quedo con el segundo parametro
        cuerpo = request.split('\r\n\r\n', 1)[1]
        return metodo, recurso, cuerpo

    def process(self, peticion):
        """Process the relevant elements of the request.

        Finds the HTML text corresponding to the resource name,
        ignoring requests for resources not in the dictionary.
        """
        metodo, recurso, cuerpo = peticion

        if metodo == "GET":
            if recurso in self.content:  #Si esta en el diccionario
                httpCode = "200 OK"
                htmlBody = "<html><body>" + self.content[recurso] \
                    + "</body></html>"
            else:               #Si no esta en el diccionario
                httpCode = "404 Not Found"
                htmlBody = "Not Found"
        elif metodo == "PUT" or metodo == "POST":
            #pass   #para que pase, y no se error de identacion
            self.content[recurso] = cuerpo
            httpCode = "200 OK"
            htmlBody = "Todo bien!"
        else:
            httpCode = "405 Method not allowed"
            htmlBody = "Go away!"
        return (httpCode, htmlBody)


if __name__ == "__main__":
    testWebApp = contentApp("localhost", 1235)
