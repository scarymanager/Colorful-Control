# AGENTS.md

# Colorful Control

## Overview

Colorful Control is a modern, open-source RGB keyboard control application for Colorful/Clevo laptops.

The application should support Linux first, but the architecture must be designed so Windows support can be added later without major rewrites.

The project should be modular, maintainable, and pleasant to contribute to.

---

# Goals

- Cross-platform architecture
- Linux implementation first
- Windows backend later
- Modern PySide6 GUI
- CLI interface
- System tray
- Live updates (no Apply button)
- Automatic configuration saving
- Plugin-friendly animation system
- Well documented

---

# Technology

Language:
- Python 3.12+

GUI:
- PySide6

CLI:
- Typer

Configuration:
- JSON

Testing:
- pytest

Linting:
- Ruff

Formatting:
- Ruff format

Packaging:
- pyproject.toml

---

# Project Structure

colorful_control/

    app.py
    controller.py
    config.py

    backends/
        base.py
        linux.py
        windows.py

    animations/
        base.py
        rainbow.py
        breath.py
        cycle.py
        strobe.py
        solid.py
        off.py

    gui/

    tray/

    cli/

    daemon/

tests/

docs/

assets/

---

# Architecture

Everything should communicate through a common backend interface.

GUI

↓

Controller

↓

Backend

↓

Operating System

The GUI must never access Linux or Windows APIs directly.

---

# Linux Backend

Linux should support:

- /sys/class/leds/*kbd_backlight*
- Legacy tuxedo_keyboard interface

Detect automatically which interface is available.

---

# Windows Backend

Initially create placeholders only.

Later this backend will communicate with the OEM driver or EC.

Do not assume implementation details yet.

---

# Animation System

Each animation should be its own class.

Example:

Animation

↓

RainbowAnimation

BreathAnimation

CycleAnimation

StrobeAnimation

Animations should be replaceable without modifying the GUI.

---

# GUI

Requirements:

- Modern appearance
- Native Qt widgets
- Live updates
- No Apply button
- Instant preview
- Dark mode support
- Tray support

---

# Coding Style

- Type hints everywhere
- Small functions
- Small classes
- Composition over inheritance
- Avoid global variables
- Avoid giant files
- Write clear docstrings
- Prefer readability over cleverness

---

# Git

Small focused commits.

Examples:

feat:
fix:
docs:
refactor:
test:
style:

---

# Important

Do not implement everything at once.

Always implement one feature at a time.

Prefer clean architecture over fast implementation.
