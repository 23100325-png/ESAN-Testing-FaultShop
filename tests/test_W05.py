from playwright.sync_api import Page, expect


def test_W05_busqueda_producto_inexistente(page: Page):
    page.goto("http://localhost:5000/")
    page.locator('input[name="q"]').fill("ProductoInexistente987654")
    page.get_by_role("button", name="Search").click()

    expect(page.locator("p.no-results")).to_contain_text("No results for")
    expect(page.locator("a.product-card")).to_have_count(0)

    page.screenshot(path="screenshots/W05_resultado.png", full_page=True)
    page.wait_for_timeout(8000)