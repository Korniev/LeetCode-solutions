import time
from copy import deepcopy
from pathlib import Path
from typing import Optional, Any, MutableMapping


# Context manager tracker
class Timer:
    def __init__(self, label: Optional[str] = "Timer", print_on_exit: bool = True):
        self.label = label
        self.print_on_exit = print_on_exit
        self.start = None
        self.elapsed = None

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self.start
        if self.print_on_exit and self.label:
            print(f"[{self.label}] {self.elapsed:.6f}s")
        return False


with Timer("sum10m") as timer:
    sum(range(1000000))
print(timer.elapsed)


# Context manager safe open file
class SafeOpen:
    def __init__(self, filename: str | Path, mode: str = "r", encoding: str = "utf-8"):
        self.filename = Path(filename)
        self.mode = mode
        self.encoding = encoding
        self.file = None

    def __enter__(self):
        if any(m in self.mode for m in ("w", "a", "x")):
            self.filename.parent.mkdir(parents=True, exist_ok=True)
        if "b" in self.mode:
            self.file = open(self.filename, self.mode)
        else:
            self.file = open(self.filename, self.mode, encoding=self.encoding)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file and not self.file.closed:
            try:
                self.file.close()
            finally:
                self.file = None
        return False

    def __repr__(self):
        return f"SafeOpen({str(self.filename)!r}, {self.mode!r})"


with SafeOpen("test.txt", "w") as file:
    print(repr(file))
    file.write("Hello, world!")


# Context manager for Config Transaction
class ConfigTransaction:
    def __init__(self, config: MutableMapping[str, Any], *, deep: bool = False, **overrides: Any):
        self.config = config
        self.overrides = overrides
        self._original: MutableMapping[str, Any]
        self._deep = deep

    def __enter__(self):
        self._original = deepcopy(self.config) if self._deep else self.config.copy()
        self.config.update(self.overrides)
        return self.config

    def __exit__(self, exc_type, exc_val, exc_tb):
        assert self._original is not None
        self.config.clear()
        self.config.update(self._original)
        return False


config = {"a": 1, "b": 2}
with ConfigTransaction(config, a=3, b=4) as cfg:
    print(cfg)  # {'a': 3, 'b': 4}
print(config)
