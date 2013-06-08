###Riesgo1:
* **Descripción**: Desconocimiento de las tecnologías a usar: OpenID, base de datos nosql, webmining, sms, cloud computing, etc. que podría llegar a ocasionar retrasos inesperados en el proyecto.
* **Probabilidad**: Media
* **impacto**: Bajo
* **Exposición**: Baja
* **Mitigación**: Dedicar horas de aprendizaje, lo antes posible, para cada tecnología y saber de antemano los problemas que podrían suceder.
* **Plan de contingencia**: Contratar gente especializada en las tecnologías.

###Riesgo2:
* **Descripción**: Definiciones vagas: criterios de sustitución y asociación, información a recuperar, prioridad de los usuarios por la información.
* **Probabilidad**: Alta
* **impacto**: Alto
* **Exposición**: Alta
* **Mitigación**: Acordar fechas límites para la presentación de documentación definiendo mejor cada caso en particular.
* **Plan de contingencia**: ??

###Riesgo3:
* **Descripción**: Inconvenientes con el servicio de spambust que nos deja sin esta funcionalidad. (E.g.: sube el precio, problemas de servicio por su parte).
* **Probabilidad**: Baja
* **impacto**: Alto
* **Exposición**: Media
* **Mitigación**: Implementar, lo antes posible, un servicio propio que remplace el de spambust.
* **Plan de contingencia**: Dejar de detectar el spam o detectarlo en menor medida con una implementación fácil y rápida pero no tan efectiva.

###Riesgo4:
* **Descripción**: Falta de dinero para financiar el proyecto.
* **Probabilidad**: Media
* **impacto**: Alto
* **Exposición**: Alta
* **Mitigación**: Conseguir sponsor, lo antes posibles, para que el proyecto sea auto-sostenible.
* **Plan de contingencia**: Resignar funcionalidades del proyecto que requiera mucha inversión para reducir los costos.

###Riesgo5:
* **Descripción**: El hardware disponible no es suficiente para soportar TODAS las funcionalidades a cumplir (extraer datos, publicarlos mediante la api, predecir los deseos del usuario, verificar los datos recibidos, generar información de auditoría).
* **Probabilidad**: Media
* **impacto**: Alto
* **Exposición**: Alta
* **Mitigación**: Mas HW, mejores algoritmos.
* **Plan de contingencia**: Resignar alguna de las funcionalidades.

###Riesgo6:
* **Descripción**: Un miembro abandona el equipo de trabajo.
* **Probabilidad**: Media
* **impacto**: Medio
* **Exposición**: Media
* **Mitigación**: Particionado al sistema en 'modulos' simples con una única responsabilidad y alta cohesión interna, y manteniendo la documentación de la arquitectura del sistema actualizada, de forma que al incorporar un remplazo, la curva de aprendizaje del sistema se vea reducida.
* **Plan de contingencia**: Contratar remplazo.

###Riesgo7:
* **Descripción**: Debido a los tiempos acotados requerido para sacar al mercado el producto, los modulos podrian carecer del testing adecuado.
* **Probabilidad**: Media
* **impacto**: Bajo
* **Exposición**: Baja
* **Mitigación**: Mantener un minimo nivel de testing requerido en cada modulo.
* **Plan de contingencia**: Reparar bugs y mejorar los test del modulo.


* Falta de testing adecuado en algún modulo / funcionalidad del sistema.
