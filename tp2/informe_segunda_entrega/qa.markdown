En esta sección se presentan los distintos _atributos de calidad_ que fueron obtenidos de analizar el documento original con las especificaciones de los interesados y los resultados del QAW (_Quality Assurance Workshop_).

###Atributo de **modificabilidad**:  
Se trabajará con todo tipo de productos, clasificados en rubros. Se espera que a futuro se pueda incrementar la cantidad de rubros existentes, y también controlar el conjunto de productos válidos y la pertenencia de cada uno a determinados rubros.

* Fuente: Administradores del sistema.
* Estimulo: Se desea agregar un nuevo producto/rubro.
* Artefacto: Subsistema de rubros y productos.
* Entorno: Funcionamiento normal.
* Respuesta: Utilizando la interfaz de administración, se agrega un nuevo producto/rubro al sistema, sin detener su funcionamiento.
* Medida: El administrador puede acceder mediante una interfas apropiada al sistema y realizar los cambios sin que sea necesario cambiar el código fuente del sistema.

###Atributo de **modificabilidad**:  
Las reglas de asociación y sustitución entre productos todavía no están bien definidas, por lo que se anticipa que deberán cambiarse con frecuencia.

* Fuente: Administradores del sistema
* Estimulo: Se desea agregar/modificar las reglas de asociación y sustitución.
* Artefacto: Sistema central TPA.
* Entorno: Modo de mantenimiento.
* Respuesta: Se modifican las reglas de asociación y sustitución.
* Medida: En menos de 5 horas de trabajo se implementan y ponen en funcionamiento las modificaciones a estas reglas.

###Atributo de **usabilidad**:  
Se desarrollará un sistema de confianza configurable individualmente, el cual será fácil de operar por un usuario común.

* Fuente: Usuario autenticado.
* Estimulo: Modifica las reglas de confianza de ofertas.
* Artefacto: Sistema central TPA.
* Entorno: Funcionamiento normal.
* Respuesta: El sistema provee un asistente de configuración de confianza de ofertas, que ayuda a modificar dichas preferencias.
* Medida: Un usuario nuevo del sistema logra completar la tarea en menos de 15 minutos.

###Atributo de **extensibilidad**:  
 Un usuario puede confiar en distinta medida en sus contactos de redes sociales, en sus promociones de tarjetas de crédito, en usuarios anónimos, y otros tipos de fuentes de ofertas. A futuro pueden agregarse nuevos tipos de fuentes.

* Fuente: Equipo de desarrollo.
* Estimulo: Se desea agregar una configuración de confianza del usuario para una nueva fuente de ofertas.
* Artefacto: Sistema central TPA.
* Entorno: Modo de mantenimiento.
* Respuesta: Se agrega la configuración de confianza de datos al sistema.
* Medida: La configuración de confianza se implementa en menos de 5 horas de trabajo y se integra al sistema en menos de 1 hora.

###Atributo de **usabilidad**:  
Se desea que la interfaz de la aplicación para realizar consultas sea intuitiva y amigable.

* Fuente: Un usuario nuevo.
* Estimulo: El usuario desea realizar una consulta.
* Artefacto: Interfaz Móvil / Interfaz Web.
* Entorno: Funcionamiento normal.
* Respuesta: Se realiza la consulta y se informan los resultados.
* Medida: En menos de 5 minutos, un usuario nuevo comprende la interfaz y puede comenzar a utilizarla.

###Atributo de **usabilidad**:  
Una característica que se espera de sistema será su inmediata respuesta y su capacidad de anticiparse a nuestras búsquedas. Los resultados deben aparecer a medida que ingresamos una búsqueda.

* Fuente: Un usuario.
* Estimulo: El usuario desea realizar una consulta.
* Artefacto: Interfaz Movil / Interfaz Web.
* Entorno: Funcionamiento normal.
* Respuesta: Se comienzan a presentar resultados, que son las ofertas populares / más buscadas / más recomendadas.
* Medida: En menos de 1 segundo luego de que se comenzo a escribir una consulta, el sistema comienza a sugerir posibles resultados.

###Atributo de **disponibilidad**:  
El servicio debe estar disponible en todo momento, y no debe caerse, en la medida de lo posible.  

* Fuente: Usuario.
* Estimulo: Se desea realizar una consulta.
* Artefacto: Interfaz móvil.
* Entorno: Funcionamiento normal.
* Respuesta: Se realiza la consulta al sistema, se obtienen resultados y son mostrados al usuario.
* Medida: Siempre que el usuario disponga de conexión, en el 99% de los casos el envío de la consulta al sistema central y la recepción de la respuesta se realizan con éxito.

###Atributo de **disponibilidad**:  
Cuando el usuario no tenga conexión a Internet, debe poder consultar a la aplicación de todos modos, y recibir una respuesta satisfactoria.

