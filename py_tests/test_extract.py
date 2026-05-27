from unittest.mock import patch, Mock
from src.extract import extract

def test_extract_returns():
    mock_res = Mock()
    mock_res.json.return_value = {
        "status": "ok",
        "articles": [
            {"title": "test article", "source": {"name": "test name"}}
        ]
    }
    mock_res.raise_for_status = Mock()

    with patch("src.extract.requests.get", return_value=mock_res):
        res = extract("fake_key")

    assert isinstance(res, list)
    assert len(res) == 1
    assert res[0]["title"] == "test article"

def test_extract_bad_response():
    mock_res = Mock()
    mock_res.json.return_value = {
        "status": "error",
        "code": "apikeyinvalid",
        "message": "The request is invalid."
    }
    mock_res.raise_for_status.side_effect = Exception("404")

    with patch("src.extract.requests.get", return_value=mock_res):
        try:
            extract("fake_key")
            assert False, "not raised"
        except Exception as e:
            assert "404" in str(e)