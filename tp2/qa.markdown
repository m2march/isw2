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


# Restricciones
* No sql
* Cloud computing
* OpenId
* SpamBust
* No hay servidor con redundancia, hay pcs.

# Calidad 
* Extensibilidad de las fuentes de datos (2do párrafo enunciado)
* Modificabilidad de los rubros y productos de rubros (3pe)
* Modificabilidad de las reglas de asociación y sustitución (3pe)
* Performance para velocidad en que se publican las ofertas (4pe)
* Seguridad para evitar usos malintencionados autenticarse con OpenId (6pe)
* Usabilidad sistema de confianza (facilmente?) configurable
* Extensibilidad de los provider de datos del usuario.
* Modificabilidad del servicio de deteccion de spam.
* Auditabilidad para ver la cantidad de ofertas falsas detectadas, productos de precios dudosos, etc.
--------------
* Usabilidad interfaz elegante y entendible para todos los usuarios.
* Disponibilidad que no decaiga, escala nacional y siga funcionando offline.
* Preg: Hay algun atributo para hacer que el sistema entre en funcionamiento facilmente? que este modularizado?
* Auditabilidad del servicio SpamBust





