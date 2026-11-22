import re
from playwright.sync_api import Page, expect

def test_W01_catalogo_detalle(page: Page):

    page.goto("http://localhost:5000/")

    producto = page.locator("a.product-card").first

    expect(producto).to_be_visible()

    nombre_catalogo = producto.locator("h3").inner_text().strip()
    print("Producto del catalogo:", nombre_catalogo)

    assert nombre_catalogo != ""

    producto.click()

    expect(page).to_have_url(
        re.compile(r".*/product/\d+/?$")
    )

    nombre_detalle = page.get_by_text(
        nombre_catalogo,
        exact=True
    ).first

    expect(nombre_detalle).to_be_visible()

    texto_detalle = nombre_detalle.inner_text().strip()
    print("Producto del detalle:", texto_detalle)
    assert texto_detalle == nombre_catalogo
    print("W01: PRUEBA EXITOSA")
