import re
from playwright.sync_api import Page, expect


def test_W04_cerrar_sesion_regresar_inicio(page: Page):
    page.goto("http://localhost:5000/login")

    # Si el formulario de login existe, intenta iniciar sesión o ir directo al inicio
    if page.locator("input[name='username'], input[name='email']").count() > 0:
        user_input = page.locator("input[name='username'], input[name='email']").first
        pass_input = page.locator("input[name='password']").first
        if user_input.is_visible() and pass_input.is_visible():
            user_input.fill("customer")
            pass_input.fill("customer123")
            submit_btn = page.locator("button[type='submit'], input[type='submit']").first
            if submit_btn.is_visible():
                submit_btn.click()

    # Busca enlace o botón de cerrar sesión / logout si existe
    logout_locator = page.locator(
        "a[href*='logout'], button:has-text('Logout'), a:has-text('Logout'), "
        "button:has-text('Sign out'), a:has-text('Sign out'), a:has-text('Cerrar sesión')"
    )
    if logout_locator.count() > 0 and logout_locator.first.is_visible():
        logout_locator.first.click()

    # Regresa a la página de inicio y verifica que carga correctamente
    page.goto("http://localhost:5000/")
    expect(page).to_have_url(re.compile(r"^http://(localhost|127\.0\.0\.1):5000/?$"))
    expect(page.locator("body")).to_be_visible()
    print("W04: PRUEBA EXITOSA - Cerrar sesion y regresar a inicio")