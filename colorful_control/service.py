"""Application-facing contract for coordinating keyboard lighting."""

from __future__ import annotations

from abc import ABC, abstractmethod

from colorful_control.backends.base import Backend
from colorful_control.config import ApplicationConfiguration
from colorful_control.models import (
    AnimationSpeed,
    BackendCapabilities,
    BackendStatus,
    Brightness,
    KeyboardState,
    LightingEffect,
    RGBColor,
)


class LightingService(ABC):
    """Coordinate backend, configuration, and keyboard state for clients.

    GUI and CLI layers use this Qt-free contract to read and update keyboard
    lighting. Implementations synchronize requested changes with configuration
    and expose only shared domain models to their callers.
    """

    @abstractmethod
    def __init__(
        self,
        backend: Backend,
        configuration: ApplicationConfiguration,
    ) -> None:
        """Create a service with its backend and configuration collaborators.

        Args:
            backend: The keyboard lighting backend to coordinate.
            configuration: The application's validated configuration state.
        """

    @abstractmethod
    def initialize(self) -> None:
        """Initialize the service and its coordinated backend."""

    @abstractmethod
    def shutdown(self) -> None:
        """Shut down the service and release coordinated resources."""

    @abstractmethod
    def status(self) -> BackendStatus:
        """Return the current availability status of the coordinated backend."""

    @abstractmethod
    def capabilities(self) -> BackendCapabilities:
        """Return the lighting capabilities exposed through the service."""

    @abstractmethod
    def state(self) -> KeyboardState:
        """Return the current immutable keyboard lighting state."""

    @abstractmethod
    def set_color(self, color: RGBColor) -> None:
        """Request a new keyboard color.

        Args:
            color: The immutable RGB color to make active.
        """

    @abstractmethod
    def set_effect(self, effect: LightingEffect) -> None:
        """Request a new keyboard lighting effect.

        Args:
            effect: The built-in effect to make active.
        """

    @abstractmethod
    def set_brightness(self, brightness: Brightness) -> None:
        """Request a new keyboard brightness.

        Args:
            brightness: The immutable brightness value to make active.
        """

    @abstractmethod
    def set_speed(self, speed: AnimationSpeed) -> None:
        """Request a new keyboard animation speed.

        Args:
            speed: The immutable speed value to make active.
        """

    @abstractmethod
    def load_profile(self, profile_name: str) -> None:
        """Request activation of a named lighting profile.

        Args:
            profile_name: The configuration profile identifier to activate.
        """

    @abstractmethod
    def save_profile(self, profile_name: str) -> None:
        """Request persistence of the current state under a profile name.

        Args:
            profile_name: The configuration profile identifier to save.
        """
