from app import add, http_pool, is_py3, normalize_url


def test_add():
    assert add(2, 3) == 5


def test_normalize_url():
    assert normalize_url("  https://Example.com  ") == "https://example.com"


def test_is_py3():
    assert is_py3() is True


def test_http_pool_created():
    assert http_pool() is not None
