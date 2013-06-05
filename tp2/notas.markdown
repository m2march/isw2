#Stuff:

* Juntar informacion de distintos lugares (facebook, 	pininterest, paginas de supermercados, sms, páginas de descuentos y subastas)
	* Modulo de obtención de datos
	* Investigar cómo obtener información de sitios fijos (facebook, pininterest, supermercados, páginas de descuentos)
	* Modulos para cada una de las fuentes
	* Investigar y obtener información de sms (¿hay que hablar con companías telefónicas?)
	

* Web mining (relacionado con el punto anterior)
	* Investigar como realizar webmining de sitios más complicados
	* ¿Se trabaja con sitios fijos, o se utiliza *la internes*?

* API para publicar datos
	* Definir que datos se quieren publicar en la API
  * Módulo de publicación de datos
  * Tener en cuenta que debe interfasear con nuestro storage de datos

* Limitación de productos por rubros

* Flexibilidad en los rubros habilitados y sus productos asociados
  * Algún stakeholder desea agregar un nuevo rubro. Debe poder agregarse al sistema de manera simple.
    ¿Es necesario recuperar ofertas viejas para el nuevo rubro solo se toman las que surgan desde el momento en que se define el rubro? 
  * Se decíden agregar un nuevo producto a un rubro, se debe poder registrar información al respecto desde ese momento.
  * Se decide eliminar un producto de un rubro. Los datos de ese producto no deben mostrarse más. ¿Se borran los datos sobre el mismo?

* Hay reglas de asociacion y sustitucion entre productos.
  * Definir correctamente los criterios de _asociacion_ y _sustitución_ de productos. Entender que significa asociación: ¿Dado un producto se muestan ofertas de otro? ¿Cómo se definen cuales o qué tipo de ofertas?
  * Idem para _sustitución_.

* Modificabilidad y flexibilidad de las reglas de asociacion y sustitucion entre productos.

* Anticipacion a las busquedas. (Los resultados aparecen mientras se escribe la busqueda, e inclusive antes (Tira sugerencias usando info previa?))

* Actualizacion de informacion en tiempo real.
  * ¿Implica necesidad de servicios push? ¿O hacemos un sacadísimo polling (guarda que el polling necesita mucho HW)?
  * Implicancias de performance 

* El product owner es caprichoso y quiere NOSQL, y cloud computing, obvio, que escale.
  * ¿Que ondis? Para mi hay que tomarlo con pinzas

* Usar OpenId para autenticarse.
  * Aprender a usar OpenId
  * Módulo de login que se comunique con OpenId
  * ¿Que pasa con la autenticación y el modo offline?

* Desarrollar un sistema de confianza configurable por usuario. (Ultimo parrafo, pagina 1, hay un ejemplo.) 
  * Definir exactamente como funciona el mecanismo de confianza y ejes de cambio presentes en el mismo.

* Mecanismo de reputacion interno entre usuarios.
  * ¿¿Que demonios?? Más definiciones

* Los ultimos 2 puntos DEBEN ESTAR LISTO EN LOS PROXIMOS 2 MESES! ES PUNTO CRITICO.

* Deteccion de ofertas falsas. (Arrancamos con spambust, pero hay limitacion con el tema $$). Hay que desarrollar uno propio, lo antes posible.
  * Meta: definir que hace y no hace spambust.
  * Nuestra implementación substituirá la cajita que dice *SpamBust*
  * Luego de definir que hace spambust hay que saber que es necesario hacer alrededor. Ver además punto siguiente.

* Cada cierto tiempo, entregar un informe de cantidad de ofertas falsas detectadas, etc...

* Muchas compus tobaras, y no un superserver.

* Soporte de la aplicación para funcionar offline. 

* Fácil usabilidad para gran público. Doña rosa.
  * Definir buenas interfases. Conseguir gente que sepa hacer eso.
  * Atributois de calidad relacionados que deben ser cuidadosamente evaluados.`

#Riesgos:

* Desconocimiento de las tecnologías a usar: OpenID, base de datos nosql, webmining, sms, cloud computing, etc.
* Definiciones vagas: criterios de sustitución y asociación, información a recuperar, prioridad de los usuarios por la información
* Para lograr que los datos sean accessibles rápidamente, si tenemos que hacer polling, puede que la cantidad de HW disponible no nos permita acceder a la informacion con la constancia necesaria.
* Por la falta de HW podemos tener problemas para otras tareas pesadas en procesamiento como ser: cálculo de prioridades de los usuarios, verificación de las ofertas conseguidas, mantenmiento de información de auditoría 
* Inconvenientes con el servicio de spambust que nos deja sin esta funcionalidad. (E.g.: sube el precio, problemas de servicio por su parte)
* Falta de dinero para financiar el proyecto.
* El hardware disponible no es suficiente para realizar la extracción de datos de internet de manera suficientemente rápida
* El hardware disponible no es suficiente para soportar TODAS las fucionalidades a cumplir (extraer datos, publicarlos mediante la api, predecir los deseos del usuario, verificar los datos recibidos, generar información de auditoría).
* Falta de testing adecuado en algun modulo / funcionalidad del sistema.
* Un miembro abandona el equipo de trabajo. Una posible forma de mitigar  esta situación es particionando al sistema en 'modulos' simples con una unica responsabilidad y alta cohesion interna, y manteniendo la documentación de la arquitectura del sistema actualizada, de forma que al incorporar un remplazo, la curva de aprendizaje del sistema se vea reducida.
