import sys
import logging

from .utils import run_tests, t

def main():
    logging.basicConfig(level=logging.INFO, format="")
    passed, tot = run_tests()

    if tot == 0:
        logging.info("no tests registered")
        return 0

    logging.info("%d passed | %d failed | %d total | %.2f%% success", passed, tot - passed, tot, 100 * passed / tot)

    if passed == tot: return 0
    else: return 1

if __name__ == "__main__":
    sys.exit(main())