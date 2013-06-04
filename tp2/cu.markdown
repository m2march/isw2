#Casos de Uso

* Obteniendo informacion de ...
	* Facebook.
	* Pinterest.
	* Twitter.
	* Web minning de paginas de supermercados y bla bla ...
	* etc ...
**Descripción**: El sistema colecta la información de los distintos medios, la procesa, y almacena la información obtenida en la base de datos, o algun otro medio. _Solo almaceno productos de rubros habilitados?_.

* Se consulta información a través de el API publica.
**Descripción**: Es posible realizar consultas al sistema mediante un API Publica (Rest?, XmlRpc?, SOAP?, Varias?, etc...).

* Se consulta infromación a través de una interfaz amigable al usuario (web?, desktop?, ...). 
	* Diria de dividir esto en 2 etapas, una en la que se implementa una interfaz linda, pero simple, y otra con funcionalidad avanzada. Asi se puede poner el producto en el mercado cuanto antes (y empezar a autofinanciarse).


* Se puede consultar información offline.
**Descripción**: Utilizando una caché, o algo por el estilo, proveer cierta funcionalidad. Una podria ser tener disponible de forma offline un historial con los resultados de busquedas previas. 

* ABM de rubros habilitados.
* ABM de productos en un rubro.

* Si realizo una consulta por un producto A, obtengo ofertas de este producto.
**Descripción**: Se busca en la base de datos del sistema ofertas que cumplan lo especificado.

* Si realizo una consulta por un producto A y este no esta se le informa al usuario.
* Si realizo una consulta por un producto A, que se sustituye por B, tambien se muestran ofertas de B.
* Si realizo una consulta por un producto A, que se asocia con B, tambien se muestran ofertas de B.

* Se prepara un informe con las estadisticas de ofertas detectadas como falsas.

* Mientras escribo una busqueda, se comienzan a obtener resultados.
* Al ingresar a la pagina, se sugieren ofertas, basado en busquedas anteriores (Relacionado con que hay que obtener resultados cuanto antes, tal vez habria q acordarlo con el PO).

* El usuario se autentifica usando OpenID.
* Un usuario autentificado puede votar por la validez de una oferta.
* Las ofertas mostradas a un usuario autenticado se priorizan usando su mecanismo de confianza. 

* Sistema de ofertas promocionadas (las empresas pagan por que sus productos aparezcan primeros en las busquedas, o resaltados). La meto pq hay que autofinanciarse.
