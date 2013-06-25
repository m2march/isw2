
###CU1: Obteniendo informacion de Internet
**Descripción**: El sistema colecta información sobre ofertas de distintos medios (redes sociales, sitios de información en Internet, SMS), la procesa para extraer los datos relevantes de la oferta, y la almacena para luego ser provista a los usuarios.

###CU2: Almacenando datos obtenidos de distintos sitios de Internet
**Descripción**: El sistema recorre distintos sitios de Internet y consulta distintos servicios obteniendo ofertas, y las almacena internamente en el sistema para poder ser accedidos después por los mecanismos que presentan la información a los usuarios de la aplicación.

###CU3: Se consulta información a través de una API pública
**Descripción**: Clientes externos pueden consultar a nuestro sistema por ofertas almacenadas, a través de un servicio público (API) ofrecido por nosotros.

###CU4: El usuario consulta por un producto determinado
**Descripción**: El usuario consulta por un producto válido A de algún rubro, y recibe como respuesta ofertas que le indican dónde comprarlo y a qué precio.

**Ruta alternativa**: El producto A no es válido; se le informa al usuario que no existe información para dicho producto.

###CU5: El usuario consulta precios a través de una interfaz amigable en su computadora
**Descripción**: El usuario accede a un sitio web propio de _Twitteando para ahorrar_, a través del cual puede consultar por precios para distintos productos.

###CU6: El usuario consulta precios a través de una interfaz amigable en su celular
**Descripción**: El usuario accede a una aplicación de celular propia de _Twitteando para ahorrar_, a través de la cual puede consultar por precios para distintos productos.

###CU7: Se realiza una consulta por un producto desde un dispositivo sin conexión
**Descripción**: El usuario accede a la aplicación de celular _Twitteando para ahorrar_ sin tener conectividad a Internet y realiza una consulta. Como respuesta recibe las ofertas relevantes al producto buscado. La información provista al usuario podría estar limitada respecto de lo que vería si tuviera conectividad, pero debe ser satisfactoria dentro de lo posible. Se le notifica al usuario que está trabajando en un modo "sin conexión".

###CU8: Se anticipa a los deseos del usuario y se muestra informacion preliminar
**Descripción**: Al mismo tiempo que el usuario comienza a ingresar una consulta, la aplicación se anticipa a los deseos del usuario para mostrarle rápidamente precios de productos que podrían responder a la consulta que se está formulando.

###CU9: Se realiza una consulta por un producto sustituible
**Descripción**: El usuario consulta por un producto A dentro de los habilitados en algún rubro y existe una regla de sustitución que indica que A es sustituible por el producto B. Luego el usuario recibe información de ofertas de A y también ofertas de B.

###CU10: Se realiza una consulta por un producto que tiene productos asociados
**Descripción**: El usuario consulta por un producto A dentro de los habilitados en algún rubro y existe una regla de asociación que indica que A se relaciona con el producto B. Luego el usuario recibe información de ofertas de A y también ofertas de B.

###CU11: Mostrando publicidades
**Descripción**: Cuando el usuario utiliza la aplicación, visualiza, además de los resultados de su consulta, propaganda de los sponsors de _Twitteando para ahorrar_.

###CU12: ABM de rubros habilitados
**Descripción**: Los administradores del sistema pueden acceder al mismo para agregar nuevos rubros, o modificar o borrar existentes.

###CU13: ABM de productos en un rubro
**Descripción**: Los administradores del sistema pueden acceder al mismo para agregar nuevos productos, o modificar o borrar existentes. También pueden redefinir la pertenencia de un producto a uno o más rubros.

###CU14: El usuario se autentica con el sistema
**Descripción**: El usuario de la aplicación puede utilizar alguna cuenta de un servicio asociado con OpenID (Google, Yahoo, Facebook y otros) para autenticarse en la aplicación. A partir de ese momento la aplicación sabe quién es el usuario y puede utilizar la información que tiene del mismo para proveerle funcionalidades más avanzadas.

###CU15: Un usuario autenticado modifica sus preferencias de confianza
**Descripción**: El usuario autenticado accede a una sección de preferencias de usuario, y determina sus niveles de confianza para cada tipo de fuente de las ofertas. Los tipos de fuente pueden depender de la información de redes sociales asociada a la cuenta.

###CU16: Un usuario realiza una consulta por un producto determinado estando autenticado
**Descripción**: Las ofertas que devuelve el sistema ante la consulta estarán ordenadas según las prefeencias establecidas por el usuario. Se mostrarán primero aquellas cuya fuente haya declarado como más confiables, luego las de fuentes con menor confianza. No se mostrará ninguna oferta cuya fuente esté declarada como no confiable.

###CU17: Detectando ofertas falsas
**Descripción**: Al recopilar datos de precios en Internet, el sistema es capaz de detectar si la información es sospechosa y marcarla como tal, para futura revisión. Además el sistema recopila todas las evidencias encontradas para sospechar de los datos.

###CU18: Siendo martes se publica un informe de ofertas falsas
**Descripción**: Cada martes el sistema arma y publica un informe con los productos sobre los cuales se encontraron precios dudosos junto con la evidencia que genera la sospecha. Este informe debe estar disponible para revisión por usuarios externos selectos.

###CU19: Un usuario autenticado puede votar por la validez de una oferta
**Descripción**: Un usuario ya autenticado en el sistema elige una oferta y la marca como válida o inválida. Esto afecta la reputación del usuario o fuente que dio origen a la oferta para facilitar la detección de ofertas sospechosas.
