# RE-LIC

La app es un sistema de consulta y carga de dos tipos de publicaciones: remates judiciales y licitaciones.

Y tiene tres roles de usuarios: Clientes, Martilleros y Operadores del sistema.

Después de implementar restricción con logueo los clientes sólo pueden listar y buscar remates y licitaciones, los martilleros pueden listar, buscar y cargar remates y cargargarse como martilleros habilitados y los operarios pueden listar, buscar y cargar remates, licitaciones, clientes, martilleros y operadores. 

Se comienza en http://127.0.0.1:8000/ y se puede navegar en las "vistas publicas" de remates, licitaciones y martilleros.

Hay dos vistas sólo para operadores, la de clientes (/Publicaciones/clientes/) y la de operadores (/Publicaciones/operadores/) en las que puede consultar y cargar esos registros.
