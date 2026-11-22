
import app as faultshop


def test_U03_after_request_preserves_ok_response():
    original_response = faultshop.app.response_class(
        response="Operación exitosa",
        status=200
    )

    result = faultshop.after_request(original_response)

    assert result is original_response

    assert result.status_code == 200

    assert result.get_data(as_text=True) == "Operación exitosa"
