# Resumen Ejecutivo

## Proyecto RED

**Versión:** 1.0
**Fecha:** Junio 2026
**Autor:** Elias Hurtado Reales

---

# Introducción

RED es una empresa dedicada al diseño, estampación y comercialización de prendas textiles. Con el crecimiento del comercio electrónico, surge la necesidad de contar con una plataforma digital que permita mejorar la interacción entre la empresa y sus clientes, facilitando la consulta de productos y la administración de la información desde un único sistema.

Este proyecto consiste en el desarrollo de una aplicación web construida con **Django**, cuyo propósito es ofrecer una solución organizada, segura y escalable para la gestión de usuarios, productos y comunicación con los clientes.

---

# Planteamiento del Problema

Actualmente, RED no dispone de una plataforma web que permita mostrar su catálogo de productos ni gestionar de manera centralizada la información de sus clientes.

La ausencia de un sistema digital dificulta la difusión de los productos, limita el alcance comercial de la empresa y obliga a realizar múltiples procesos de forma manual, generando demoras y aumentando la posibilidad de errores administrativos.

Además, la empresa no cuenta con un medio para que los visitantes puedan registrarse, autenticarse ni enviar consultas directamente desde internet.

---

# Solución Propuesta

Se desarrollará una aplicación web que permitirá a los usuarios crear una cuenta, iniciar sesión y consultar un catálogo de productos disponibles.

El sistema incorporará un formulario de contacto mediante el cual cualquier visitante podrá comunicarse con la empresa para realizar consultas o solicitar información.

Adicionalmente, se implementará un panel de administración desde el cual el administrador podrá gestionar los productos registrados mediante operaciones de creación, consulta, actualización y eliminación (CRUD), garantizando que la información del catálogo permanezca actualizada.

La solución estará desarrollada bajo el patrón Modelo-Vista-Template (MVT) de Django, utilizando una arquitectura cliente-servidor que facilite futuras ampliaciones del sistema.

---

# Objetivo General

Desarrollar una aplicación web que permita administrar usuarios y productos mediante una plataforma segura y organizada, ofreciendo un catálogo digital y un formulario de contacto que fortalezca la presencia digital de la empresa RED.

---

# Objetivos Específicos

* Implementar el registro e inicio de sesión de usuarios.
* Desarrollar un catálogo para visualizar los productos disponibles.
* Implementar un formulario de contacto para la comunicación con la empresa.
* Desarrollar un panel de administración para gestionar los productos.
* Aplicar buenas prácticas de desarrollo utilizando Django y Git.
* Diseñar una estructura modular que facilite el mantenimiento del sistema.

---

# Alcance

La primera versión del proyecto contempla las siguientes funcionalidades:

* Registro de usuarios.
* Inicio de sesión.
* Administración de usuarios mediante Django Admin.
* Catálogo de productos.
* Visualización del detalle de cada producto.
* Formulario de contacto.
* Panel administrativo para la gestión de productos.
* Búsqueda básica de productos.

Las funcionalidades relacionadas con compras en línea, pagos electrónicos, personalización de prendas, carrito de compras y seguimiento de pedidos no hacen parte del alcance de esta primera versión.

---

# Tecnologías Utilizadas

| Componente           | Tecnología        |
| -------------------- | ----------------- |
| Lenguaje             | Python 3          |
| Framework Backend    | Django            |
| Base de Datos        | SQLite            |
| Frontend             | HTML5             |
| Estilos              | Bootstrap 5 + CSS |
| Interactividad       | JavaScript        |
| Control de Versiones | Git               |
| Repositorio Remoto   | GitHub            |

---

# Beneficios Esperados

La implementación del sistema permitirá:

* Mejorar la presencia digital de la empresa.
* Facilitar la visualización del catálogo de productos.
* Centralizar la administración de la información.
* Optimizar la comunicación entre clientes y empresa.
* Reducir procesos manuales.
* Facilitar futuras ampliaciones del proyecto.

---

# Público Objetivo

La aplicación está orientada a dos tipos de usuarios:

## Clientes

* Registrarse.
* Iniciar sesión.
* Consultar el catálogo.
* Visualizar el detalle de los productos.
* Enviar mensajes mediante el formulario de contacto.

## Administradores

* Gestionar productos.
* Crear nuevos registros.
* Editar información.
* Eliminar registros cuando sea necesario.
* Administrar la información desde el panel administrativo.

---

# Resultados Esperados

Al finalizar el desarrollo se espera disponer de una plataforma web funcional que permita gestionar usuarios, productos y solicitudes de contacto desde una única aplicación, ofreciendo una base sólida para futuras funcionalidades como pedidos, pagos en línea, personalización de productos y gestión de inventario.

---

# Conclusión

El desarrollo de esta aplicación representa el primer paso hacia la transformación digital de la empresa RED. La solución propuesta permitirá organizar la información de manera centralizada, mejorar la experiencia de los usuarios y facilitar la administración del catálogo de productos mediante una plataforma moderna, escalable y desarrollada con tecnologías ampliamente utilizadas en el desarrollo web.
