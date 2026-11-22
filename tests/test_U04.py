from unittest.mock import patch

import app as faultshop


def test_U04_servidor_smtp_no_disponible():
    with patch.object(
        faultshop.smtplib,
        "SMTP",
        side_effect=ConnectionRefusedError("SMTP server unreachable"),
    ) as smtp_mock:
        resultado = faultshop.send_reset_email(
            "liam@esan.edu.pe",
            "liam_gago",
            "token_prueba_004",
        )

    smtp_mock.assert_called_once()
    assert resultado is False or resultado is None