# Arquitectura del Sistema

## Proyecto RED

**Versión:** 1.0
**Framework:** Django
**Patrón:** Modelo - Vista - Template (MVT)

---

# Introducción

La aplicación RED está desarrollada utilizando el framework **Django**, el cual implementa el patrón de arquitectura **Modelo - Vista - Template (MVT)**. Esta arquitectura permite separar las responsabilidades del sistema, facilitando el mantenimiento, la escalabilidad y la reutilización del código.

Además, el sistema sigue una arquitectura **Cliente - Servidor**, donde los usuarios interactúan con la aplicación mediante un navegador web mientras el servidor procesa las solicitudes y administra la información almacenada en la base de datos.

---

# Arquitectura General

El funcionamiento general del sistema puede representarse mediante el siguiente diagrama:

```text
                    Usuario
                       │
                       │ HTTP
                       ▼
┌─────────────────────────────────────┐
│             Navegador Web           │
│      HTML + CSS + Bootstrap         │
└─────────────────────────────────────┘
                       │
                       │ Solicitudes
                       ▼
┌─────────────────────────────────────┐
│             Django                  │
│        URLs → Views → Models        │
└─────────────────────────────────────┘
                       │
                       │ ORM
                       ▼
┌─────────────────────────────────────┐
│            SQLite Database          │
└─────────────────────────────────────┘
```

---

# Arquitectura Cliente - Servidor

El sistema está dividido en dos componentes principales.

## Cliente

Corresponde al navegador web utilizado por el usuario.

Sus responsabilidades son:

* Mostrar las páginas del sistema.
* Capturar la información ingresada por el usuario.
* Enviar solicitudes al servidor.
* Mostrar las respuestas obtenidas.

Tecnologías utilizadas:

* HTML5
* CSS3
* Bootstrap 5
* JavaScript

---

## Servidor

El servidor procesa todas las solicitudes realizadas por los usuarios.

Entre sus responsabilidades se encuentran:

* Registrar usuarios.
* Autenticar usuarios.
* Consultar productos.
* Gestionar el formulario de contacto.
* Administrar la información del sistema.

Tecnologías utilizadas:

* Python
* Django

---

## Base de Datos

Toda la información del sistema es almacenada utilizando SQLite durante la fase de desarrollo.

La base de datos almacena:

* Usuarios.
* Productos.
* Mensajes de contacto.

En futuras versiones podrá migrarse fácilmente a PostgreSQL sin realizar cambios importantes en la lógica del sistema gracias al ORM de Django.

---

# Patrón MVT de Django

Django utiliza el patrón **Modelo - Vista - Template**, el cual organiza la aplicación en diferentes capas.

## Model

Los modelos representan las tablas de la base de datos.

Su función principal es:

* Definir la estructura de los datos.
* Validar información.
* Gestionar las relaciones entre tablas.

Ejemplo:

* Usuario
* Producto
* Contacto

---

## View

Las vistas contienen la lógica del sistema.

Su responsabilidad es:

* Recibir las solicitudes del navegador.
* Procesar la información.
* Consultar los modelos.
* Enviar la respuesta correspondiente.

Ejemplos:

* Registro de usuarios.
* Inicio de sesión.
* Listado de productos.
* Formulario de contacto.

---

## Template

Los Templates representan la interfaz visual.

Se encargan de mostrar la información al usuario mediante páginas HTML utilizando el motor de plantillas de Django.

Ejemplos:

* Login
* Registro
* Catálogo
* Contacto
* Panel administrativo

---

# Flujo del Registro

```text
Usuario

↓

Formulario de Registro

↓

Validación de Datos

↓

Creación del Usuario

↓

Base de Datos

↓

Redirección al Login
```

---

# Flujo del Inicio de Sesión

```text
Usuario

↓

Formulario Login

↓

Validación de Credenciales

↓

Autenticación Django

↓

Inicio de Sesión

↓

Redirección al Panel Administrativo
```

---

# Flujo del Catálogo

```text
Usuario

↓

Solicita Catálogo

↓

View de Productos

↓

Consulta Base de Datos

↓

Obtiene Productos

↓

Renderiza Plantilla

↓

Visualiza Catálogo
```

---

# Flujo del Formulario de Contacto

```text
Usuario

↓

Completa Formulario

↓

Validación

↓

Guardar Mensaje

↓

Base de Datos

↓

Mensaje de Confirmación
```

---

# Estructura General del Proyecto

```text
ProyectoRED/

│

├── core/

│   ├── settings.py

│   ├── urls.py

│   └── wsgi.py

│

├── users/

│

├── products/

│

├── contact/

│

├── templates/

│

├── static/

│

├── media/

│

├── db.sqlite3

│

└── manage.py
```

---

# Organización de los Módulos

El sistema se encuentra dividido en módulos independientes para facilitar el mantenimiento.

| Módulo    | Responsabilidad                               |
| --------- | --------------------------------------------- |
| Users     | Registro e inicio de sesión                   |
| Products  | Gestión y visualización de productos          |
| Contact   | Gestión de mensajes enviados por los usuarios |
| Templates | Interfaces gráficas                           |
| Static    | Archivos CSS, JavaScript e imágenes           |

---

# Principios Aplicados

Durante el desarrollo del proyecto se aplican los siguientes principios:

* Separación de responsabilidades.
* Reutilización de código.
* Modularidad.
* Escalabilidad.
* Mantenimiento sencillo.
* Organización por aplicaciones de Django.

---

# Ventajas de la Arquitectura

La arquitectura implementada ofrece múltiples beneficios:

* Facilita el mantenimiento del código.
* Permite agregar nuevas funcionalidades sin afectar las existentes.
* Mejora la organización del proyecto.
* Favorece la reutilización de componentes.
* Facilita el trabajo colaborativo.
* Aprovecha las buenas prácticas recomendadas por Django.

---

# Conclusión

La arquitectura implementada proporciona una base sólida para el desarrollo del proyecto RED. La separación entre presentación, lógica de negocio y acceso a datos permite construir una aplicación organizada, escalable y fácil de mantener, preparada para incorporar nuevas funcionalidades en futuras versiones.
