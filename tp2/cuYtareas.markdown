#Primeras iteraciones

(tambien van todas las tares en  #Tareas) 
* Obteniendo información definida de Twitter.
* Establecer una primera interfaz de fácil implementación
* Almacenando datos obtenidos de distintos sitios de internet.
* Si realizo una consulta por un producto A, obtengo ofertas de este producto.
* Mostrando publicidades en la aplicación


#Segunda iteracion
* El usuario se autentifica usando OpenID.
* Un usuario autentificado puede votar por la validez de una oferta.
* Las ofertas mostradas a un usuario autenticado se priorizan usando un mecanismo de confianza. 
faltan

#Tareas

* Diseño conceptual del sistema.
* Realización de WBS.
* Primera revisión del caso de negocio, objetivos y requerimientos.
* Análisis de riesgos.
* Definición y priorización de casos de uso, documentando los tiempos esperados para los casos de uso más prioritarios.
* Definir junto a los stakholder los atributos de calidad del sistema.
* Diseño de la Arquitectura, teniendo en cuenta las restricciones a las tecnologías impuestas por los stakholder.


#Casos de Uso

* Obteniendo informacion de internet
**Descripción**: El sistema colecta la información de los distintos medios, la procesa, y almacena la información obtenida en la base de datos, o algun otro medio. _Solo almaceno productos de rubros habilitados?_.
    + Definición funcional de la información a obtener.
    + Validación de la definición funcional con el stakholder.
    * Obteniendo información definida de Facebook.
        + Investigar conectividad con facebook.
        + Implementar conectividad con facebook.
        + Testeo de la conectividad con facebook.
        + Integración de la conectividad con facebook con el resto del sistema
        + Investigar obtención de datos
        + Implementar obtención de datos
        + Testear obtención de datos
        + Integración de componente
    * Obteniendo información definida de Pinterest.
        + Investigar conectividad con Pinterest.
        + Implementar conectividad con Pinterest.
        + Testeo de la conectividad con Pinterest.
        + Integración de la conectividad con Pinterest con el resto del sistema
        + Investigar obtención de datos
        + Implementar obtención de datos
        + Testear obtención de datos
        + Integración de componente
    * Obteniendo información definida de Twitter.
        + Investigar conectividad con Twitter.
        + Implementar conectividad con Twitter.
        + Testeo de la conectividad con Twitter.
        + Integración de la conectividad con Twitter con el resto del sistema
        + Investigar obtención de datos
        + Implementar obtención de datos
        + Testear obtención de datos
        + Integración de componente
	  * Obteniendo datos de otros sitios web 
        + Definir sitios relevantes para la extracción de datos
        + Investigar las posibilidades de extracción de datos de sitios web
        + Implementación de mecanismos de extracción de datos
        + Integración del mecanismo con sitios de internet de interés
        + Validación del funcionamiento
        + Corrección de errores 
    + Obteniendo información de sms
        + Investigar conectividad
        + Implementar conectividad
        + Testear conectividad 
        + Integración de componente
        + Investigar análisis de datos
        + Implementar análisis de datos
        + Testear análisis de datos
        + Integración de componente

* Se consulta información a travéz de el API publica.
**Descripción**: Es posible realizar consultas al sistema mediante un API Publica (Rest?, XmlRpc?, SOAP?, Varias?, etc...).
    + Definición de los servicios que van a ser provistos por la API
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
**Descripción**: Utilizando una caché, o algo por el estilo, proveer cierta funcionalidad. Una podria ser tener disponible de forma offline un historial con los resultados de busquedas previas. 
    + Definir el nivel de funcionalidad que debe ser provista para el usuario en caso de no tener conexión con el sistema
    + Planificar como esta funcionalidad será lograda
    + Realizar las modificaciones necesarias en el sistema central para lograr la funcionalidad
    + Realizar las modificaciones en la interfaz para lograr la funcionalidad
    + Realizar los tests necesarios para corroborar el funcionamiento de la interfaz en caso de no tener conexión con el sistema

* ABM de rubros habilitados.
* ABM de productos en un rubro.

* Almacenando datos obtenidos de distintos sitios de internet.
**Descripción**: El sistema recorre distintos sitios de internet y consulta distintos servicios obteniendo precios y locaciones para comprar distintos productos y los almacena internamente en el sistema para poder ser accedidos después por los mecanismos que presentan la información a los usuarios de la aplicación.
    + Crear un diseño de BD que se ajuste a las necesidades y requerimientos del sistema
    + Implementar una componente que alimente a la BD con los datos extraido de los obtenedores de datos
    + Realizar tests funcionales
    + Realizar tests de stress
    + Integración de las consultas con el resto del sistema

* Si realizo una consulta por un producto A, obtengo ofertas de este producto.
**Descripción**: Se busca en la base de datos del sistema ofertas que cumplan lo especificado.
    + Definir el tipo de consultas que se van a poder hacer
    + Implementar la componente encargada de hacer las consultas a la BD.
    + Realizar tests funcionales
    + Realizar tests de stress
    + Integración de las consultas con el resto del sistema

* Si realizo una consulta por un producto A y este no esta se le informa al usuario.
* Si realizo una consulta por un producto A, que se sustituye por B, tambien se muestran ofertas de B.
* Si realizo una consulta por un producto A, que se asocia con B, tambien se muestran ofertas de B.

* Se prepara un informe con las estadisticas de ofertas detectadas como falsas.

* Mientras escribo una busqueda, se comienzan a obtener resultados.
* Al ingresar a la pagina, se sugieren ofertas, basado en busquedas anteriores (Relacionado con que hay que obtener resultados cuanto antes, tal vez habria q acordarlo con el PO).

* El usuario se autentifica usando OpenID.
* Un usuario autentificado puede votar por la validez de una oferta.
* Las ofertas mostradas a un usuario autenticado se priorizan usando un mecanismo de confianza. 

* Sistema de ofertas promocionadas (las empresas pagan por que sus productos aparezcan primeros en las busquedas, o resaltados). La meto pq hay que autofinanciarse.

* Mostrando publicidades en la aplicación. 
**Descripción**: Cuando el usuario utiliza la aplicación visualiza, aparte de los resultados de su consulta, propaganda de los spónsores de _twitteando para ahorrar_.
    + Definir el restricciones para el formato de las propagandas de spónsores.
    + Realizar tramites administrativos para el cobro de este servicio.
    + Promocionar el servicio con posibles interesados.
    + Implementar un componente administrador de la presentación de la publicidad de sponsors.
        + Realizar tests funcionales.
    + Integrar a la aplicacion

* Filtrando ofertas falsas mediante nuestro sistema de spam

Referencias
===========

* Caso de uso / tarea
+ Caso de uso / tarea dependiente del caso de uso superior
