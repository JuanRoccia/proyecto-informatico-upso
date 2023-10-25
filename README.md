# Proyecto Informático - UPSO Full Stack Development

**Repositorio Oficial del Proyecto Final Full Stack** para la materia "Proyecto Informático" de la Universidad Provincial del Sudoeste (UPSO).

## Detalles Generales:

**Base de datos:** [phpMyAdmin](https://phpmyadmin.alwaysdata.com/)

**Miro UML:** [Enlace al UML](https://miro.com/app/board/uXjVNcVEkuI=/?share_link_id=288846579962)

**Miro esquema de funcionalidad:** [Enlace al esquema](https://miro.com/welcomeonboard/SzdmejZMY3RPM2tKUmtIVVhOeUVmbmRMTW9odFdQWjdxZnhMaHNLSzR3ZDNrQ2JXSkNpdGE0MjFTemJ3RGJia3wzNDU4NzY0NTY2MzkxMjI1NDYzfDI=?share_link_id=290604163291)

*Nota: Aquí también irían los detalles de alojamiento y esas cuestiones del lanzamiento.*

## Registro de Desarrollo:

### Día 1: Inicio y Fundamentación del Proyecto

**Fecha:** 10/10/2023

**Resumen del Día:**
Hoy marcamos el comienzo oficial de nuestro ambicioso proyecto final. El equipo se reunió para discutir y esbozar la arquitectura y el diseño fundamental del sistema.

**Logros Principales:**
- **Diseño UML:** Finalizamos el diseño del Modelo UML para nuestra base de datos. Este modelo servirá como nuestra guía principal para las futuras implementaciones y garantizará que todos los miembros del equipo tengan una visión clara de la estructura de datos.
- **Implementación Inicial de Flask:** Realizamos nuestro primer commit, que incluye la implementación básica de Flask. Esta será la base sobre la que construiremos nuestra aplicación backend.
- **Estructura del Proyecto:** Decidimos dividir nuestro proyecto en dos segmentos principales: frontend y backend. Esta estructura modular nos ayudará a mantener el código organizado y facilitará la colaboración entre los miembros del equipo.
- **Integración de la Base de Datos Remota:** Establecimos una conexión con nuestra base de datos en remoto. Asegurarnos de que esta integración funcione sin problemas desde el principio es crucial para el desarrollo fluido del proyecto.

**Reflexiones y Pensamientos:**
El primer día sentó las bases de lo que promete ser un proyecto desafiante pero gratificante. El equipo está motivado y listo para enfrentar los desafíos que se avecinan. Estamos ansiosos por ver cómo evoluciona este proyecto y cómo nuestra visión inicial se transforma y se adapta a medida que avanzamos.

### Día 2: Implementación de la Base de Datos y Trabajo en el Frontend

**Fecha:** 11/10/2023

**Resumen del Día:**
Hoy, el equipo se centró en la implementación de la base de datos y en la mejora del frontend. Se agregaron varios archivos y se organizó la estructura del proyecto para facilitar el desarrollo.

**Logros Principales:**
- **Base de Datos:** Agregamos la base de datos y sus archivos de queries. Además, la implementamos en alwaysdata.com para tener acceso remoto a la misma.
- **Models.py:** Se agregaron los métodos en `models.py` para acceder a los datos de la base de datos.
- **Frontend:** Se trabajó en el frontend, mejorando su apariencia y funcionalidad. Se agregaron estilos y se organizó la estructura de carpetas con archivos como `normalize.css`, `variables.css` y `index.css` en sus respectivas ubicaciones.

**Reflexiones y Pensamientos:**
El segundo día vio una gran cantidad de progreso en términos de funcionalidad y diseño. Con la base de datos en su lugar y el frontend tomando forma, el equipo está emocionado por lo que vendrá a continuación. La colaboración y la organización han sido clave para el éxito de hoy, y esperamos mantener este impulso en los próximos días.

### Día 3: Modificaciones, Avances en Organización y Estructura

**Fecha:** 12/10/2023

**Resumen del Día:**
Hoy, el equipo continuó con el impulso de los días anteriores, enfocándose en fortalecer la estructura del proyecto. Se priorizó la organización, creando y consolidando ramas específicas en el repositorio y ajustando la base de datos para alinearla con las visiones más recientes del UML y el esquema de funcionalidades.

**Logros Principales:**
- **Rama `develop`:** Se implementó la rama `develop` para centralizar los pull requests de los cambios que realiza el equipo en sus respectivas ramas. Esto permite mantener la rama `main` aislada y actualizada con la última versión funcional.
- **Rama `release`:** Se implementó la rama `release` para el lanzamiento de la app.
- **Configuraciones de Flask:** Se ajustaron las configuraciones necesarias para organizar las rutas y directorios de Flask.
- **Base de Datos:** Se realizaron modificaciones en la base de datos para ajustar ciertas características con las nuevas implementaciones reflejadas en el UML y en el esquema de funcionalidades.

**Reflexiones y Pensamientos:**
El tercer día estuvo lleno de avances significativos en términos de estructura y organización del proyecto. Con la implementación de nuevas ramas y ajustes en la base de datos, el equipo está bien posicionado para próximas implementaciones.

### Día 4: Implementaciones y Optimizaciones

**Fecha:** 13/10/2023

**Resumen del Día:**
Hoy, el equipo se sumergió en las implementaciones más recientes y en la optimización de las funcionalidades existentes. Con la colaboración activa de todos, logramos avanzar significativamente en varios frentes del proyecto.

**Logros Principales:**
- **Dashboard:** Se inició el desarrollo del `aside` del dashboard, un componente esencial para la navegación y la experiencia del usuario.
- **Base de Datos:** Se realizaron ajustes cruciales en la base de datos, especialmente en la estructura de las facturas. Se eliminaron las claves primarias innecesarias y se añadió el campo `user_idUser` a la tabla `Bill` para mejorar la relación y la funcionalidad.
- **Funcionalidades de Productos:** Se implementaron métodos para consultar, modificar y eliminar productos. Estas funcionalidades son esenciales para la gestión de productos en nuestra aplicación.
- **Pull Requests:** Se enviaron dos pull requests importantes: "Init dashboard-aside" y "PUT, DELETE, GET product", que reflejan el progreso del día y preparan el terreno para futuras integraciones.

**Reflexiones y Pensamientos:**
El cuarto día demostró la capacidad del equipo para adaptarse y evolucionar. A medida que el proyecto avanza, cada miembro del equipo ha demostrado su compromiso y habilidad para enfrentar desafíos y superar obstáculos. Con cada nuevo día, nuestra visión se acerca un paso más a la realidad.

### Día 5: Avances en Autenticación y Consolidación de Funcionalidades

**Fecha:** 14/10/2023

**Resumen del Día:**
Hoy, el equipo se centró en fortalecer la autenticación y consolidar las funcionalidades que se han estado desarrollando. La colaboración entre los miembros del equipo fue esencial para garantizar que las implementaciones fueran coherentes y alineadas con la visión del proyecto.

**Logros Principales:**
- **Autenticación:** Se implementó la generación de tokens para mejorar la seguridad en el proceso de autenticación. Esta implementación es crucial para garantizar que solo los usuarios autorizados tengan acceso a ciertas partes de la aplicación.
- **Refactorización:** Se realizaron cambios en las variables para mejorar la legibilidad y coherencia del código. Estos cambios son esenciales para garantizar que el código sea mantenible a medida que el proyecto crece.
- **Estilos del Dashboard:** Se fusionaron los estilos del `aside` del dashboard, mejorando la apariencia y la experiencia del usuario.
- **Registro y Login:** Se inició el desarrollo de los scripts de registro y login, estableciendo la base para la autenticación de usuarios en la plataforma. Además, se implementó la encriptación de contraseñas para garantizar la seguridad de los datos de los usuarios.

**Reflexiones y Pensamientos:**
El quinto día reflejó la dedicación del equipo para mejorar y optimizar el proyecto. Con la implementación de características esenciales como la autenticación y la encriptación, el equipo ha demostrado su compromiso con la seguridad y la eficiencia. Estamos emocionados por los próximos pasos y confiamos en que cada día nos acerca más a nuestro objetivo final.

### Día 6: Consolidación de Autenticación y Mejoras en la Interfaz

**Fecha:** 20/10/2023

**Resumen del Día:**
Hoy, el equipo se sumergió profundamente en la consolidación de las funcionalidades de autenticación y en la mejora de la interfaz de usuario. Con la colaboración activa de todos, logramos pulir aspectos esenciales que mejoran la experiencia del usuario y la seguridad de la plataforma.

**Logros Principales:**
- **Decorador de Recursos de Usuario:** Se implementó un decorador de recursos de usuario con el objetivo principal de validar que el usuario que intenta acceder al recurso sea el correcto, evitando así el acceso no autorizado a datos de otros usuarios.
- **Pull Request de Autenticación:** Se completó la implementación de autenticación y se envió una pull request. Esta implementación garantiza que cada usuario solo pueda acceder a sus propios datos, mejorando la privacidad y la seguridad.
- **Manejo de Errores:** Se destacó la necesidad de manejar errores de manera más eficiente, con el objetivo de que la ejecución de Flask no muestre errores en la consola, mejorando así la robustez del backend.
- **Conexión entre Frontend y Backend:** Se logró conectar con éxito las funcionalidades de login y registro con el backend, y se realizaron ajustes en la función `register_user` para manejar correctamente los datos que provienen del frontend.
- **Validaciones:** Se implementaron validaciones adicionales para garantizar que se reciban todos los datos requeridos en el registro de usuarios, modificación de productos y adición de productos, y para asegurar que no haya campos vacíos o inválidos.

**Reflexiones y Pensamientos:**
El sexto día evidenció el compromiso del equipo con la perfección y la eficiencia. A medida que el proyecto avanza, hemos aprendido la importancia de la atención al detalle y la colaboración. Con cada nueva implementación y mejora, estamos construyendo una plataforma más segura, intuitiva y eficiente. El equipo está emocionado por los desafíos que se avecinan y confiado en que estamos en el camino correcto hacia la culminación exitosa de nuestro proyecto.

