import sys

RESET = "\033[0m"
COLORS = {
    "DEBUG": "\033[36m",  # cyan
    "INFO": "\033[32m",  # green
    "WARNING": "\033[33m",  # yellow
    "ERROR": "\033[31m",  # red
    "CRITICAL": "\033[35m",  # magenta
}


class Logger:
    def _log(self, level: str, msg: str) -> None:
        color = COLORS.get(level, "")
        print(f"{color}{level}:{RESET} {msg}", file=sys.stderr)

    def debug(self, msg: str) -> None:
        self._log("DEBUG", msg)

    def info(self, msg: str) -> None:
        self._log("INFO", msg)

    def warning(self, msg: str) -> None:
        self._log("WARNING", msg)

    def error(self, msg: str) -> None:
        self._log("ERROR", msg)

    def critical(self, msg: str) -> None:
        self._log("CRITICAL", msg)


logger = Logger()
