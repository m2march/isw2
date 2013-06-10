###Riesgo1:
* **Descripción**: Por falta de definiciones claras y consisas el código desarrollado no cumple con las expectativas de los stakeholders y se vuelve necesario modificarlo. Se consideran particularmente riesgosas las definiciones en: criterios de sustitución y asociación, información a recuperar, prioridad de los usuarios por la información.
* **Probabilidad**: Alta
* **Impacto**: Alto
* **Exposición**: Alta
* **Mitigación**: Acordar fechas límites para la presentación de documentación definiendo mejor cada caso en particular. Se aislarán y se implementarán los modulos correspondientes a estas caracteristicas de forma que su modificación resulte lo mas rapida posible. (Modificabilidad)
* **Plan de contingencia**: Se estiran los períodos del proyecto para poder realizar las modificaciones necesarias. 

###Riesgo2:
* **Descripción**: Falta de dinero para financiar el proyecto.
* **Probabilidad**: Media
* **Impacto**: Alto
* **Exposición**: Alta
* **Mitigación**: Conseguir sponsor, lo antes posibles, para que el proyecto sea auto-sostenible.
* **Plan de contingencia**: Resignar funcionalidades del proyecto que requiera mucha inversión para reducir los costos.

###Riesgo3:
* **Descripción**: El hardware disponible no es suficiente para soportar TODAS las funcionalidades a cumplir (extraer datos, publicarlos mediante la api, predecir los deseos del usuario, verificar los datos recibidos, generar información de auditoría).
* **Probabilidad**: Media
* **Impacto**: Alto
* **Exposición**: Alta
* **Mitigación**: Aprender a utilizar correctamente los recursos a nuestro alcance, en este caso los equipos de escritorio. Entrenar a los desarrolladores en técnicas de cómputo paralelo.
* **Plan de contingencia**: Resignar alguna de las funcionalidades.

###Riesgo4:
* **Descripción**: Inconvenientes con el servicio de spambust que nos deja sin esta funcionalidad. (E.g.: sube el precio, problemas de servicio por su parte).
* **Probabilidad**: Baja
* **Impacto**: Alto
* **Exposición**: Media
* **Mitigación**: Implementar, lo antes posible, un servicio propio que remplace el de spambust.
* **Plan de contingencia**: Dejar de detectar el spam o detectarlo en menor medida con una implementación fácil y rápida pero no tan efectiva.

###Riesgo5:
* **Descripción**: Un miembro abandona el equipo de trabajo.
* **Probabilidad**: Media
* **Impacto**: Medio
* **Exposición**: Media
* **Mitigación**: Particionado al sistema en 'modulos' simples con una única responsabilidad y alta cohesión interna, y manteniendo la documentación de la arquitectura del sistema actualizada, de forma que al incorporar un remplazo, la curva de aprendizaje del sistema se vea reducida.
* **Plan de contingencia**: Contratar remplazo.

###Riesgo6:
* **Descripción**: Los deseos del usuario sobre la aplicación no son los esperados por los stakeholders y es necesario cambiar drásticamente la funcionalidad.
* **Probabilidad**: Media
* **Impacto**: Media
* **Exposición**: Media
* **Mitigación**: Tener una versión beta de la aplicación de usuario para tener feedback lo antes posible y poder agregar las modificaciones de forma suave y sin desperdiciar tiempo de trabajo.
* **Plan de contingencia**: Hacer estudios de marketing para comprender realmente las necesidades del usuario.

###Riesgo7:
* **Descripción**: Desconocimiento de las tecnologías a usar: OpenID, base de datos nosql, webmining, sms, cloud computing, etc. que podría llegar a ocasionar retrasos inesperados en el proyecto.
* **Probabilidad**: Media
* **Impacto**: Bajo
* **Exposición**: Baja
* **Mitigación**: Dedicar horas de aprendizaje, lo antes posible, para cada tecnología y saber de antemano los problemas que podrían suceder.
* **Plan de contingencia**: Contratar gente especializada en las tecnologías.

###Riesgo8:
* **Descripción**: Debido a los tiempos acotados requerido para sacar al mercado el producto, los módulos podrían carecer del testing adecuado.
* **Probabilidad**: Media
* **impacto**: Bajo
* **Exposición**: Baja
* **Mitigación**: Mantener un mínimo nivel de testing requerido en cada módulo.
* **Plan de contingencia**: Reparar bugs y mejorar los test del módulo.

