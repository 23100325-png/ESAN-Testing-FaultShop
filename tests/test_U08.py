from unittest.mock import MagicMock, patch

import app as faultshop


def test_U08_rechazo_destinatario_smtp_no_interrumpe_envio():
    recipient = "customer@example.com"
    smtp = MagicMock()
    smtp.__enter__.return_value = smtp
    smtp.sendmail.side_effect = faultshop.smtplib.SMTPRecipientsRefused(
        {recipient: (550, b"Recipient address rejected")}
    )

    with patch.object(faultshop.smtplib, "SMTP", return_value=smtp) as smtp_class:
        result = faultshop.send_reset_email(recipient, "customer", "reset-token")

    smtp_class.assert_called_once_with(faultshop.MAIL_SERVER, faultshop.MAIL_PORT)
    smtp.sendmail.assert_called_once()
    assert result is None
