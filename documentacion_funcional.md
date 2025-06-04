# Documento Funcional Resumido

## Objetivo General del Sistema

Desarrollar una aplicación CLI de finanzas personales y hogareñas que permita a un usuario técnico registrar, administrar y analizar sus finanzas personales y compartidas. La aplicación debe facilitar la gestión de ingresos, gastos, presupuestos y proyectos de ahorro, además de permitir análisis de datos mediante notebooks de Python.

## Principales Módulos o Funcionalidades

- Registro de transacciones (ingresos y gastos).
- Gestión de presupuestos mensuales.
- Definición y seguimiento de objetivos de ahorro.
- Generación de gráficos y reportes.
- Exportación de datos para análisis en Python.
- Predicción de gastos futuros y ajuste de presupuestos por inflación.

## Flujo de Uso Esperado

1. Registro de datos financieros.
2. Gestión de presupuestos y objetivos de ahorro.
3. Análisis y generación de reportes.
4. Exportación de datos para análisis externo.

## Reglas de Negocio Clave

- El dinero se mueve como un flujo entre cuentas y objetivos de ahorro.
- Los gastos compartidos se distribuyen según proporciones salariales.
- Categorías opcionales para transacciones con posibilidad de incorporar ML en el futuro.

## Supuestos y Restricciones

- La aplicación será utilizada en un entorno seguro y personal.
- Lenguaje principal: Python.
- Base de datos: SQLite para facilidad de uso y manejo local.

## Criterios de Éxito para el MVP

- Funcionalidad básica del menú CLI.
- Registro de ingresos y gastos personales y compartidos.
- Generación de presupuestos mensuales.
- Exportación de datos a CSV para análisis en notebooks de Python.
- Robustez y facilidad de uso.

# Tabla de User Stories

| Número de US | Nombre de la US                                 | Épica                    | Feature                       | AC                                                                                                                                                                                                                                  | Prioridad | Esfuerzo Estimado |
| ------------ | ----------------------------------------------- | ------------------------ | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ----------------- |
| 0            | Configuración Inicial del Entorno               | Configuración            | Estructura de Carpetas        | GIVEN el inicio del proyecto WHEN se configura el entorno THEN se crea la estructura de carpetas necesaria                                                                                                                          | Muy Alta  | 2                 |
| 1            | Registro de Ingresos                            | Gestión de Transacciones | Registro de Ingresos          | GIVEN que estoy en el menú de registro de ingresos WHEN ingreso la cantidad, la fuente, la fecha y una descripción THEN el ingreso se registra correctamente                                                                        | Muy Alta  | 3                 |
| 2            | Registro de Gastos Personales                   | Gestión de Transacciones | Registro de Gastos            | GIVEN que estoy en el menú de registro de gastos WHEN ingreso la cantidad, la categoría, la fecha, el método de pago y una descripción THEN el gasto se registra correctamente                                                      | Muy Alta  | 5                 |
| 3            | Registro de Gastos Compartidos                  | Gestión de Transacciones | Registro de Gastos            | GIVEN que estoy en el menú de registro de gastos compartidos WHEN ingreso la cantidad, la categoría, la fecha, el método de pago y los porcentajes de participación THEN el gasto compartido se registra y distribuye correctamente | Alta      | 8                 |
| 4            | Gestión de Presupuestos Mensuales               | Gestión de Presupuestos  | Creación de Presupuestos      | GIVEN que estoy en el menú de gestión de presupuestos WHEN defino categorías de gastos y cantidades máximas THEN el presupuesto mensual se crea correctamente                                                                       | Alta      | 8                 |
| 5            | Definición y Seguimiento de Objetivos de Ahorro | Gestión de Ahorros       | Objetivos de Ahorro           | GIVEN que estoy en el menú de objetivos de ahorro WHEN defino un objetivo con cantidad total, fecha límite y descripción THEN el objetivo de ahorro se registra correctamente                                                       | Alta      | 5                 |
| 6            | Modificación y Eliminación de Transacciones     | Gestión de Transacciones | Modificación de Transacciones | GIVEN que estoy en el menú de transacciones WHEN selecciono modificar o eliminar una transacción THEN la transacción se actualiza o elimina correctamente                                                                           | Alta      | 5                 |
| 7            | Gestión de Ingresos Recurrentes                 | Gestión de Transacciones | Ingresos Recurrentes          | GIVEN que estoy en el menú de ingresos recurrentes WHEN defino un ingreso como recurrente con frecuencia y fecha de inicio THEN el ingreso se registra automáticamente según la frecuencia definida                                 | Alta      | 5                 |
| 8            | Generación de Gráficos y Reportes               | Análisis y Reportes      | Generación de Reportes        | GIVEN que estoy en el menú de reportes WHEN selecciono generar un gráfico de ingresos y gastos THEN se genera un gráfico de barras correctamente                                                                                    | Media     | 8                 |
| 9            | Exportación de Datos a CSV                      | Análisis y Reportes      | Exportación de Datos          | GIVEN que estoy en el menú de exportación WHEN selecciono exportar datos a CSV THEN los datos se exportan correctamente en formato CSV                                                                                              | Media     | 3                 |
| 10           | Exportación de Reportes Preformateados          | Análisis y Reportes      | Exportación de Reportes       | GIVEN que estoy en el menú de exportación WHEN selecciono exportar un reporte preformateado THEN se genera un archivo con la estructura mínima esperada para análisis en Python                                                     | Media     | 5                 |
| 11           | Predicción de Gastos Futuros                    | Análisis y Reportes      | Predicción de Gastos          | GIVEN que estoy en el menú de predicción de gastos WHEN solicito una predicción de gastos futuros THEN la aplicación genera una predicción basada en datos históricos                                                               | Media     | 13                |
| 12           | Ajuste de Presupuestos por Inflación            | Gestión de Presupuestos  | Ajuste de Presupuestos        | GIVEN que estoy en el menú de ajustes de presupuesto WHEN ingreso la tasa de inflación THEN el presupuesto se ajusta correctamente según la inflación                                                                               | Baja      | 5                 |
| 13           | Registro de Gastos en Cuotas                    | Gestión de Transacciones | Registro de Gastos            | GIVEN que estoy en el menú de registro de gastos WHEN registro un gasto en cuotas con cantidad total, número de cuotas y fecha de inicio THEN el gasto se registra y se distribuye en cuotas correctamente                          | Baja      | 5                 |
| 14           | Robustez y Facilidad de Uso                     | Configuración            | Mejora Continua               | GIVEN que uso la aplicación regularmente WHEN realizo operaciones financieras THEN la aplicación es estable y fácil de usar                                                                                                         | Baja      | 8                 |
