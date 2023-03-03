from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("pysets")
except PackageNotFoundError:
    __version__ = "unknown"
