# JFrog Xray Load Testing with Locust

## Prerequisites
- Python 3.8+
- Docker installed
- JFrog trial account setup

## Setup
```bash
pip3 install -r requirements.txt
```

## Run Locust
```bash
source venv/bin/activate
locust -f locustfile.py
```

## Load Test Scenario
- Create Docker repository
- Push Docker image (do this manually using `docker_image.sh`)
- Create policy & watch
- Apply watch
- Check scan status
- Fetch violations

## Report
Run tests via browser at http://localhost:8089
Export results from UI or extend for CSV/json using Locust event hooks.

## Load Injection Pattern
✅ 1. Gradual Ramp-Up (Realistic User Growth)
Use case: Simulate users logging in over time.

Users: 50
Spawn rate: 5 (10 seconds to reach full load)
Runtime: 5m

✅ 2. Spike Test (Sudden Load Burst)
Use case: Test how system handles a sudden traffic spike (e.g., product launch).

Users: 100
Ramp up: 100 (spawn instantly)
Runtime: 2m

To run in Head-less mode:
locust -f locustfile.py \
  --headless \
  --users 10 \
  --spawn-rate 2 \
  --run-time 1m \
  --host https://trialf6dxqy.jfrog.io \
  --html report.html \
  --csv report