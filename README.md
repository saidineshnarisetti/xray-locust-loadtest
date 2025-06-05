🧪 JFrog Xray Load Testing with Locust
📋 Prerequisites
Python 3.8+

Docker (for pushing test images)

JFrog trial account

⚙️ Setup
Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate
Install dependencies:


```pip install -r requirements.txt```
🚀 Running Locust
To start the Locust web UI:

```locust -f locustfile.py```
Then open your browser and go to: http://localhost:8089

🧪 Load Test Workflow
The test simulates the following scenario:

✅ Create Docker repository

✅ Push Docker image (run manually via docker_image.sh)

✅ Create policy and watch

✅ Apply the watch to the repository

✅ Trigger a scan

✅ Retrieve violations

📈 Load Patterns
1. Gradual Ramp-Up (Realistic Growth)
👥 Users: 50

🚀 Spawn Rate: 5 users/sec

⏱️ Run Time: 5 minutes

Use Case: Simulates steady user onboarding or normal traffic growth.

2. Spike Test (Sudden Load Burst)
👥 Users: 100

🚀 Spawn Rate: 100 users/sec

⏱️ Run Time: 2 minutes

Use Case: Stress test for traffic bursts (e.g., marketing campaigns or releases).

🧑‍💻 Running in Headless Mode (CI/CD or CLI)

```
locust -f locustfile.py \
  --headless \
  --users 10 \
  --spawn-rate 2 \
  --run-time 1m \
  --host https://trialf6dxqy.jfrog.io \
  --html report.html \
  --csv report
```

This will generate report.html, report_stats.csv, and report_failures.csv for analysis.

📊 Reporting
Run tests via the browser or CLI (headless mode).

Download metrics directly from the UI.

Customize export (JSON, CSV) using Locust event hooks.
