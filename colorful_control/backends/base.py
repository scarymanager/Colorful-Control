"""Abstract, platform-independent keyboard lighting backend contract."""

from __future__ import annotations

from abc import ABC, abstractmethod

from colorful_control.models import (
    AnimationSpeed,
    BackendCapabilities,
    BackendStatus,
    Brightness,
    KeyboardState,
    LightingEffect,
    RGBColor,
)


class Backend(ABC):
    """Define the domain-model API implemented by every keyboard backend.

    A backend translates shared domain state into platform-specific operations.
    It does not expose platform details to callers, which allows controllers,
    user interfaces, and command-line clients to remain platform independent.
    """

    @classmethod
    @abstractmethod
    def is_supported(cls) -> bool:
        """Return whether this backend can support the current environment.

        Detection must not change keyboard state or initialize the backend.
        """

    @abstractmethod
    def initialize(self) -> None:
        """Prepare the backend for use after support has been detected.

        Implementations establish only the resources needed to serve the
        remaining backend API.
        """

    @abstractmethod
    def shutdown(self) -> None:
        """Release resources associated with an initialized backend.

        Implementations should safely handle shutdown after incomplete setup.
        """

    @abstractmethod
    def status(self) -> BackendStatus:
        """Return the backend's current availability status."""

    @abstractmethod
    def capabilities(self) -> BackendCapabilities:
        """Return the lighting features currently available from the backend."""

    @abstractmethod
    def set_color(self, color: RGBColor) -> None:
        """Set the keyboard color represented by ``color``.

        Args:
            color: The immutable RGB color to make active.
        """

    @abstractmethod
    def set_effect(self, effect: LightingEffect) -> None:
        """Set the active keyboard lighting effect.

        Args:
            effect: The shared identifier of the requested lighting effect.
        """

    @abstractmethod
    def set_brightness(self, brightness: Brightness) -> None:
        """Set the keyboard brightness represented by ``brightness``.

        Args:
            brightness: The immutable brightness value to make active.
        """

    @abstractmethod
    def set_speed(self, speed: AnimationSpeed) -> None:
        """Set the active effect speed represented by ``speed``.

        Args:
            speed: The immutable animation-speed value to make active.
        """

    @abstractmethod
    def state(self) -> KeyboardState:
        """Return an immutable snapshot of the current keyboard state."""
