# Web Scraper para Datos de Contratación Pública

## Descripción General

Este proyecto es un web scraper que recopila URLs específicas del sitio web de contratación pública española (https://contrataciondelestado.es). El script utiliza Selenium y BeautifulSoup para navegar por el sitio web, completar los criterios de búsqueda y extraer enlaces profundos (deep-link URLs) de los resultados de búsqueda.

El scraper está desarrollado en Python y se centra principalmente en extraer datos relacionados con "Obras" con un código CPV específico (`41000000`). Este proyecto automatiza la tarea de recopilar información de contratación, facilitando la extracción eficiente de los datos relevantes para cualquier interesado en contratos públicos.

## Características

- Utiliza **Selenium** para interactuar con una interfaz web dinámica.
- Utiliza **BeautifulSoup** para analizar datos HTML y extraer enlaces relevantes.
- Automatiza el proceso de navegación a través de múltiples páginas de resultados de búsqueda.
- Guarda los URLs extraídos en un archivo de texto para un uso posterior.

## Requisitos Previos

Asegúrate de tener lo siguiente instalado:

- **Python 3.6+**
- **Google Chrome** (u otro navegador si se modifica)
- **ChromeDriver** para Selenium (compatible con la versión instalada de Chrome)
- Bibliotecas de Python necesarias:
  - `selenium`
  - `beautifulsoup4`

## Instalación

1. Clona el repositorio desde GitHub:

   ```sh
   git clone https://github.com/yourusername/your-repository-name.git
   cd your-repository-name
   ```

2. Instala los paquetes requeridos usando `pip`:

   ```sh
   pip install -r requirements.txt
   ```

   Crea un archivo `requirements.txt` con el siguiente contenido:

   ```
   selenium
   beautifulsoup4
   ```

3. Asegúrate de tener **ChromeDriver** instalado y disponible en la variable PATH de tu sistema.

## Uso

Para ejecutar el scraper, simplemente ejecuta el script de Python:

```sh
python scraper.py
```

El script:

1. Abrirá el navegador Chrome y navegará al sitio web de contratación pública española.
2. Completará el formulario de búsqueda con el código CPV especificado (`41000000`).
3. Recopilará URLs de los resultados de búsqueda a través de todas las páginas.
4. Guardará las URLs recopiladas en un archivo de texto llamado `all_deeplink_urls.txt`.

## Notas Importantes

- Este scraper interactúa con un sitio web en vivo, por lo que debes considerar las implicaciones éticas y legales antes de ejecutarlo.
- Asegúrate de no sobrecargar el servidor con demasiadas solicitudes en un corto período de tiempo.
- Considera modificar el código para añadir retrasos (`time.sleep()`) y evitar posibles problemas con el sitio web.

## Archivos

- **scraper.py**: Script principal para extraer datos del sitio web de contratación pública.
- **requirements.txt**: Lista de dependencias para instalar antes de ejecutar el script.
- **all_deeplink_urls.txt**: Archivo de salida que contiene todos los URLs recopilados.

## Estructura del Proyecto

```
|-- scraper.py
|-- requirements.txt
|-- all_deeplink_urls.txt
```

## Licencia

Este proyecto está licenciado bajo la Licencia GNU. Consulta el archivo `LICENSE` para más detalles.

## Contribuir

Siéntete libre de hacer un fork de este repositorio y realizar mejoras. ¡Las pull requests son bienvenidas!

1. Haz un fork del repositorio
2. Crea una rama para tu nueva característica (`git checkout -b feature/nueva-caracteristica`)
3. Realiza tus cambios (`git commit -m 'Añadir una característica'`)
4. Sube la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## Contacto

Si tienes alguna pregunta o problema, siéntete libre de abrir un issue en el repositorio o contactarme en `isidrecc@gmail.com`.


