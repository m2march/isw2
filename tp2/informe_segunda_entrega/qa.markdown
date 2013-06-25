* _Extensibilidad_ de las fuentes de datos. (2do párrafo enunciado)
	* Fuente: El equipo de desarrolladores.
	* Estimulo: Se desea implementar una nueva fuente de datos.
	* Artefacto: Sistema de obtención de datos.
	* Entorno: En funcionamiento normal. 
	* Respuesta: Se implementa la fuente de datos y se la integra al sistema.
	* Medida: La fuente de datos se integra con el sistema en menos de 1 hora, sin detener al sistema.

* _Modificabilidad_ de los bots que obtienen datos.
	* Fuente: El equipo de desarrolladores.
	* Estimulo: Se desea implementar/modificar/eliminar un bot para obtener datos de una pagina web determinada.
	* Artefacto: Sistema de obtención de datos.
	* Entorno: En funcionamiento normal. 
	* Respuesta: Se implementa el bot y se integra con el sistema.
	* Medida: el bot se implementa o modifica en menos de 25 horas y se integra con el sistema en menos de 1 hora, sin detener al sistema.

* _Detección de fallas_ en la información obtenida por los bots.
	* Fuente: Las paginas monitoreadas.
	* Estimulo: Se produce un cambio en la estructura de las paginas monitoreadas.
	* Artefacto: Bot del sistema de obtención de datos.
	* Entorno: En funcionamiento normal. 
	* Respuesta: Se detecta el cambio en la estructura de la pagina, se detiene el bot, y se informa a los administradores.
	* Medida: Cuando de una serie de consultas, se detecta un 70% de cambios en su estructura, se considera como error.

* _Modificabilidad_ de los rubros y productos de rubros. (3pe)
	* Fuente: Administradores del sistema.
	* Estimulo: Se desea agregar un nuevo producto/rubro.
	* Artefacto: Sistema central TPA.
	* Entorno: Funcionamiento normal.
	* Respuesta: Utilizando la interfaz de administración, se agrega un nuevo producto/rubro al sistema, sin detenerlo.
	* Medida: Se agrega un producto/rubro en menos de 5 minutos.

* _Modificabilidad_ de las reglas de asociación y sustitución. (3pe)
	* Fuente: Administradores del sistema
	* Estimulo: Se desea agregar/modificar las reglas de asociación y sustitución.
	* Artefacto: Sistema central TPA.
	* Entorno: Modo de mantenimiento.
	* Respuesta: Se modifican las reglas de asociación y sustitución. 
	* Medida: En menos de 24hs se implementan y ponen en funcionamiento las modificaciones a estas reglas.

* _Performance_ para velocidad en que se identifican ofertas de las distintas fuentes de datos. (4pe)
	* Fuente: Usuario externo
	* Estimulo: Se publica en un medio monitoreado por el sistema de obtención de datos una oferta.
	* Artefacto: Sistema de obtención de datos.
	* Entorno: Funcionamiento normal.
	* Respuesta: El sistema de obtención de datos identifica esta oferta y la agrega a la base de datos.
	* Medida: La oferta se comienza a tener en cuenta 10 segundos despues de que fue publicada por una fuente de datos.

* _Usabilidad_, sistema de confianza facilmente configurable.
	* Fuente: Usuario autentificado.
	* Estimulo: Modifica las reglas de confianza de ofertas.
	* Artefacto: Sistema central TPA.
	* Entorno: Funcionamiento normal.
	* Respuesta: Se modifican las reglas de confianza de ofertas.
	* Medida: El sistema provee una guia de configuración de confianza de ofertas, que ayuda a completar dicha tarea en menos de 15 minutos para un usuario nuevo.

