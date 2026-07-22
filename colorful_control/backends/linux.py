"""Placeholder implementation for the Linux keyboard backend."""

from __future__ import annotations

from colorful_control.backends.base import Backend


class LinuxBackend(Backend):
    """Reserve the Linux-specific implementation of the shared backend API.

    This class intentionally remains abstract until hardware integration is
    designed. It inherits the complete platform-neutral contract from
    :class:`~colorful_control.backends.base.Backend`.
    """

    # TODO: Implement the abstract backend contract for Linux.
