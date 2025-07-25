from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import os
import uuid

app = Flask(__name__)
CORS(app)

def compile_and_run_c_cpp(code_file, compiler):
    binary_path = f"/tmp/{uuid.uuid4()}.out"  # Unique output file
    compile = subprocess.run(
        [compiler, code_file, "-o", binary_path],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    if compile.returncode != 0:
        raise Exception(f"Compilation failed:\n{compile.stderr}")
    os.chmod(binary_path, 0o755)
    run = subprocess.run(
        [binary_path],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    os.remove(binary_path)  # Clean up binary
    return run

LANG_COMMANDS = {
    "python": lambda path: ["python", path],
    "java": lambda path: [
        "sh", "-c",
        f"cd {os.path.dirname(path)} && javac {os.path.basename(path)} && java Main"
    ],
    "javascript": lambda code_file: ["node", code_file]

}

@app.route("/execute", methods=["POST"])
def execute_code():
    data = request.json
    language = data.get("language")
    code = data.get("code")

    file_map = {
        "python": "main.py",
        "c": "main.c",
        "cpp": "main.cpp",
        "java": "Main.java",
        "javascript": "main.js"

    }

    filename = file_map.get(language)
    if not filename:
        return jsonify({"error": "Unsupported language"}), 400

    # Java must not be renamed
    if language == "java":
        file_path = "/tmp/Main.java"
    else:
        file_path = f"/tmp/{uuid.uuid4()}_{filename}"

    # Write code to file
    with open(file_path, "w") as f:
        f.write(code)

    try:
        if language in ["c", "cpp"]:
            compiler = "gcc" if language == "c" else "g++"
            result = compile_and_run_c_cpp(file_path, compiler)
        else:
            result = subprocess.run(
                LANG_COMMANDS[language](file_path),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=5,
                text=True
            )

        return jsonify({
            "stdout": result.stdout,
            "stderr": result.stderr
        })

    except subprocess.TimeoutExpired:
        return jsonify({"error": "Execution timed out"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        try:
            os.remove(file_path)
            if language == "java":
                class_file = os.path.join(os.path.dirname(file_path), "Main.class")
                if os.path.exists(class_file):
                    os.remove(class_file)
        except Exception as e:
            print("Cleanup error:", e)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
