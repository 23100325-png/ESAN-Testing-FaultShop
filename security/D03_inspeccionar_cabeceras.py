"""D03 - Inspeccion local de cabeceras HTTP; no equivale a defecto validado."""
import requests

URL = "http://127.0.0.1:5000/"
CABECERAS = (
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Content-Security-Policy",
)


def main():
    respuesta = requests.get(URL, timeout=10, allow_redirects=False)
    print(f"URL: {URL}  HTTP: {respuesta.status_code}")
    print("Cabeceras recibidas:")
    for nombre, valor in respuesta.headers.items():
        print(f"  {nombre}: {valor}")
    print("Revisión:")
    for nombre in CABECERAS:
        print(f"  {nombre}: {'PRESENTE' if nombre in respuesta.headers else 'AUSENTE'}")
    print("Confirmar el hallazgo con una captura real y documentar su alcance.")


if __name__ == "__main__":
    main()
