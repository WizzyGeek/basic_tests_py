from __future__ import annotations

import typing as _t
import logging

from . import tests

logger = logging.getLogger("tests")

def test(obj: _t.Callable) -> _t.Callable:
    tests.append(obj)
    return obj

t = test

def _run_test(func: _t.Callable[[], _t.Any]) -> bool:
    try:
        func()
    except AssertionError as ex:
        logger.exception("[X] '%s' FAILED\n===", func.__qualname__, exc_info=ex)
        return False
    except BaseException as ex:
        logger.exception("[!] '%s' ERRORED\n===", func.__qualname__, exc_info=ex)
        return False
    else:
        logger.info("[+] '%s' PASSED", func.__qualname__)
        return True

def run_tests():
    return sum(map(_run_test, tests)), len(tests)