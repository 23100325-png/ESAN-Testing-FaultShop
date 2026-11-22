
# Proyecto Final - Prueba de Software ESAN

Repositorio colaborativo para realizar pruebas sobre FaultShop.

## Integrantes
- Romario Huamani Paccaya
- Estefano Esteban Villacorta Garcia
- Kiara Angelita Ruiz Vásquez
- Liam Gago Coronel

## Herramientas
- pytest: pruebas unitarias
- Playwright: pruebas funcionales web
- Bruno: pruebas API
- k6: pruebas de rendimiento
- Kiwi TCMS: gestión de pruebas

## Casos desarrollados
- U01: Conexión a base de datos con ruta inválida
- U05: Asunto de correo de recuperación, asistido por IA
- U06: Conservación de respuesta HTTP 404, asistido por IA

## Preparación del entorno

Instalar Python y Docker Desktop.

Crear entorno virtual:

    py -m venv .venv

Instalar dependencias:

    .\.venv\Scripts\python.exe -m pip install -r requirements.txt pytest

Iniciar FaultShop:

    docker compose up -d

Ejecutar las pruebas unitarias:

    .\.venv\Scripts\python.exe -m pytest tests/ -v

## Aplicación original

FaultShop fue desarrollado por César R. Beltrán-Hernández.

Repositorio original:
https://github.com/CesarBeltran/faultshop

Se conserva la licencia original CC BY-NC 4.0.
Este repositorio se utiliza exclusivamente para fines académicos.
