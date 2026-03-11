import React, { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [email, setEmail] = useState("");
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
  if (!file || !email) {
    alert("Please select a file and enter email.");
    return;
  }

  const formData = new FormData();
  formData.append("file", file);
  formData.append("email", email);

  try {
    setLoading(true);

    const response = await axios.post(
      "http://localhost:8000/upload",
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }
    );

    setSummary(response.data.summary);
  } catch (error) {
    console.error(error);
    alert("Error uploading file");
  }

  setLoading(false);
};

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>Sales Insight Automator</h1>

      <p>Upload a CSV sales file and receive an AI-generated summary.</p>

      <input
        type="file"
        accept=".csv"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br /><br />

      <input
        type="email"
        placeholder="Enter recipient email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />

      <br /><br />

      <button onClick={handleUpload}>
        {loading ? "Processing..." : "Upload"}
      </button>

      <br /><br />

      {summary && (
        <div>
          <h3>Summary</h3>
          <pre>{summary}</pre>
        </div>
      )}
    </div>
  );
}

export default App;