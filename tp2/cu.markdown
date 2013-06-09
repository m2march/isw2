
* Obteniendo informacion de internet
**Descripción**: El sistema colecta la información de los distintos medios, la procesa, y la almacena para luego ser provista a los usuarios.  


* Se consulta información a travéz de el API publica.
**Descripción**: Clientes externos pueden consultar a nuestro sistema por precios que recopilamos de distintos medios a través de un servicio público (API) ofrecido por nuestro sistema.


* El usuario consulta precios a través de una interfaz amigable
**Descripción**: El usuario accede a una aplicación de celular propia de _twitteando para ahorrar_ a través de la cual puede consultar por precios para distintos productos.


* Se realizó una consulta por un producto, y el dispositivo sin tener conexión, logra responder la consulta de alguna forma medianamente satisfactoria.
**Descripción**: El usuario accede a la aplicación de celular _twitteando para ahorrar_ sin tener conectividad a internet y recibe precios de los productos deseados y los relacionados a estos. La información provista al usuario podría estar limitada respecto de lo que vería si tuviera conectividad, pero esto no debería ser notado por el mismo. 

* ABM de rubros habilitados.
**Descripción**: Ciertos usuarios particulares del sistema pueden acceder al mismo para agregar nuevos rubros o modificar o borrar existentes. 

* ABM de productos en un rubro.
**Descripción**: Ciertos usuarios particulares del sistema pueden acceder al mismo para agregar nuevos productosi o modificar o borrar existentes. También pueden redefinir la pertenencia de un producto a uno o más rubros.

* Si realizo una consulta por un producto A, obtengo ofertas de este producto.
**Descripción**: El usuario consulta por un producto A dentro de los habilitados en algún rubro y recibe información de donde comprarlo y a qué precio. 

* Si realizo una consulta por un producto A y este no está se le informa al usuario.
**Descripción**: El usuario consulta por un producto A  que no está habilitado en ningún rubro y es informado que el sistema no posee información sobre donde comprar el mismo.

* Si realizo una consulta por un producto A, y se considera que puede sustituirse por B, tambien se muestran ofertas de B.
**Descripción**: El usuario consulta por un producto A dentro de los habilitados en algún rubro y se definió que puede sustituirse por el producto B, luego el usuario recibe información de donde comprar A y donde comprar B y a qué precio. 

* Si realizo una consulta por un producto A, que se considera asociado con B, tambien se muestran ofertas de B.
**Descripción**: El usuario consulta por un producto A dentro de los habilitados en algún rubro y se definió que está asociado con el producto B, luego el usuario recibe información de donde comprar A y donde comprar B y a qué precio. 
