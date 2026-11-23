
"""W02 - Buscar un producto existente (original, Esteban)."""
from playwright.sync_api import Page, expect


def test_W02_buscar_producto_existente(page: Page):
    page.goto("http://localhost:5000/")
    page.locator('input[name="q"]').fill("Wireless Mouse")
    page.get_by_role("button", name="Search").click()

    producto = page.locator('a.product-card').filter(
        has_text="Wireless Mouse"
    )

    expect(producto).to_have_count(1)
    expect(producto).to_be_visible()

    print("W02: Wireless Mouse encontrado en resultados")

    page.screenshot(
        path="screenshots/W02_resultado.png",
        full_page=True
    )

    page.wait_for_timeout(10000)
