Tenemos el fichero clientes.csv con datos sensibles y necesitamos pasárselo al equipo de desarrollo para que haga pruebas, pero queremos aplicar data masking sobre determinadas columnas. El data masking consistiría en sustituir por el carácter X cada una de las letras de las columnas alfanuméricas (y mantener los símbolos como @, ., -,…) y por el valor medio del total en las columnas numéricas. Las columnas sensibles son “Nombre”, “Email” y “Facturado”. La salida se llamará clientes_masked.csv y tendrá las mismas columnas que clientes.csv.
Ejemplo:
* juan@mail.com pasaría a ser XXXX@XXXX.XXX. Esto es, mantiene la longitud y el formato.
* Si tenemos 2 filas de facturación con valores de 10 y 5, pasarán a valer ambas 7.5


El mismo proceso de masking se utilizará en un futuro para aplicarlo sobre tablas de una base de datos. Cuanto más reutilizable sea, mejor.

Bonus:

* Crear un informe en el que se muestre, por consola:
    * Longitud media, máxima y mínima del campo Nombre
    * Valor medio, máximo y mínimo del campo Facturación
* Pruebas unitarias.

Notas:

* Es muy importante la calidad del código.
* No utilizar ninguna dependencia externa más allá de lo que de por defecto el entorno de ejecución.
* Escribir un readme.md con las instrucciones de ejecución


