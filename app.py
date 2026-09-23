"""VibeGuard 시드 앱 — 취약한 의존성을 일부러 고정해 둔 예제."""
import six
import urllib3


def add(left, right):
    """두 수를 더한다."""
    return left + right


def normalize_url(raw):
    """앞뒤 공백을 없애고 소문자로 맞춘다."""
    return raw.strip().lower()


def http_pool():
    """urllib3 연결 풀. 네트워크를 쓰지는 않는다."""
    return urllib3.PoolManager()


def is_py3():
    return six.PY3
