from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="YoYoRace F1 Analytics")


@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>YoYoRace - F1 Analytics</title>
        <style>
            body { font-family: system-ui, sans-serif; max-width: 800px; margin: 50px auto; padding: 20px; }
            h1 { color: #e10600; }
            .card { border: 1px solid #ddd; border-radius: 8px; padding: 20px; margin: 15px 0; }
            a { color: #e10600; }
        </style>
    </head>
    <body>
        <h1>🏎️ YoYoRace F1 Analytics</h1>
        <p>Pet project for experiments with F1 telemetry and session data.</p>

        <div class="card">
            <h3>📊 Dashboards</h3>
            <p><a href="https://app.yoyorace.tech">Streamlit Dashboards →</a></p>
        </div>

        <div class="card">
            <h3>🔧 Infrastructure</h3>
            <p><a href="https://af.yoyorace.tech">Airflow (admin only)</a></p>
            <p><a href="https://etl.yoyorace.tech">Spark UI (admin only)</a></p>
        </div>

        <div class="card">
            <h3>📡 API Health</h3>
            <p>Status: <span style="color: green;">● Online</span></p>
        </div>
    </body>
    </html>
    """


@app.get("/health")
async def health():
    return {"status": "ok", "service": "yoyorace-api"}