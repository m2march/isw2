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
* Extensibilidad de las fuentes de datos (2do párrafo enunciado)
	* Fuente: El equipo de desarrolladores.
	* Estimulo: Se desea implementar una nueva fuente de datos.
	* Artefacto: Sistema de obtención de datos.
	* Entorno: En funcionamiento normal. 
	* Respuesta: Se implementa la fuente de datos y se la integra al sistema.
	* Medida: La fuente de datos se implementa en el tiempo esperado, y se integra con el sistema en menos de 1 hora, sin detenerlo.

* Modificabilidad de los rubros y productos de rubros (3pe)
	* Fuente: Administradores del sistema.
	* Estimulo: Se desea agregar un nuevo producto/rubro.
	* Artefacto: Sistema central TPA.
	* Entorno: Funcionamiento normal.
	* Respuesta: Utilizando la interfaz de administración, se agrega un nuevo producto/rubro al sistema, sin detenerlo.
	* Medida: Se agrega un producto/rubro en menos de 5 minutos.

* Modificabilidad de las reglas de asociación y sustitución (3pe)
	* Fuente: Administradores del sistema
	* Estimulo: Se desea agregar/modificar las reglas de asociación y sustitución.
	* Artefacto: Sistema central TPA.
	* Entorno: Funcionamiento normal.
	* Respuesta: Se modifican las reglas de asociación y sustitución. 
	* Medida: En menos de 24hs se implementan y ponen en funcionamiento las modificaciones a estas reglas.

* Performance para velocidad en que se publican las ofertas (4pe)
	* Fuente: 
	* Estimulo:
	* Artefacto:
	* Entorno:
	* Respuesta:
	* Medida:
* Seguridad para evitar usos malintencionados autenticarse con OpenId (6pe)
	* Fuente: 
	* Estimulo:
	* Artefacto:
	* Entorno:
	* Respuesta:
	* Medida:
* Usabilidad sistema de confianza (facilmente?) configurable
	* Fuente: 
	* Estimulo:
	* Artefacto:
	* Entorno:
	* Respuesta:
	* Medida:
* Extensibilidad de los provider de datos del usuario.
	* Fuente: 
	* Estimulo:
	* Artefacto:
	* Entorno:
	* Respuesta:
	* Medida:
* Modificabilidad del servicio de deteccion de spam.
	* Fuente: 
	* Estimulo:
	* Artefacto:
	* Entorno:
	* Respuesta:
	* Medida:
* Auditabilidad para ver la cantidad de ofertas falsas detectadas, productos de precios dudosos, etc.
	* Fuente: 
	* Estimulo:
	* Artefacto:
	* Entorno:
	* Respuesta:
	* Medida:
--------------
* Usabilidad interfaz elegante y entendible para todos los usuarios.
	* Fuente: 
	* Estimulo:
	* Artefacto:
	* Entorno:
	* Respuesta:
	* Medida:
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





