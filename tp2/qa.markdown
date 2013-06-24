# Funcionalidad 
* API de publicación de datos
* Anticiparse a las busquedas - usabilidad
* Autenticacion opcional
* Sistema de confianza configurable
* Mecanismo interno de reputacion de usuarios.
* Saber como conectarse con un provider de datos del usuario (LinkedIn, tarjetas de credito)

-------
* Productos o vendedores destacados (+ABM)
* Eliminar ofertas por algun criterio (?) pero log.
* Bannear usuarios
* Obtener datos de sms
* Obtener datos de redes sociales
* Obtener datos de sitios

----------------
singup openid (?)




# Restricciones
* No sql
* Cloud computing
* OpenId
* SpamBust
* No hay servidor con redundancia, hay pcs.

# Calidad 
* _Extensibilidad_ de las fuentes de datos. (2do párrafo enunciado)
	* Fuente: El equipo de desarrolladores.
	* Estimulo: Se desea implementar una nueva fuente de datos.
	* Artefacto: Sistema de obtención de datos.
	* Entorno: En funcionamiento normal. 
	* Respuesta: Se implementa la fuente de datos y se la integra al sistema.
	* Medida: La fuente de datos se implementa en el tiempo esperado, y se integra con el sistema en menos de 1 hora, sin detenerlo.

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
	* Entorno: Funcionamiento normal.
	* Respuesta: Se modifican las reglas de asociación y sustitución. 
	* Medida: En menos de 24hs se implementan y ponen en funcionamiento las modificaciones a estas reglas.

* _Performance_ para velocidad en que se identifican ofertas de las distintas fuentes de datos. (4pe)
	* Fuente: Usuario externo
	* Estimulo: Se publica en un medio monitoreado por el sistema de obtención de datos una oferta.
	* Artefacto: Sistema de obtención de datos.
	* Entorno: Funcionamiento normal.
	* Respuesta: El sistema de obtención de datos identifica esta oferta y la agrega a la base de datos.
	* Medida: La oferta no se encuentra mas de 1 hora sin ser identificada.

* Seguridad para evitar usos malintencionados autenticarse con OpenId (6pe)
	* Fuente:
	* Estimulo: 
	* Artefacto:
	* Entorno:
	* Respuesta:
	* Medida:

* _Usabilidad_, sistema de confianza facilmente configurable.
	* Fuente: Usuario autentificado.
	* Estimulo: Modifica las reglas de confianza de ofertas.
	* Artefacto: Sistema central TPA.
	* Entorno: Funcionamiento normal.
	* Respuesta: Se modifican las reglas de confianza de ofertas.
	* Medida: El sistema provee una guia de configuración de confianza de ofertas, que ayuda a completar dicha tarea en menos de 15 minutos para un usuario nuevo.

* Extensibilidad de las provider de datos del usuario.
	* Fuente: 
	* Estimulo:
	* Artefacto:
	* Entorno:
	* Respuesta:
	* Medida:

* Modificabilidad del servicio de deteccion de spam.
	* Fuente: Equipo de desarrollo.
	* Estimulo: Se desea modificar el funcionamiento del servicio de detección de Spam.
	* Artefacto: Sistema de detección de Spam.
	* Entorno: Funcionamiento normal.
	* Respuesta: Se modifica el funcionamiento del servicio.
	* Medida: El funcionamiento del servicio de detección de Spam debe poder modificarse (Cambio de proveedor, nuevo proveedor, etc...) con el sistema en funcionamiento Normal, y deberia ser posible que mas de un sistema de detección de Spam puedan co-existir.

* Auditabilidad para ver la cantidad de ofertas falsas detectadas, productos de precios dudosos, etc.
	* Fuente: Administradores del sistema.
	* Estimulo: Se desea ver el resumen de ofertas falsas, detectadas, etc...
	* Artefacto: Sistema de detección de Spam.
	* Entorno: Funcionamiento normal.
	* Respuesta: Se obtiene un resumen con la información de ofertas falsas detectadas, precios dudosos, etc...
	* Medida: 

--------------
* Usabilidad de la interfaz del sistema para realizar consultas.
	* Fuente: Un usuario nuevo.
	* Estimulo: El usuario desea realizar una consulta.
	* Artefacto: Interfaz Movil / Interfaz Web.
	* Entorno: Funcionamiento normal.
	* Respuesta: Se realiza la consulta y se informa de los resultados a los usuarios.
	* Medida: En menos de 5 minutos, un usuario nuevo comprende la interfaz y comienza a utilizarla .

* Disponibilidad que no decaiga, escala nacional y siga funcionando offline.
	* Fuente: 
	* Estimulo:
	* Artefacto:
	* Entorno:
	* Respuesta:
	* Medida:
* Preg: Hay algun atributo para hacer que el sistema entre en funcionamiento facilmente? que este modularizado?
	* Fuente: 
	* Estimulo:
	* Artefacto:
	* Entorno:
	* Respuesta:
	* Medida:
* Auditabilidad del servicio SpamBust
	* Fuente: 
	* Estimulo:
	* Artefacto:
	* Entorno:
	* Respuesta:
	* Medida:





