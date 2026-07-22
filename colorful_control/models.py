"""Immutable domain models shared across Colorful Control.

These types describe application state without depending on a user interface,
storage format, operating system, or hardware implementation.
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class Platform(str, Enum):
    """Identify a supported application platform."""

    LINUX = "linux"
    WINDOWS = "windows"


class BackendStatus(str, Enum):
    """Describe the current availability state of a lighting backend."""

    UNAVAILABLE = "unavailable"
    READY = "ready"
    ERROR = "error"


class LightingEffect(str, Enum):
    """Identify a built-in keyboard lighting effect."""

    OFF = "off"
    SOLID = "solid"
    RAINBOW = "rainbow"
    BREATH = "breath"
    CYCLE = "cycle"
    STROBE = "strobe"


class Theme(str, Enum):
    """Identify an application interface theme preference."""

    SYSTEM = "system"
    DARK = "dark"
    LIGHT = "light"


class DomainModel(BaseModel):
    """Provide immutable, strict validation for domain value objects."""

    model_config = ConfigDict(extra="forbid", frozen=True)


class RGBColor(DomainModel):
    """Represent an immutable RGB color using 8-bit color channels."""

    red: int = Field(ge=0, le=255)
    green: int = Field(ge=0, le=255)
    blue: int = Field(ge=0, le=255)

    @property
    def as_tuple(self) -> tuple[int, int, int]:
        """Return the color channels in red, green, blue order."""

        return (self.red, self.green, self.blue)

    @property
    def hex_value(self) -> str:
        """Return the color in conventional ``#RRGGBB`` notation."""

        return f"#{self.red:02X}{self.green:02X}{self.blue:02X}"


class Brightness(DomainModel):
    """Represent an immutable keyboard brightness percentage."""

    percentage: int = Field(ge=0, le=100)


class AnimationSpeed(DomainModel):
    """Represent a positive animation speed for hardware or software effects.

    The value is intentionally unbounded above so implementations can map it
    to their native range without changing the shared domain model.
    """

    value: float = Field(gt=0, allow_inf_nan=False)


class BackendCapabilities(DomainModel):
    """Describe the lighting features available through a backend.

    The supported-effect collection uses the shared effect enum, allowing
    clients to decide which controls to expose without platform-specific
    knowledge.
    """

    supports_color: bool
    supports_brightness: bool
    supports_animation_speed: bool
    supported_effects: frozenset[LightingEffect]


class KeyboardState(DomainModel):
    """Capture an immutable snapshot of the active keyboard lighting state."""

    color: RGBColor
    brightness: Brightness
    effect: LightingEffect
    speed: AnimationSpeed
