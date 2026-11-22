from email import message_from_string
from unittest.mock import MagicMock, patch

import app as faultshop


def test_U09_generar_enlace_recuperacion_con_usuario_y_token():
    smtp_mock = MagicMock()
    smtp_mock.__enter__.return_value = smtp_mock

    to_email = "liam@esan.edu.pe"
    username = "liam_gago"
    token = "tok_seguro_009"
    enlace_esperado = (
        f"http://172.17.0.1:5000/reset-password?step=reset&token={token}&username={username}"
    )

    with patch.object(faultshop.smtplib, "SMTP", return_value=smtp_mock):
        faultshop.send_reset_email(to_email, username, token)

    smtp_mock.sendmail.assert_called_once()
    mensaje_enviado = message_from_string(smtp_mock.sendmail.call_args[0][2])
    cuerpo_texto = mensaje_enviado.get_payload()

    assert mensaje_enviado["To"] == to_email
    assert enlace_esperado in cuerpo_texto