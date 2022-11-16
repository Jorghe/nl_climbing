# README #
nl Climbing almacena las rutas de las principales zonas de escalada en Nuevo León.

## Uso ##
Usa `git clone git@github.com:Jorghe/nl_climbing.git` para descargar el archivo

Para hacer web scraping inicia `scrapCrag.py`, en CLI se deberá inicializar automáticamente, después de unos segundos, se guarda un archivo llamado `nl-climbing.json`

### Jupyter Notebook ### 
Importa la biblioteca `from scrapCrag import nlCrag`

Después puedes usar la clase como
```
climbing = nlCrag()
# Cargar todos los archivos de forma asincrónica
climbing.initialize()

# Ahora puedes acceder a las rutas
rutas = climbing.crag

```
# Enlaces externos
Los resultados de este data wrangling está activo en http://nl-climbing.deta.dev/