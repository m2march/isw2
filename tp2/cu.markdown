#Casos de Uso

* Obteniendo informacion de ...
	* Facebook.
	* Pinterest.
	* Twitter.
	* Web minning de paginas de supermercados y bla bla ...
	* etc ...

* Se consulta información a travéz de el API publica.
* Se consulta infromación a travéz de una interfaz amigable al usuario (web?, desktop?, ...). 
	* Diria de dividir esto en 2 etapas, una en la que se implementa una interfaz linda, pero simple, y otra con funcionalidad avanzada. Asi se puede poner el producto en el mercado cuanto antes (y empezar a autofinanciarse).

* Se puede consultar información offline.

* ABM de rubros habilitados.
* ABM de productos en un rubro.

* Si realizo una consulta por un producto A, obtengo ofertas de este producto.
* Si realizo una consulta por un producto A, este esta en un rubro habilitado.
* Si realizo una consulta por un producto A, que se sustituye por B, tambien se muestran ofertas de B
* Si realizo una consulta por un producto A, que se asocia con B, tambien se muestran ofertas de B

* Se minimizan las probabilidades de que una oferta sea SPAM. (Me suena a obj no funcional)

* Se prepara un informe con las estadisticas de ofertas detectadas como falsas.

* Mientras escribo una busqueda, se comienzan a obtener resultados.
* Al ingresar a la pagina, se sugieren ofertas, basado en busquedas anteriores (Relacionado con que hay que obtener resultados cuanto antes, tal vez habria q acordarlo con el PO).

* El usuario se autentifica usando OpenID.
* Un usuario autentificado puede votar por la validez de una oferta.
* Las ofertas mostradas a un usuario autenticado se priorizan usando su mecanismo de confianza. 

* Sistema de ofertas promocionadas (las empresas pagan por que sus productos aparezcan primeros en las busquedas, o resaltados). La meto pq hay que autofinanciarse.
