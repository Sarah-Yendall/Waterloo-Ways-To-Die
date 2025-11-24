# Waterloo Ways To Die

A minimal Python prototype inspired by "Dumb Ways to Die", reimagined with University of Waterloo-themed mini-challenges.

Prerequisites

- Python 3.8 or newer
- pip
- (Optional on Linux) system libraries required to build/run `pygame` from pip

Quick install

1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install Python dependencies:

```bash
python -m pip install -r requirements.txt
```

If `pygame` fails to build on Linux, install the platform dependencies first (Ubuntu/Debian):

```bash
sudo apt update
sudo apt install -y python3-dev libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev
python -m pip install -r requirements.txt
```

Run the game

```bash
python -m game.main
```

Project layout

- `game/main.py` — minimal Pygame loop, title screen, and a sample level.
- `requirements.txt` — runtime dependencies (`pygame`).

Notes & next steps

- This is an early prototype. I can add sprites, sounds, scoring, and more levels.
- If you want a packaged binary or web port, tell me which target and I'll scaffold it.
