from flask import Flask, render_template, jsonify, request
import subprocess, tempfile, os, shutil

app = Flask(__name__)

QUESTIONS = [
    {"id": 1, "title": "Two Sum", "difficulty": "Easy", "prompt": "Given an array of integers and a target, return indices of two numbers that add up to the target.", "tag": "Arrays"},
    {"id": 2, "title": "Valid Parentheses", "difficulty": "Easy", "prompt": "Determine whether a string containing brackets is valid and properly nested.", "tag": "Stack"},
    {"id": 3, "title": "Longest Substring", "difficulty": "Medium", "prompt": "Find the length of the longest substring without repeating characters.", "tag": "Strings"},
    {"id": 4, "title": "Merge Intervals", "difficulty": "Medium", "prompt": "Merge all overlapping intervals and return the resulting non-overlapping intervals.", "tag": "Sorting"},
    {"id": 5, "title": "Binary Search", "difficulty": "Easy", "prompt": "Find the target value in a sorted array and return its index, or -1 if absent.", "tag": "Search"},
]

LANGUAGES = [
    {"id":"python","name":"Python"},{"id":"javascript","name":"JavaScript"},{"id":"typescript","name":"TypeScript"},
    {"id":"cpp","name":"C++"},{"id":"c","name":"C"},{"id":"java","name":"Java"},{"id":"go","name":"Go"},
    {"id":"rust","name":"Rust"},{"id":"csharp","name":"C#"},{"id":"php","name":"PHP"},{"id":"ruby","name":"Ruby"},
    {"id":"kotlin","name":"Kotlin"},{"id":"swift","name":"Swift"}
]

@app.route('/')
def index():
    return render_template('index.html', questions=QUESTIONS, languages=LANGUAGES)

@app.post('/api/run')
def run_code():
    data = request.get_json(silent=True) or {}
    code = data.get('code','')
    language = data.get('language','python')
    stdin = data.get('input','')
    if not code.strip(): return jsonify(ok=False, output='Code is empty.')
    if language != 'python':
        return jsonify(ok=False, output=f'{language.title()} editor is ready. Connect a secure sandbox/Judge API for execution of this language.' )
    # Local-development runner: keep this app bound to localhost. Never expose this endpoint publicly.
    try:
        p = subprocess.run(['python','-I','-S','-c',code], input=stdin, text=True, capture_output=True, timeout=3, cwd=os.getcwd())
        out = (p.stdout + p.stderr).strip()
        return jsonify(ok=p.returncode==0, output=out or ('Process finished with no output.' if p.returncode==0 else f'Process exited with code {p.returncode}.'))
    except subprocess.TimeoutExpired:
        return jsonify(ok=False, output='Time Limit Exceeded (3 seconds).')
    except Exception as e:
        return jsonify(ok=False, output=f'Runner error: {e}')

@app.get('/api/questions')
def questions(): return jsonify(QUESTIONS)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
