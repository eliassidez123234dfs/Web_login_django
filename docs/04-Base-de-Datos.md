# Base de Datos

## Proyecto RED

**Versión:** 1.0
**Motor de Base de Datos:** SQLite (Desarrollo)
**ORM:** Django ORM

---

# Introducción

La base de datos del proyecto RED tiene como objetivo almacenar y administrar toda la información relacionada con los usuarios, productos y mensajes enviados desde el formulario de contacto.

Durante la etapa de desarrollo se utiliza SQLite por su facilidad de configuración e integración con Django. La arquitectura del proyecto permite migrar posteriormente a PostgreSQL sin modificar la lógica del sistema gracias al uso del ORM de Django.

---

# Modelo Entidad - Relación (MER)

En la primera versión del sistema se implementan tres entidades principales.

```text
                Usuario
                   │
                   │
        ┌──────────┴──────────┐
        │                     │
        ▼                     ▼
   Producto             Contacto
```

Cada entidad representa un módulo independiente del sistema y se comunica con la aplicación mediante el ORM de Django.

---

# Modelo Relacional

```text
USUARIO
-------------------------
id (PK)
username
email
password
first_name
last_name
is_staff
is_active
date_joined

PRODUCTO
-------------------------
id (PK)
nombre
descripcion
precio
imagen
stock
fecha_creacion

CONTACTO
-------------------------
id (PK)
nombre
correo
asunto
mensaje
fecha_envio
```

---

# Diccionario de Datos

## Tabla: Usuario

Corresponde al modelo de autenticación utilizado por Django.

| Campo       | Tipo     | Restricción   | Descripción                      |
| ----------- | -------- | ------------- | -------------------------------- |
| id          | Integer  | PK            | Identificador único              |
| username    | Varchar  | UNIQUE        | Nombre de usuario                |
| email       | Email    | UNIQUE        | Correo electrónico               |
| password    | Varchar  | NOT NULL      | Contraseña cifrada               |
| first_name  | Varchar  | Opcional      | Nombre                           |
| last_name   | Varchar  | Opcional      | Apellido                         |
| is_staff    | Boolean  | Default False | Permite acceder al administrador |
| is_active   | Boolean  | Default True  | Estado del usuario               |
| date_joined | DateTime | Auto          | Fecha de registro                |

---

## Tabla: Producto

Almacena los productos que serán visualizados en el catálogo.

| Campo          | Tipo       | Restricción | Descripción         |
| -------------- | ---------- | ----------- | ------------------- |
| id             | Integer    | PK          | Identificador       |
| nombre         | Varchar    | NOT NULL    | Nombre del producto |
| descripcion    | Text       | NOT NULL    | Descripción         |
| precio         | Decimal    | NOT NULL    | Precio              |
| imagen         | ImageField | Opcional    | Imagen del producto |
| stock          | Integer    | Default 0   | Cantidad disponible |
| fecha_creacion | DateTime   | Auto        | Fecha de creación   |

---

## Tabla: Contacto

Registra los mensajes enviados desde el formulario de contacto.

| Campo       | Tipo     | Restricción | Descripción           |
| ----------- | -------- | ----------- | --------------------- |
| id          | Integer  | PK          | Identificador         |
| nombre      | Varchar  | NOT NULL    | Nombre del remitente  |
| correo      | Email    | NOT NULL    | Correo electrónico    |
| asunto      | Varchar  | Opcional    | Asunto del mensaje    |
| mensaje     | Text     | NOT NULL    | Contenido del mensaje |
| fecha_envio | DateTime | Auto        | Fecha del envío       |

---

# Relaciones

Actualmente la primera versión del sistema mantiene una estructura sencilla, donde cada módulo funciona de forma independiente.

```text
Usuario

↓

Autenticación

↓

Panel Administrativo

↓

Administración de Productos
```

Los mensajes de contacto son almacenados de forma independiente y pueden ser consultados posteriormente desde el panel administrativo.

---

# Reglas de Integridad

Para garantizar la consistencia de los datos se aplican las siguientes restricciones:

* Cada usuario debe poseer un correo electrónico único.
* No pueden existir dos nombres de usuario iguales.
* Todo producto debe tener un nombre y un precio.
* Todo mensaje de contacto debe contener un nombre, un correo y un mensaje.
* Las contraseñas son almacenadas utilizando el sistema de hash de Django.

---

# Índices

Con el fin de optimizar las consultas se utilizan índices automáticos sobre:

| Campo    | Tabla    |
| -------- | -------- |
| username | Usuario  |
| email    | Usuario  |
| id       | Producto |
| id       | Contacto |

---

# Flujo de Persistencia

## Registro de Usuario

```text
Formulario

↓

View

↓

Modelo Usuario

↓

SQLite
```

---

## Registro de Producto

```text
Administrador

↓

Formulario

↓

Modelo Producto

↓

SQLite
```

---

## Registro de Contacto

```text
Formulario

↓

Validación

↓

Modelo Contacto

↓

SQLite
```

---

# Ventajas del Uso del ORM

El proyecto utiliza Django ORM para interactuar con la base de datos.

Entre sus ventajas se encuentran:

* Evita escribir consultas SQL manuales.
* Reduce errores de programación.
* Facilita el mantenimiento.
* Permite migrar fácilmente entre motores de base de datos.
* Protege contra ataques de inyección SQL mediante consultas parametrizadas.

---

# Migraciones

Toda modificación realizada sobre los modelos deberá reflejarse mediante el sistema de migraciones de Django.

Comandos utilizados:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# Respaldo de la Información

Durante el desarrollo, la información se almacena en el archivo `db.sqlite3`.

Para entornos de producción se recomienda:

* PostgreSQL como motor de base de datos.
* Respaldos automáticos periódicos.
* Restricción de acceso mediante usuarios con permisos específicos.
* Copias de seguridad antes de cada despliegue.

---

# Conclusión

La estructura de la base de datos propuesta proporciona una organización clara y eficiente para el almacenamiento de la información del sistema. El uso del ORM de Django facilita la administración de los datos, mejora la mantenibilidad del proyecto y permite que la aplicación pueda crecer incorporando nuevas entidades y relaciones en futuras versiones sin afectar la arquitectura existente.
