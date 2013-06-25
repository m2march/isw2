En esta sección se presentan los distintos _atributos de calidad_ que fueron obtenidos de analizar el documento original con las especificaciones de los interesados y la _quality assurance workshop_.

* **Modificabilidad** de los _rubros_ y _productos_ de rubros.
	* Fuente: Administradores del sistema.
	* Estimulo: Se desea agregar un nuevo producto/rubro.
	* Artefacto: Sistema central TPA.
	* Entorno: Funcionamiento normal.
	* Respuesta: Utilizando la interfaz de administración, se agrega un nuevo producto/rubro al sistema, sin detenerlo.
	* Medida: La interfaz para agregar productos/rubros es lo suficientemente intuitiva como para poder agregar un producto/rubro en menos de 5 minutos.

* **Modificabilidad** de las reglas de _asociación_ y _sustitución_.
	* Fuente: Administradores del sistema
	* Estimulo: Se desea agregar/modificar las reglas de asociación y sustitución.
	* Artefacto: Sistema central TPA.
	* Entorno: Modo de mantenimiento.
	* Respuesta: Se modifican las reglas de asociación y sustitución. 
	* Medida: En menos de 5 horas de trabajo se implementan y ponen en funcionamiento las modificaciones a estas reglas.

* **Usabilidad** sistema de confianza facilmente configurable.
	* Fuente: Usuario autentificado.
	* Estimulo: Modifica las reglas de confianza de ofertas.
	* Artefacto: Sistema central TPA.
	* Entorno: Funcionamiento normal.
	* Respuesta: Se modifican las reglas de confianza de ofertas.
	* Medida: El sistema provee un asistente de configuración de confianza de ofertas, que ayuda a completar dicha tarea en menos de 15 minutos para un usuario nuevo.

* **Extensibilidad** de las fuentes de confianza de datos del usuario.
	* Fuente: Equipo de desarrollo.
	* Estimulo: Se desea agregar una nueva fuente de confianza de datos del usuario.
	* Artefacto: Sistema central TPA.
	* Entorno: Modo de mantenimiento.
	* Respuesta: Se agrega la fuente de confianza de datos al sistema. 
	* Medida: La fuente de confianza se implementa en menos de 5 horas de trabajo y se integra al sistema en menos de 1 hora.

* **Usabilidad** de la interfaz del sistema para realizar consultas.
	* Fuente: Un usuario nuevo.
	* Estimulo: El usuario desea realizar una consulta.
	* Artefacto: Interfaz Movil / Interfaz Web.
	* Entorno: Funcionamiento normal.
	* Respuesta: Se realiza la consulta y se informan los resultados.
	* Medida: En menos de 5 minutos, un usuario nuevo comprende la interfaz y puede comenzar a utilizarla .

* **Usabilidad** de la interfaz del sistema mientras se realizan consultas.
	* Fuente: Un usuario.
	* Estimulo: El usuario desea realizar una consulta.
	* Artefacto: Interfaz Movil / Interfaz Web.
	* Entorno: Funcionamiento normal.
	* Respuesta: Conforme se escribe la respuesta, se muestran resultados.
	* Medida: En menos de 1 segundo luego de que se comenzo a escribir una consulta, el sistema comienza a sugerir posibles resultados.

* **Usabilidad** de la interfaz del sistema, antes de realizar consultas.
	* Fuente: Un usuario.
	* Estimulo: Se accede a la interfaz y aun no se realiza ningun tipo de consulta.
	* Artefacto: Interfaz Movil / Interfaz Web.
	* Entorno: Funcionamiento normal.
	* Respuesta: Se comienzan a presentar resultados.
	* Medida: Se muestran las ofertas populares / mas buscadas / mas recomendadas.

* **Disponibilidad** del servicio.
	* Fuente: Usuario.
	* Estimulo: Se desea realizar una consulta.
	* Artefacto: Interfaz movil.
	* Entorno: Funcionamiento normal.
	* Respuesta: Se realiza la consulta al sistema, se obtienen resultados y son mostrados al usuario.
	* Medida: Siempre que el usuario disponga de conexión, en el 99% de los casos la consulta se realiza con exito al sistema central.

