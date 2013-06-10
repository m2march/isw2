
###CU1: Obteniendo informacion de internet
**Descripción**: El sistema colecta la información de los distintos medios, la procesa, y la almacena para luego ser provista a los usuarios.  


###CU2: Se consulta información a travéz de el API publica.
**Descripción**: Clientes externos pueden consultar a nuestro sistema por precios que recopilamos de distintos medios a través de un servicio público (API) ofrecido por nuestro sistema.


###CU3: El usuario consulta precios a través de una interfaz amigable
**Descripción**: El usuario accede a una aplicación de celular propia de _twitteando para ahorrar_ a través de la cual puede consultar por precios para distintos productos.


###CU4: Se realizó una consulta por un producto, y el dispositivo sin tener conexión, logra responder la consulta de alguna forma medianamente satisfactoria.
**Descripción**: El usuario accede a la aplicación de celular _twitteando para ahorrar_ sin tener conectividad a internet y recibe precios de los productos deseados y los relacionados a estos. La información provista al usuario podría estar limitada respecto de lo que vería si tuviera conectividad, pero esto no debería ser notado por el mismo. 

###CU5: ABM de rubros habilitados.
**Descripción**: Ciertos usuarios particulares del sistema pueden acceder al mismo para agregar nuevos rubros o modificar o borrar existentes. 

###CU6: ABM de productos en un rubro.
**Descripción**: Ciertos usuarios particulares del sistema pueden acceder al mismo para agregar nuevos productosi o modificar o borrar existentes. También pueden redefinir la pertenencia de un producto a uno o más rubros.

###CU7: Si realizo una consulta por un producto A, obtengo ofertas de este producto.
**Descripción**: El usuario consulta por un producto A dentro de los habilitados en algún rubro y recibe información de donde comprarlo y a qué precio. 

###CU8: Si realizo una consulta por un producto A y este no está se le informa al usuario.
**Descripción**: El usuario consulta por un producto A  que no está habilitado en ningún rubro y es informado que el sistema no posee información sobre donde comprar el mismo.

###CU9: Si realizo una consulta por un producto A, y se considera que puede sustituirse por B, tambien se muestran ofertas de B.
**Descripción**: El usuario consulta por un producto A dentro de los habilitados en algún rubro y se definió que puede sustituirse por el producto B, luego el usuario recibe información de donde comprar A y donde comprar B y a qué precio. 

###CU10: Si realizo una consulta por un producto A, que se considera asociado con B, tambien se muestran ofertas de B.
**Descripción**: El usuario consulta por un producto A dentro de los habilitados en algún rubro y se definió que está asociado con el producto B, luego el usuario recibe información de donde comprar A y donde comprar B y a qué precio. 

###CU11: Si realizo una consulta por un producto A y soy un usuario autentificado, las ofertas recibidas se priorizan acorde a mis preferencias de confianza.
**Descripción**: Dentro de las ofertas relacionadas al producto A que conoce el sistema, se mostrarán primero aquellas cuya fuente yo haya declarado de mayor confianza, luego las de fuentes con menor confianza y no se mostrará ninguna oferta cuya fuente declaré como no confiable.

###CU12: Mostrando publicidades
**Descripción**: Cuando el usuario utiliza la aplicación visualiza, aparte de los resultados de su consulta, propaganda de los spónsores de _twitteando para ahorrar_.

###CU13: Detectando ofertas falsas
**Descripción**: Al recopilar datos de precios en internet, el sistema es capaz de detectar si la información es sospechosa y marcarla como tal, para futura revisión. Además el sistema recopila todas las evidencias encontradas para sospechar de los datos.

###CU14: Siendo martes se publica un informe de ofertas falsas
**Descripción**: Cada martes el sistema arma y publica un informe con los productos sobre los cuales se encontraron precios dudosos junto con la evidencia que genera la sospecha. Este informe debe estar disponible para revisión por usuarios externos selectos. 

###CU15: Se prepara un informe con las estadisticas de ofertas detectadas como falsas.
**Descripción**: Al mismo tiempo que el usuario comienza a ingresar una consulta, la aplicación se anticipa a los deseos del usuario para mostrarle rápidamente precios de productos que podríán responder a la consulta que se está formulando.

###CU16: El usuario se autentica con el sistema 
**Descripción**: El usuario de la aplicación puede utilizar alguna cuenta de un servicio asociado con OpenID (google, yahoo, facebook y otro) para autenticarse en la aplicación. A partir de ese momento la aplicación sabe quién es el usuario y puede utilizar la información que tiene del mismo para proveerle funcionalidades más avanzadas.

###CU17: Un usuario autentificado puede votar por la validez de una oferta.
**Descripción**: Un usuario ya autenticado en el sistema elije una oferta y la marca como válida o inválida. Esto afecta la reputación del usuario o fuente que dio origen a la oferta para facilitar la detección de ofertas sospechosas.

