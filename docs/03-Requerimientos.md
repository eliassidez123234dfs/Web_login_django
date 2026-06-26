# Requerimientos del Sistema

## Proyecto RED

**Versión:** 1.0
**Fecha:** Junio 2026

---

# Introducción

Este documento describe los requerimientos funcionales y no funcionales del proyecto **RED**, definiendo las características que deberá cumplir el sistema para satisfacer las necesidades de la empresa y de sus usuarios.

Los requerimientos sirven como guía para el desarrollo, las pruebas y el mantenimiento de la aplicación.

---

# Actores del Sistema

## Visitante

Es cualquier persona que accede a la plataforma sin haber iniciado sesión.

Puede:

* Visualizar el catálogo de productos.
* Consultar el detalle de un producto.
* Registrarse.
* Iniciar sesión.
* Enviar mensajes mediante el formulario de contacto.

---

## Usuario Registrado

Corresponde a un usuario autenticado dentro del sistema.

Puede:

* Iniciar sesión.
* Cerrar sesión.
* Visualizar el catálogo.
* Consultar el detalle de los productos.
* Enviar mensajes de contacto.

---

## Administrador

Es el encargado de gestionar la información del sistema.

Puede:

* Administrar productos.
* Crear productos.
* Editar productos.
* Eliminar productos.
* Consultar mensajes enviados desde el formulario de contacto.
* Administrar usuarios mediante Django Admin.

---

# Requerimientos Funcionales

## Gestión de Usuarios

### RF-001 Registro de Usuario

El sistema deberá permitir el registro de nuevos usuarios mediante un formulario.

Campos mínimos:

* Nombre de usuario.
* Correo electrónico.
* Contraseña.
* Confirmación de contraseña.

---

### RF-002 Inicio de Sesión

El sistema deberá permitir que un usuario autenticado acceda a la plataforma utilizando su correo electrónico o nombre de usuario y su contraseña.

---

### RF-003 Cierre de Sesión

El usuario podrá cerrar su sesión en cualquier momento.

---

# Catálogo de Productos

### RF-004 Visualización del Catálogo

El sistema mostrará todos los productos disponibles.

Cada producto deberá mostrar como mínimo:

* Imagen.
* Nombre.
* Precio.
* Descripción corta.

---

### RF-005 Detalle del Producto

El usuario podrá visualizar la información completa de un producto.

Información mostrada:

* Imagen.
* Nombre.
* Descripción.
* Precio.
* Estado.

---

### RF-006 Búsqueda de Productos

El usuario podrá realizar búsquedas utilizando el nombre del producto.

---

# Gestión de Productos

### RF-007 Crear Producto

El administrador podrá registrar nuevos productos.

---

### RF-008 Editar Producto

El administrador podrá modificar la información de un producto existente.

---

### RF-009 Eliminar Producto

El administrador podrá eliminar productos del catálogo.

---

### RF-010 Listar Productos

El administrador podrá visualizar todos los productos registrados.

---

# Formulario de Contacto

### RF-011 Enviar Mensaje

El sistema permitirá enviar mensajes mediante un formulario de contacto.

Campos:

* Nombre
* Correo
* Asunto
* Mensaje

---

### RF-012 Almacenar Mensajes

Los mensajes enviados serán almacenados en la base de datos para su posterior consulta.

---

# Requerimientos No Funcionales

## RNF-001 Seguridad

Las contraseñas deberán almacenarse utilizando el sistema de hash implementado por Django.

---

## RNF-002 Disponibilidad

La aplicación deberá estar disponible para los usuarios mientras el servidor se encuentre en funcionamiento.

---

## RNF-003 Usabilidad

La interfaz deberá ser intuitiva y sencilla de utilizar.

---

## RNF-004 Rendimiento

El sistema deberá responder las solicitudes en tiempos adecuados para garantizar una buena experiencia de usuario.

---

## RNF-005 Compatibilidad

La aplicación deberá funcionar correctamente en los principales navegadores web modernos.

---

## RNF-006 Escalabilidad

La arquitectura deberá permitir la incorporación de nuevos módulos sin afectar los existentes.

---

# Reglas de Negocio

## RN-001

Cada usuario deberá registrarse utilizando un correo electrónico válido.

---

## RN-002

No podrán existir dos usuarios registrados con el mismo correo electrónico.

---

## RN-003

Solo los administradores podrán gestionar los productos.

---

## RN-004

Todos los productos deberán contener un nombre y un precio antes de ser almacenados.

---

## RN-005

El formulario de contacto deberá validar que todos los campos obligatorios hayan sido diligenciados.

---

# Restricciones del Sistema

* El desarrollo se realizará utilizando Django.
* La base de datos utilizada durante el desarrollo será SQLite.
* La interfaz será construida con HTML5, CSS3 y Bootstrap 5.
* El control de versiones será administrado mediante Git y GitHub.

---

# Casos de Uso Principales

| Código | Caso de Uso                   | Actor         |
| ------ | ----------------------------- | ------------- |
| CU-01  | Registrar usuario             | Visitante     |
| CU-02  | Iniciar sesión                | Usuario       |
| CU-03  | Cerrar sesión                 | Usuario       |
| CU-04  | Visualizar catálogo           | Visitante     |
| CU-05  | Consultar detalle de producto | Visitante     |
| CU-06  | Buscar productos              | Visitante     |
| CU-07  | Enviar mensaje de contacto    | Visitante     |
| CU-08  | Crear producto                | Administrador |
| CU-09  | Editar producto               | Administrador |
| CU-10  | Eliminar producto             | Administrador |
| CU-11  | Listar productos              | Administrador |

---

# Prioridad de Desarrollo

| Funcionalidad     | Prioridad |
| ----------------- | --------- |
| Registro          | Alta      |
| Inicio de sesión  | Alta      |
| Catálogo          | Alta      |
| CRUD de Productos | Alta      |
| Contacto          | Media     |
| Búsqueda          | Media     |

---

# Conclusión

Los requerimientos definidos establecen el comportamiento esperado del sistema RED y servirán como base para el diseño de la base de datos, la implementación del código fuente y la ejecución de pruebas funcionales. La correcta implementación de estos requerimientos permitirá desarrollar una aplicación organizada, mantenible y preparada para futuras ampliaciones.
