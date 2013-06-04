#Casos de Uso

* Obteniendo informacion de internet
    * Definición funcional de la información a obtener.
    + Validación de la información a obtener.
    * Evaluar la necesidad de paralelizar el procesamiento de los datos para soportar la masividad (escalabilidad)
	+ Obteniendo información definida de Facebook.
        * Investigar conectividad con facebook.
        + Implementar conectividad con facebook.
        + Testeo de la conectividad con facebook.
        * Integración de la conectividad con facebook con el resto del sistema
	+ Obteniendo información definida de Pinterest.
        * Investigar conectividad con Pinterest.
        + Implementar conectividad con Pinterest.
        + Testeo de la conectividad con Pinterest.
        * Integración de la conectividad con Pinterest con el resto del sistema
	+ Obteniendo información definida de Twitter.
        * Investigar conectividad con Twitter.
        + Implementar conectividad con Twitter.
        + Testeo de la conectividad con Twitter.
        * Integración de la conectividad con Twitter con el resto del sistema
	+ Web mining de paginas de supermercados
    + Web mining de páginas de subastas
    + Web mining de páginas de descuentos
    + Obtener información de sms
        * Averiguar como se podría obtener información companías telefónicas
        + Evaluar hacibilidad del caso de uso frente a la nueva información
        + Implementar la comunicación con las companías telefónicas
        + Testear la comunicación con las companías telefónicas
        * Investigar métodos de extracción de información a partir de textos como los de sms
        + Implementar métodos de extracción de informacióñ desde los sms
        + Testear la extracción de informacióñ desde sms
        * Integrar la obtención de mensajes con la extracción de información
        + Testear la intergración de las partes
        + Integrar la información de sms al resto del sistema

* Se consulta información a travéz de el API publica.
    * Definición de los servicios que van a ser provistos por la API
    + Evaluar como afecta el proveer servicios a los requerimientos de hardware al sistema
    + Implementar los servicios a proveer
    + Testear el correcto funcionamiento de los servicios

* El usuario consulta precios a través de una interfaz amigable
	* Definir cualidades funcionales y no funcionales que debe alcanzar la inferfaz a utilizar
    * Establecer una primera interfaz de fácil implementación
        * Definir funcionalidad a proveer en la primera versión
        + Definir documentación sobre la funcionalidad a proveer
        + Establecer situaciones críticas de usabilidad
        + Implementar la funcionalidad
        + Realizar tests funcionales
        + Realizar tests de usabilidad para recolectar mejoras para la siguiente iteración
        + Realizar tests de stress
    * Realizar una versión 2.0 de la aplicación para usuario
        * Definir y priorizar mejoras y nuevas funcionalidades de la definición anterior
        + Documentar el nuevo producto a alcanzar
        + Establecer situaciones críticas de usabilidad
        + Implementar la funcionalidad
        + Realizar tests funcionales
        + Realizar tests de stress

* Se realizó una consulta por un producto A, y el dispositivo sin tener conexión, logra responder la consulta de alguna forma medianamente satisfactoria.
    + Definir el nivel de funcionalidad que debe ser provista para el usuario en caso de no tener conexión con el sistema
    + Planificar como esta funcionalidad será lograda
    + Realizar las modificaciones necesarias en el sistema central para lograr la funcionalidad
    + Realizar las modificaciones en la interfaz para lograr la funcionalidad
    + Realizar los tests necesarios para corroborar el funcionamiento de la interfaz en caso de no tener conexión con el sistema

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


Referencias
===========

* Caso de uso / tarea
j
+ Caso de uso / tarea dependiente del caso de uso superior
