from email import message_from_string
from unittest.mock import MagicMock, patch

import app as faultshop


def test_U05_send_reset_email_sends_password_reset_message():
    recipient = "customer@example.com"
    smtp = MagicMock()
    smtp.__enter__.return_value = smtp

    with patch.object(faultshop.smtplib, "SMTP", return_value=smtp) as smtp_class:
        faultshop.send_reset_email(recipient, "customer", "reset-token")

    smtp_class.assert_called_once_with(faultshop.MAIL_SERVER, faultshop.MAIL_PORT)
    smtp.sendmail.assert_called_once()
    sent_message = message_from_string(smtp.sendmail.call_args[0][2])

    assert sent_message["Subject"] == "Password reset - FaultShop"
    assert smtp.sendmail.call_args[0][1] == recipient
    assert sent_message["To"] == recipient