* _Extensibilidad_ de las fuentes de confianza de datos del usuario.
	* Fuente: Equipo de desarrollo.
	* Estimulo: Se desea agregar una nueva fuente de confianza de datos del usuario.
	* Artefacto: Sistema central TPA.
	* Entorno: Modo de mantenimiento.
	* Respuesta: Se agrega la fuente de confianza de datos al sistema. 
	* Medida: La fuente de confianza se implementa en menos de 25hs y se integra al sistema en menos de 1 hora.

* _Modificabilidad_ del servicio de deteccion de spam.
	* Fuente: Equipo de desarrollo.
	* Estimulo: Se desea modificar el funcionamiento del servicio de detección de Spam.
	* Artefacto: Sistema de detección de Spam.
	* Entorno: Funcionamiento normal.
	* Respuesta: Se modifica el funcionamiento del servicio.
	* Medida: El funcionamiento del servicio de detección de Spam debe poder modificarse (Cambio de proveedor, nuevo proveedor, etc...) con el sistema en funcionamiento Normal, y deberia ser posible que mas de un sistema de detección de Spam puedan co-existir.

* _Auditabilidad_ para ver la cantidad de ofertas falsas detectadas, productos de precios dudosos, etc.
	* Fuente: Administradores del sistema.
	* Estimulo: Se desea ver el resumen de ofertas falsas, detectadas, etc...
	* Artefacto: Sistema de detección de Spam.
	* Entorno: Funcionamiento normal.
	* Respuesta: Se obtiene un resumen con la información de ofertas falsas detectadas, precios dudosos, etc...
	* Medida: Cada vez que se elimina / modifica una oferta se registra 'quien, cuando, por que (precio dudoso, oferta falsa, etc...), y la oferta'.

* _Usabilidad_ de la interfaz del sistema para realizar consultas.
	* Fuente: Un usuario nuevo.
	* Estimulo: El usuario desea realizar una consulta.
	* Artefacto: Interfaz Movil / Interfaz Web.
	* Entorno: Funcionamiento normal.
	* Respuesta: Se realiza la consulta y se informa de los resultados a los usuarios.
	* Medida: En menos de 5 minutos, un usuario nuevo comprende la interfaz y comienza a utilizarla .

* _Usabilidad_ de la interfaz del sistema mientras se realizan consultas.
	* Fuente: Un usuario.
	* Estimulo: El usuario desea realizar una consulta.
	* Artefacto: Interfaz Movil / Interfaz Web.
	* Entorno: Funcionamiento normal.
	* Respuesta: Conforme se escribe la respuesta, se muestran resultados.
	* Medida: En menos de 1 segundo luego de que se comenzo a tipear una consulta, el sistema comienza a sugerir posibles resultados.

* _Usabilidad_ de la interfaz del sistema, antes de realizar consultas.
	* Fuente: Un usuario.
	* Estimulo: Se accede a la interfaz y aun no se realiza ningun tipo de consulta.
	* Artefacto: Interfaz Movil / Interfaz Web.
	* Entorno: Funcionamiento normal.
	* Respuesta: Se comienzan a presentar resultados.
	* Medida: Se muestran las ofertas populares / mas buscadas / mas recomendadas.


* _Disponibilidad_ del servicio.
	* Fuente: Usuario.
	* Estimulo: Se desea realizar una consulta.
	* Artefacto: Interfaz movil.
	* Entorno: Funcionamiento normal.
	* Respuesta: Se realiza la consulta al sistema, se obtienen resultados y son mostrados al usuario.
	* Medida: En el 99% de los casos la consulta se realiza con exito al sistema central.

* _Disponibilidad_ del servicio cuando no hay conección.
	* Fuente: Usuario.
	* Estimulo: Se desea realizar una consulta.
	* Artefacto: Interfaz movil.
	* Entorno: Funcionamiento sin conección
	* Respuesta: Si la consulta se encuentra disponible sin conección, se obtienen los resultados y son mostrados al usuario.
	* Medida: Las ultimas consultas y las consultas mas populares al momento de la ultima conección se encuentran disponibles.
