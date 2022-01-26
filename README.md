# Data Cleaning Pandas

<a href="https://www.gifsanimados.org/cat-tiburones-516.htm"><img src="https://www.gifsanimados.org/data/media/516/tiburon-imagen-animada-0011.gif" border="0" alt="tiburon-imagen-animada-0011" /></a>


## INTRODUCCIÓN:
Para la realización de este proyecto hemos usado una base de datos de ataque de tiburones:
[Global Shark Attacks](https://www.kaggle.com/teajay/global-shark-attacks) 

Además hemos puesto en práctica diferentes métodos de Pandas y visualización de datos.
     

## OBJETIVO:
El objetivo del proyecto es utilizar diferentes técnicas de exploración, limpieza y análisis de datos. Con todo esto, y una vez desarrollada una hipótesis, podemos llegar a conclusiones basadas en datos sólidos, de una forma fiable.


## HIPÓTESIS:
### HIPÓTESIS 1:
La primera hipótesis que manejamos, es que durante los meses de verano hay más ataques de tiburones ya que la presencia humana en su habitat es mayor.

<img src= "Images/tib_ver2.jpg">


### HIPÓTESIS 2:
Después, desarrollamos las hipótesis de que cada año hay más ataques y que USA es el país con más ataques de todos los que manejamos.

### HIPÓTESIS 3:
Por último, creemos que el número de ataques ha ido subiendo a lo largo de los años. Para analizar esto hemos usado los datos desde el año 1900 hasta el 2018.


## ESTRUCTURA:
1. [Exploración](https://github.com/ce-valle/pandas_project/blob/main/explore.ipynb): en este cuaderno hemos realizado la exploración inicial de datos.
2. [Limpieza](https://github.com/ce-valle/pandas_project/blob/main/cleanning.ipynb): creación de nuevas bases de datos para trabajar en nuestra hipótesis y limpieza de las mismas.
3. [Análisis datos](https://github.com/ce-valle/pandas_project/blob/main/analysis.ipynb): con las tablas preparadas y los datos limpios, análizamos los datos en base a nuestras hipótesis y realizamos los gráficos que las explican.
4. [Datos](https://github.com/ce-valle/pandas_project/tree/main/Data): carpeta con todos los subsets que hemos ido manejando.
5. [Gráficas](https://github.com/ce-valle/pandas_project/tree/main/Figures): carpeta con los gráficos que hemos realizado en la fase de análisis.
6. [Funciones](https://github.com/ce-valle/pandas_project/tree/main/src): carpeta con las funciones que hemos usado durante el proceso de limpieza.


## DESARROLLO:
Durante la fase de exploración, hemos utilizado diferentes métodos de Pandas, como: `sample`, `shape`, `info`, `isnull` y `describe`.

Para la limpieza de datos y creación de subsets con los que trabajar nuestras hipótesis, hemos tenido que: renombrar columnas, `drop_duplicates` para eliminar datos duplicados,... Nos hemos centrado en la limpieza de los datos necesarios para el desarrollo de nuestras hipótesis.

En la fase final de análisis de datos hemos creado diferentes tipos de gráficas para defender las hipótesis que estábamos manejando.


## CONCLUSIÓN:
En una primera visualización, vemos que la hipótesis principal del proyecto no se cumple, sin embargo, al profundizar más en los datos y entender mejor la naturaleza de los mismos, hemos podido ver que la hipótesis era correcta.

Para más info: [Análisis](https://github.com/ce-valle/pandas_project/blob/main/analysis.ipynb)


## LIBRERÍAS:
* [Pandas](https://pandas.pydata.org/)
* [Nunpy](https://numpy.org/doc/1.18/)
* [Seaborn](https://seaborn.pydata.org/)
* [Maplotlib](https://matplotlib.org/)
* [Regex](https://docs.microsoft.com/es-es/dotnet/api/system.text.regularexpressions.regex?view=net-6.0)