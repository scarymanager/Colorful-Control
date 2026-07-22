"""Public keyboard lighting backend abstractions and placeholders."""

from colorful_control.backends.base import Backend
from colorful_control.backends.linux import LinuxBackend
from colorful_control.backends.windows import WindowsBackend

__all__ = ["Backend", "LinuxBackend", "WindowsBackend"]
