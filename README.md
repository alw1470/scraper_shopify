## Descripción General
Este script de Python es un raspador para tiendas Shopify, diseñado para extraer información detallada de productos de sitios web de Shopify. Está diseñado para recopilar datos de productos, incluyendo variantes, de la URL de una tienda Shopify especificada.

## Requisitos
- Python 3.x
- Requests: Biblioteca HTTP para Python.
- JSON: Biblioteca para manipulación de JSON.
- Dataset: Herramienta de base de datos para Python.

## Instalación
1. Asegúrate de tener instalado Python 3.x.
2. Instala las bibliotecas de Python requeridas:
   ```bash
   pip install requests
   pip install json
   pip install dataset

## Uso
1. Inicializa el raspador con la URL base de la tienda Shopify:
url = ShopifyScraper('https://tutiendashopify.com/')
2. Ejecuta el script. Este recopilará datos de productos y los guardará en una base de datos SQLite.

## Caracteristicas
.- Scrapeo de Información de Productos: Descarga JSON de la tienda Shopify y lo analiza para extraer detalles del producto.
.- Manejo de Paginación: Itera a través de múltiples páginas de productos.
.- Almacenamiento en Base de Datos: Guarda los datos scrapeados en una base de datos SQLite para análisis o uso posterio


## Funcionamiento
.- Inicialización: La clase ShopifyScraper se inicializa con la URL base de la tienda Shopify.
.- Descarga de JSON: El método dowloadjson obtiene datos de productos en formato JSON.
.- Análisis de JSON: El método parsejson procesa los datos JSON para extraer detalles del producto.
.- Conexión a la Base de Datos: Se conecta a una base de datos SQLite para almacenar los datos raspados.
.- Inserción de Datos: Inserta nuevos productos en la base de datos, evitando duplicados.

## Personlaizacion
.- Modifica el range en la función main para cambiar el número de páginas a raspar.
.- Cambia la URL de la base de datos en el bloque if __name__ == '__main__': para usar una base de datos diferente.

## Manejo de errores
.- Verifica errores en las solicitudes HTTP e imprime los códigos de estado.
.- Maneja excepciones durante el análisis de JSON y operaciones de base de datos.


## Limitaciones
.- Diseñado específicamente para tiendas Shopify.
.- Requiere ajuste manual del rango de paginación.
.- Capacidad limitada de manejo de error

## Licencia
.- Este script se publica bajo la Licencia MIT.

## Descargo de Responsabilidad
.- Esta herramienta está destinada solo para fines educativos e investigativos. Por favor, asegúrate de tener permiso para recopilar datos del sitio web objetivo.
