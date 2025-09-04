class LazyConfig:
    def __init__(self, defaults=None):
        self._defaults = defaults or {}
        self._data = {}

    def __getattr__(self, name):
        if name in self._defaults:
            print(f"[LazyConfig] Return default value for {name}")
            return self._defaults[name]
        print(f"[LazyConfig] Attribute {name!r} does not exist")
        raise AttributeError(f"No such attribute: {name}")

    def __setattr__(self, name, value):
        if name.startswith("_"):  # service attributes write directly
            super().__setattr__(name, value)
        else:
            print(f"[LazyConfig] Set {name} = {value}")
            self._data[name] = value

    def __getattribute__(self, name):
        if not name.startswith("_"):
            data = super().__getattribute__("_data")
            if name in data:
                return data[name]
        return super().__getattribute__(name)


cfg = LazyConfig(defaults={"debug": False, "port": 8080})

print(cfg.debug)
print(cfg.port)

cfg.debug = True
print(cfg.debug)
print(cfg.host)
