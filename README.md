
# 🧠 Online Code Editor - POC

This project is a Proof of Concept (POC) for a **browser-based online code editor and compiler** supporting multiple programming languages. It combines:

- 🖥️ **React** with **Monaco Editor** (VS Code editor experience)
- ⚙️ **Flask** backend for code execution
- 🐳 **Docker** for containerized deployment and language runtime support

---

## 🚀 Features

- Syntax-highlighted code editing using [Monaco Editor](https://github.com/microsoft/monaco-editor)
- Multi-language support:  
  ✅ Python  
  ✅ Java
  ✅ C  
  ✅ C++   
  ✅ JavaScript (client-side execution)
- Code execution and output display
- Dockerized setup for isolated language environments
- Secure execution using temporary files and subprocesses

---

## 🛠️ Tech Stack

| Layer    | Technology         |
|----------|--------------------|
| Frontend | React, Monaco Editor, Axios |
| Backend  | Flask, Python 3, Flask-CORS |
| Runtime  | GCC, G++, OpenJDK, Python |
| DevOps   | Docker, Docker Compose |

## 🔧 Setup Instructions

### Prerequisites

- Docker & Docker Compose installed

### Run the App

```bash
git clone https://github.com/Naveen131114/editor_tool.git
cd online-code-editor-poc
docker-compose up --build
````

* Frontend: [http://localhost:3000](http://localhost:3000)
* Backend (Flask API): [http://localhost:5000](http://localhost:5000)

---

## 📦 Docker Services

* `frontend`: React app with Monaco Editor
* `backend`: Flask server capable of compiling and running code for supported languages

---

## ✅ Supported Languages

| Language   | Compiler / Interpreter |
| ---------- | ---------------------- |
| Python     | Python 3.x             |
| C          | GCC                    |
| C++        | G++                    |
| Java       | OpenJDK                |
| JavaScript | Executed in-browser    |

---

## 🧪 Testing the Editor

1. Select a language from the dropdown.
2. Edit or paste your code in the Monaco Editor.
3. Click **Run** to execute and view the output below.

---

## 🔒 Security Note

> ⚠️ This POC runs code inside Docker containers but does not sandbox execution. It is not safe for production or public deployment without additional isolation and security layers (e.g., container sandboxing, resource limits, firejail, etc).

---

## 📌 Future Enhancements

* Code sandboxing and resource constraints
* Support for input and command-line arguments
* File upload/download support
* Multi-tab editor or collaborative editing

---

## 📄 License

This project is for demonstration and educational purposes only.

---

## 👨‍💻 Author

Developed by **\[NAVEENKUMAR M]**
Full Stack Developer | Flask | React | Docker
