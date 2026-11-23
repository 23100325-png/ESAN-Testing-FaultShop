
from playwright.sync_api import Page, expect


def test_W03_rechazar_password_incorrecta(page: Page):
    page.goto("http://localhost:5000/login")

    expect(page.locator("input[name='username']")).to_be_visible()
    expect(page.locator("input[name='password']")).to_be_visible()

    page.locator("input[name='username']").fill("carlos")
    page.locator("input[name='password']").fill(
        "clave_incorrecta_123"
    )

    page.get_by_role("button", name="Sign in").click()

    expect(page.locator(".alert-error")).to_have_text(
        "Invalid credentials"
    )

    expect(page).to_have_url("http://localhost:5000/login")

    print("W03: contraseña incorrecta rechazada correctamente")
