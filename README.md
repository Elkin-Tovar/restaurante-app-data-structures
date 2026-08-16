# Sistema de Restaurante (restaurante_app)

## Autor
* **Elkin Esteban Tovar Caicedo**

## Descripción del Proyecto
Sistema modular de gestión para restaurantes desarrollado en Python aplicando los principios de Programación Orientada a Objetos (POO). El proyecto permite administrar eficientemente colecciones de productos y usuarios mediante el uso práctico de estructuras de datos nativas de Python.

## Estructura del Proyecto
```text
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
├── main.py
└── README.md
Responsabilidad de los Componentes
modelos/producto.py: Contiene la clase Producto, encargada de representar la información propia de cada producto del restaurante (código, nombre, categoría y precio).

modelos/usuario.py: Contiene la clase Usuario, encargada de representar la información general de una persona registrada en el sistema (identificación, nombre y correo).

servicios/restaurante.py: Contiene la clase Restaurante, responsable de administrar las colecciones de datos y encapsular la lógica de negocio (registros con validación de duplicados, búsquedas, actualizaciones, eliminaciones y listados).

main.py: Punto de entrada de la aplicación. Coordina el menú interactivo, la interacción por consola con el usuario mediante input(), la creación de objetos y las llamadas a los métodos del servicio.

README.md: Documenta la estructura, el funcionamiento y la explicación detallada de las estructuras de datos aplicadas en el proyecto.

Aplicación de Estructuras de Datos
Lista (list): Se utilizó en la clase Restaurante (self.productos y self.usuarios) para administrar colecciones dinámicas de objetos, permitiendo realizar operaciones de inserción, búsqueda, actualización, borrado y listado secuencial.

Tupla (tuple): Se aplicó en main.py (opciones_menu) para almacenar la información estable e inmutable de las opciones del menú principal que se muestran en pantalla durante toda la ejecución.

Diccionario (dict): Se implementó en main.py (acciones_menu) para establecer una relación directa de clave → valor, asociando cada opción del menú ingresada por el usuario con su respectiva función ejecutora.

Conjunto (set): Se utilizó en el servicio Restaurante (obtener_categorias_unicas) para extraer dinámicamente las categorías de los productos registrados, asegurando que se presenten de forma limpia y sin elementos duplicados.

Instrucciones para Ejecutar el Programa
Asegúrate de tener instalado Python en tu equipo.

Abre una terminal y sitúate en la carpeta raíz del proyecto (restaurante_app).

Ejecuta el siguiente comando:

Bash
python main.py
Utiliza el menú interactivo ingresando el número de la opción deseada por consola.

Reflexión
Seleccionar la estructura de datos adecuada es fundamental en el desarrollo de software porque cada una está optimizada para resolver problemas específicos con eficiencia y orden. Utilizar listas facilita el dinamismo y orden secuencial de los registros; las tuplas garantizan la seguridad de datos estables que no deben mutar; los diccionarios permiten búsquedas y asociaciones rápidas por clave; y los conjuntos simplifican de forma nativa la depuración de elementos repetidos. Una correcta elección impacta directamente en el rendimiento, la legibilidad y la escalabilidad del código.
