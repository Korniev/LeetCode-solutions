class Config:
    _instance = None
    _initialized = False

    def __new__(cls, settings: dict):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, settings: dict):
        if not self._initialized:
            self._settings = dict(settings)
            Config._initialized = True

    def __getitem__(self, key):
        return self._settings[key]

    def __setitem__(self, key, value):
        self._settings[key] = value

    def __delitem__(self, key):
        del self._settings[key]

    def __contains__(self, key):
        return key in self._settings

    def __iter__(self):
        return iter(self._settings)

    def __repr__(self):
        return f"Config({self._settings!r})"

    def get(self, key, default=None):
        return self._settings.get(key, default)

    def set(self, key, value):
        self._settings[key] = value
        return self


config1 = Config({"debug": True, "port": 8080})
config2 = Config({"debug": False, "port": 5000})

print(config1 is config2)         # True
print(config1["port"])            # 8080
config2["debug"] = False
print(config1["debug"])           # False
print("port" in config1)          # True
del config1["port"]
print(config1)
