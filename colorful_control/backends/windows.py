"""Placeholder implementation for the Windows keyboard backend."""

from __future__ import annotations

from colorful_control.backends.base import Backend


class WindowsBackend(Backend):
    """Reserve the Windows-specific implementation of the shared backend API.

    This class intentionally remains abstract until hardware integration is
    designed. It inherits the complete platform-neutral contract from
    :class:`~colorful_control.backends.base.Backend`.
    """

    # TODO: Implement the abstract backend contract for Windows.
