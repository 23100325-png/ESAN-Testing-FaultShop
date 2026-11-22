import app as faultshop


def test_U06_after_request_preserves_not_found_response():
    original_response = faultshop.app.response_class(status=404)

    result = faultshop.after_request(original_response)

    assert result is original_response
    assert result.status_code == 404
