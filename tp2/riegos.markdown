* Riego1:
**Descripción**: Desconocimiento de las tecnologías a usar: OpenID, base de datos nosql, webmining, sms, cloud computing, etc. que podría llegar a ocasionar retrasos inesperados en el proyecto
**Probabilidad**: Media
**impacto**: Medio
**Exposición**: Medio
**Mitigación**: dedicar horas de aprendizaje, lo antes posible, para cada tecnología y saber de antemano los problemas que podrían suceder
**Plan de contingencia**: contratar gente especializada en las tecnologías

* Riego2:
**Descripción**: Definiciones vagas: criterios de sustitución y asociación, información a recuperar, prioridad de los usuarios por la información
**Probabilidad**: Alta
**impacto**: Alto
**Exposición**: Alto
**Mitigación**: Acordar fechas límites para la presentación de documentación definiendo mejor cada caso en particular.
**Plan de contingencia**: ??

* Riego3:
**Descripción**: Inconvenientes con el servicio de spambust que nos deja sin esta funcionalidad. (E.g.: sube el precio, problemas de servicio por su parte)
**Probabilidad**: Baja
**impacto**: Alto
**Exposición**: Medio
**Mitigación**: Implementar, lo antes posible, un servicio propio que remplace el de spambust
**Plan de contingencia**: dejar de detectar el spam o detectarlo en menor medida con una implementación fácil y rápida pero no tan efectiva.

* Riego4:
**Descripción**: Falta de dinero para financiar el proyecto.
**Probabilidad**: Media
**impacto**: Alto
**Exposición**: Alto
**Mitigación**: Conseguir sponsor, lo antes posibles, para que el proyecto sea auto-sostenible
**Plan de contingencia**: resignar funcionalidades del proyecto que requiera mucha inversión para reducir los costos.

* Riego5:
**Descripción**: Falta de testing adecuado en algún modulo / funcionalidad del sistema.
**Probabilidad**: Baja
**impacto**: Bajo
**Exposición**: Bajo
**Mitigación**: Mejorar los test de cada modulo
**Plan de contingencia**: reparar bugs y mejorar los test del modulo

* Riego6:
**Descripción**: Un miembro abandona el equipo de trabajo.
**Probabilidad**: Media
**impacto**: Medio
**Exposición**: Media
**Mitigación**: particionado al sistema en 'modulos' simples con una única responsabilidad y alta cohesión interna, y manteniendo la documentación de la arquitectura del sistema actualizada, de forma que al incorporar un remplazo, la curva de aprendizaje del sistema se vea reducida.
**Plan de contingencia**: contratar remplazo




--- 
son todo lo mismo, problema con el HW, yo dejaria una sola, la primera (o haria un merge)..
---
* Riego7:
**Descripción**: El hardware disponible no es suficiente para soportar TODAS las funcionalidades a cumplir (extraer datos, publicarlos mediante la api, predecir los deseos del usuario, verificar los datos recibidos, generar información de auditoría).
**Probabilidad**: Medio
**impacto**: Alto
**Exposición**: Alto
**Mitigación**: Mas HW, mejores algoritmos
**Plan de contingencia**: resignar alguna de las funcionalidades

* Riego: 
**Descripción**: Para lograr que los datos sean accesibles rápidamente, si tenemos que hacer polling, puede que la cantidad de HW disponible no nos permita acceder a la información con la constancia necesaria.
**Probabilidad**: Medio
**impacto**: Medio
**Exposición**: Media
**Mitigación**: Mas HW, mejores algoritmos
**Plan de contingencia**: resignar un poco el tiempo de accesibilidad a la información.

* Riego:
**Descripción**: El hardware disponible no es suficiente para realizar la extracción de datos de internet de manera suficientemente rápida
**Probabilidad**: Media
**impacto**: bajo
**Exposición**: bajo
**Mitigación**: Mas HW, mejores algoritmos
**Plan de contingencia**: resignar la velocidad de extracción de datos desde internet


* Riego: 
**Descripción**: Por la falta de HW podemos tener problemas para otras tareas pesadas en procesamiento como ser: cálculo de prioridades de los usuarios, verificación de las ofertas conseguidas, mantenimiento de información de auditoría 
**Probabilidad**: Baja
**impacto**: Medio
**Exposición**: Baja
**Mitigación**: Mas HW, mejores algoritmos
**Plan de contingencia**: resignar alguna de las funcionalidades (??)




