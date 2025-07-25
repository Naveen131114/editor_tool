import React, { useState } from "react";
import Editor from "@monaco-editor/react";
import axios from "axios";

const defaultCodes = {
  python: "print('Hello from Python')",
  c: "#include <stdio.h>\nint main() { printf(\"Hello from C\\n\"); return 0; }",
  cpp: "#include <iostream>\nint main() { std::cout << \"Hello from C++\" << std::endl; return 0; }",
  java: "public class Main { public static void main(String[] args) { System.out.println(\"Hello from Java\"); }}",
  javascript: `<!DOCTYPE html>
<html>
<body>
<h2>The var Keyword Creates Variables</h2>
<p id="demo"></p>
<script>
  var x = 5 + 6;
  var y = x * 10;
  document.getElementById("demo").innerHTML = y;
</script>
</body>
</html>`
};

function App() {
  const [language, setLanguage] = useState("python");
  const [code, setCode] = useState(defaultCodes["python"]);
  const [output, setOutput] = useState("");

  const runCode = async () => {
    if (language === "javascript") {
      setOutput(code); // Render HTML/JS inside iframe
    } else {
      try {
        const res = await axios.post("http://localhost:5000/execute", {
          language,
          code,
        });
        setOutput(res.data.stdout || res.data.stderr || res.data.error || "No output");
      } catch (err) {
        setOutput("Error executing code.");
      }
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Multi-Language Code Editor</h1>

      <select
        value={language}
        onChange={(e) => {
          setLanguage(e.target.value);
          setCode(defaultCodes[e.target.value]);
          setOutput(""); // clear output when changing language
        }}
      >
        <option value="python">Python</option>
        {/* <option value="c">C</option> */}
        {/* <option value="cpp">C++</option> */}
        <option value="java">Java</option>
        <option value="javascript">Javascript</option>
      </select>

      <Editor
        height="300px"
        defaultLanguage={language === "cpp" ? "cpp" : language}
        language={language === "cpp" ? "cpp" : language}
        value={code}
        onChange={(value) => setCode(value)}
      />

      <button onClick={runCode} style={{ marginTop: 10 }}>
        Run
      </button>

      <div style={{ marginTop: 20 }}>
        {language === "javascript" ? (
          <iframe
            title="Output"
            srcDoc={output}
            sandbox="allow-scripts"
            style={{ width: "100%", height: "300px", border: "1px solid #ccc" }}
          />
        ) : (
          <pre style={{ backgroundColor: "#eee", padding: 10 }}>{output}</pre>
        )}
      </div>
    </div>
  );
}

export default App;