* Fuente: Usuario.
* Estimulo: Se desea realizar una consulta.
* Artefacto: Interfaz móvil.
* Entorno: El dispositivo móvil no tiene conexión.
* Respuesta: Si la consulta se encuentra disponible sin conexión, se obtienen los resultados y son mostrados al usuario.
* Medida: Las últimas consultas y las consultas más populares al momento de la última conexión se encuentran disponibles.

###Atributo de **modificabilidad**:  
Se contratará temporariamente el oneroso servicio de la empresa SpamBust, mientras se pone a punto una implementación propia. La transición entre los servicios debe ser simple y transparente, y estos deben poder coexistir en caso de que sea necesario.

* Fuente: Equipo de desarrollo.
* Estimulo: Se desea modificar el funcionamiento del servicio de detección de Spam.
* Artefacto: Sistema de detección de Spam.
* Entorno: Funcionamiento normal.
* Respuesta: Se modifica el funcionamiento del servicio.
* Medida: El funcionamiento del servicio de detección de Spam debe poder modificarse (cambio de proveedor, nuevo proveedor, modificar un servicio existente, etc...) con el sistema en funcionamiento, y deberían poder co-existir varios sistemas de detección de Spam.

###Atributo de **auditabilidad**:  
Cada martes debe publicarse un informe con la cantidad de ofertas falsas detectadas, productos con precios dudosos, información contradictoria y alertas de engaños reportados por los usuarios. La información completa que lleve a la conclusión de que un precio es falso tendrá que quedar disponible para una evaluación posterior más minuciosa.

* Fuente: Administradores del sistema.
* Estimulo: Se desea ver el resumen de ofertas falsas, detectadas, etc...
* Artefacto: Sistema de detección de Spam.
* Entorno: Funcionamiento normal.
* Respuesta: Se obtiene un resumen con la información de ofertas falsas detectadas, precios dudosos, etc...
* Medida: Cada vez que se elimina / modifica una oferta se registra _qué oferta, por quién, cuándo, por qué motivo_.

###Atributo de **extensibilidad**:  
El sistema obtendrá datos de diversas fuentes, que incluyen redes sociales, SMS y sitios web. En el futuro se podrán agregar nuevas fuentes de datos, ya sean similares a las anteriores o diferentes.

* Fuente: El equipo de desarrolladores.
* Estimulo: Se desea implementar una nueva fuente de datos.
* Artefacto: Sistema de obtención de datos.
* Entorno: En funcionamiento normal.
* Respuesta: Se implementa la fuente de datos y se la integra al sistema.
* Medida: La fuente de datos se integra con el sistema en menos de 1 hora, sin detener al sistema.

###Atributo de **performance**:  
La actualización de precios debe realizarse en el instante mismo en que se publica la información.

* Fuente: Usuario externo
* Estimulo: Se publica una oferta en un medio monitoreado por el sistema de obtención de datos.
* Artefacto: Sistema de obtención de datos.
* Entorno: Funcionamiento normal.
* Respuesta: El sistema de obtención de datos identifica esta oferta y la agrega a la base de datos.
* Medida: La oferta se comienza a tener en cuenta como máximo un minuto despues de que fue publicada por una fuente de datos. Es importante destacar que existe cierto tiempo desde que un usuario publica una oferta en un medio hasta que este medio la hace disponible; este tiempo no es controlable.

###Atributo de **modificabilidad**:  
El sistema será capaz de minar la web en busca de ofertas en las páginas de las grandes cadenas de supermercados, sitios de descuento y páginas de subastas. A futuro se podrá decidir que se incorporen nuevas páginas a esta búsqueda.

* Fuente: El equipo de desarrolladores.
* Estimulo: Se desea _implementar/modificar_ un bot para obtener datos de una página web determinada.
* Artefacto: Sistema de obtención de datos.
* Entorno: En funcionamiento normal.
* Respuesta: Se implementa el bot y se integra con el sistema.
* Medida: Implementar o modificar el bot modifica un único componente (el respectivo al bot) y se integra con el sistema en menos de 1 hora, sin detener al sistema.

###Atributo de **detección y prevención de fallas**:  
Si la estructura de un sitio web monitoreado por un bot cambia de manera que la información no puede ser interpretada, se deberá ajustar el bot para que pueda continuar funcionando correctamente.

* Fuente: Las páginas monitoreadas.
* Estimulo: Se produce un cambio en la estructura de las páginas monitoreadas.
* Artefacto: Bot del sistema de obtención de datos.
* Entorno: En funcionamiento normal.
* Respuesta: Se detecta el cambio en la estructura de la página, se detiene el bot, y se informa a los administradores.
* Medida: Cuando en una serie de consultas se detecta un 70% de cambios en su estructura, se considera como error, se informa de esta situación y el bot se detiene.
