"""Typed, validated configuration models for Colorful Control.

This module defines the in-memory configuration schema only. Loading and
saving configuration data are intentionally left to a future persistence layer.
"""

from __future__ import annotations

from enum import Enum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StringConstraints


Identifier = Annotated[
    str,
    StringConstraints(strip_whitespace=True, min_length=1, max_length=128),
]
"""A non-empty, whitespace-trimmed configuration identifier."""


class ConfigurationModel(BaseModel):
    """Provide common validation rules for application configuration models."""

    model_config = ConfigDict(extra="forbid", validate_assignment=True)


class ThemeMode(str, Enum):
    """Represent the visual theme preference for the application interface."""

    SYSTEM = "system"
    LIGHT = "light"
    DARK = "dark"


class Theme(ConfigurationModel):
    """Store the selected application theme preference."""

    mode: ThemeMode = ThemeMode.SYSTEM


class Brightness(ConfigurationModel):
    """Store a normalized keyboard brightness setting."""

    value: int = Field(default=100, ge=0, le=100)


class Effect(ConfigurationModel):
    """Store the identifier of the selected keyboard lighting effect."""

    name: Identifier = "solid"


class Speed(ConfigurationModel):
    """Store a normalized keyboard animation-speed setting."""

    value: int = Field(default=50, ge=1, le=100)


class ActiveProfile(ConfigurationModel):
    """Store the optional name of the profile currently in use."""

    name: Identifier | None = None


class WindowState(ConfigurationModel):
    """Store the application window's persisted geometry and visibility state."""

    x: int | None = None
    y: int | None = None
    width: int = Field(default=1024, ge=1)
    height: int = Field(default=768, ge=1)
    is_maximized: bool = False


class TraySettings(ConfigurationModel):
    """Store system-tray behavior preferences."""

    enabled: bool = True
    minimize_to_tray: bool = True
    show_notifications: bool = True


class StartupSettings(ConfigurationModel):
    """Store application startup behavior preferences."""

    launch_on_login: bool = False
    start_minimized: bool = False


class ApplicationConfiguration(ConfigurationModel):
    """Collect the validated settings that make up application configuration.

    This model is deliberately independent of storage and UI technologies.
    """

    theme: Theme = Field(default_factory=Theme)
    brightness: Brightness = Field(default_factory=Brightness)
    effect: Effect = Field(default_factory=Effect)
    speed: Speed = Field(default_factory=Speed)
    active_profile: ActiveProfile = Field(default_factory=ActiveProfile)
    window: WindowState = Field(default_factory=WindowState)
    tray: TraySettings = Field(default_factory=TraySettings)
    startup: StartupSettings = Field(default_factory=StartupSettings)
