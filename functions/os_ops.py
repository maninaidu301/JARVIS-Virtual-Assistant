import os
import subprocess as sp
from pathlib import Path


# ==========================================
# APPLICATION PATHS
# ==========================================

paths = {
    "notepad": r"C:\Program Files\Notepad++\notepad++.exe",
    "calculator": r"C:\Windows\System32\calc.exe"
}


# ==========================================
# OPEN NOTEPAD++
# ==========================================

def open_notepad():
    """Open Notepad++ if installed."""

    notepad_path = paths["notepad"]

    if os.path.exists(notepad_path):
        os.startfile(notepad_path)
    else:
        print("Notepad++ was not found. Opening Windows Notepad instead.")
        os.system("start notepad")


# ==========================================
# OPEN DISCORD
# ==========================================

def open_discord():
    """Open Discord using its standard installation paths."""

    local_app_data = os.environ.get("LOCALAPPDATA", "")

    possible_paths = [
        os.path.join(local_app_data, "Discord", "Update.exe"),
        os.path.join(local_app_data, "Discord", "app-1.0.9003", "Discord.exe")
    ]

    # Try the Discord updater first.
    updater = possible_paths[0]

    if os.path.isfile(updater):
        sp.Popen([updater, "--processStart", "Discord.exe"])
        return

    # Try a directly installed Discord executable.
    for discord_path in possible_paths[1:]:
        if os.path.isfile(discord_path):
            os.startfile(discord_path)
            return

    # Try the Discord protocol handler.
    try:
        os.startfile("discord://")
    except OSError:
        print("Discord was not found. Please check its installation.")


# ==========================================
# OPEN COMMAND PROMPT
# ==========================================

def open_cmd():
    """Open Windows Command Prompt."""

    sp.Popen(["cmd.exe"])


# ==========================================
# OPEN WINDOWS CAMERA
# ==========================================

def open_camera():
    """Open the Windows Camera application."""

    try:
        sp.Popen(
            [
                "cmd",
                "/c",
                "start",
                "",
                "microsoft.windows.camera:"
            ],
            shell=False
        )
    except OSError as error:
        print(f"Could not open the camera: {error}")


# ==========================================
# OPEN CALCULATOR
# ==========================================

def open_calculator():
    """Open the Windows Calculator."""

    calculator_path = paths["calculator"]

    try:
        if os.path.isfile(calculator_path):
            sp.Popen([calculator_path])
        else:
            os.startfile("calculator:")
    except OSError as error:
        print(f"Could not open the calculator: {error}")