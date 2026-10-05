# CodeDuel Flask UI

Premium dark LeetCode-style coding duel interface built with Flask, HTML/CSS/JS.

## Run
```bat
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000

## Included
- Responsive no-page-scroll layout
- Python + JavaScript + TypeScript + C/C++ + Java + Go + Rust + C# + PHP + Ruby + Kotlin + Swift language selector
- LeetCode-style editor/output split with draggable output height
- Custom input tab
- Timer, queue progress, question modal, reset/format, font controls
- Purple/indigo/magenta gradient palette from the supplied reference
- Local Python demo runner with a 3-second timeout

### Security
The Python runner executes submitted code on the local machine. Keep Flask bound to `127.0.0.1` and do not expose `/api/run` to the internet. For a public coding platform, replace it with an isolated sandbox/Judge API (Docker, Firecracker, or a dedicated execution service).
