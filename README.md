# API Error Debugger

A lightweight Python utility to test API endpoints, capture errors, and generate clean debug logs — ideal for QA, developers, and Customer Success teams working with public-facing APIs.

---

### 💡 Why I Built This

In SaaS, not all API issues are infrastructure-related — sometimes it’s the wrong payload, auth headers, or endpoints. I built this tool to simulate, capture, and log API failures so I can help devs and support teams pinpoint issues fast.

---

### ⚙️ Features

- Test any REST API endpoint
- Log all failed requests with code + message
- Generate readable logs with timestamps and trace IDs
- Lightweight and fast — no dependencies beyond `requests`

---

### 🧪 Run Example

```bash
python api_debugger.py https://api.example.com/data
📁 Sample Log Output
pgsql
Copy
Edit
[2025-08-13 11:02:31] ERROR 500: Internal Server Error at /api/user/login
Details: {"message": "Unexpected server failure", "code": "E500X", "trace_id": "abc123xyz"}
🛠 Requirements
Python 3.8+

requests library

🚀 Use Cases
API monitoring & QA

Customer Success troubleshooting

Log-based support ticket evidence

Quick smoke tests before frontend handoff