* **Disponibilidad** del servicio cuando no hay conexión.
	* Fuente: Usuario.
	* Estimulo: Se desea realizar una consulta.
	* Artefacto: Interfaz movil.
	* Entorno: Funcionamiento sin conexión.
	* Respuesta: Si la consulta se encuentra disponible sin conexión, se obtienen los resultados y son mostrados al usuario.
	* Medida: Las ultimas consultas y las consultas mas populares al momento de la ultima conexión se encuentran disponibles.

* **Modificabilidad** del servicio de deteccion de spam.
	* Fuente: Equipo de desarrollo.
	* Estimulo: Se desea modificar el funcionamiento del servicio de detección de Spam.
	* Artefacto: Sistema de detección de Spam.
	* Entorno: Funcionamiento normal.
	* Respuesta: Se modifica el funcionamiento del servicio.
	* Medida: El funcionamiento del servicio de detección de Spam debe poder modificarse (Cambio de proveedor, nuevo proveedor, modificar un servicio existente, etc...) con el sistema en funcionamiento, y deberian poder co-existir mas de un sistema de detección de Spam.

* **Auditabilidad** para conocer, los Martes, la cantidad de ofertas falsas detectadas, productos de precios dudosos, etc...
	* Fuente: Administradores del sistema.
	* Estimulo: Se desea ver el resumen de ofertas falsas, detectadas, etc...
	* Artefacto: Sistema de detección de Spam.
	* Entorno: Funcionamiento normal.
	* Respuesta: Se obtiene un resumen con la información de ofertas falsas detectadas, precios dudosos, etc...
	* Medida: Cada vez que se elimina / modifica una oferta se registra _'quien, cuando, por que (precio dudoso, oferta falsa, etc...), y la oferta'_.

* **Extensibilidad** de las fuentes de datos.
	* Fuente: El equipo de desarrolladores.
	* Estimulo: Se desea implementar una nueva fuente de datos.
	* Artefacto: Sistema de obtención de datos.
	* Entorno: En funcionamiento normal. 
	* Respuesta: Se implementa la fuente de datos y se la integra al sistema.
	* Medida: La fuente de datos se integra con el sistema en menos de 1 hora, sin detener al sistema.

* **Performance** del tiempo que toma identificar una oferta desde su publicación en las distintas fuentes de datos.
	* Fuente: Usuario externo
	* Estimulo: Se publica en un medio, monitoreado por el sistema de obtención de datos, una oferta.
	* Artefacto: Sistema de obtención de datos.
	* Entorno: Funcionamiento normal.
	* Respuesta: El sistema de obtención de datos identifica esta oferta y la agrega a la base de datos.
	* Medida: La oferta se comienza a tener en cuenta como maximo en 1 minuto, despues de que fue publicada por una fuente de datos. Es importante destacar que existe cierto tiempo desde que un usuario publica una oferta en un medio, hasta que este medio la hace disponible, este tiempo no es controlable.

* **Modificabilidad** de los bots que obtienen datos de paginas web.
	* Fuente: El equipo de desarrolladores.
	* Estimulo: Se desea _implementar/modificar/eliminar_ un bot para obtener datos de una pagina web determinada.
	* Artefacto: Sistema de obtención de datos.
	* Entorno: En funcionamiento normal. 
	* Respuesta: Se implementa el bot y se integra con el sistema.
	* Medida: El bot se implementa o modifica en menos de 10 horas y se integra con el sistema en menos de 1 hora, sin detener al sistema.

* **Detección y prevención de fallas** en la información obtenida por los bots que obtienen datos de paginas web.
	* Fuente: Las paginas monitoreadas.
	* Estimulo: Se produce un cambio en la estructura de las paginas monitoreadas.
	* Artefacto: Bot del sistema de obtención de datos.
	* Entorno: En funcionamiento normal. 
	* Respuesta: Se detecta el cambio en la estructura de la pagina, se detiene el bot, y se informa a los administradores.
	* Medida: Cuando en una serie de consultas se detecta un 70% de cambios en su estructura, se considera como error, se informa de esta situación y el bot se detiene.
