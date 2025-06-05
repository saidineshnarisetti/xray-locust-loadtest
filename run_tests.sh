#!/bin/bash

echo "⚙️  Running JFrog test sequence..."

rm .names.json
sleep 2

PYTHONPATH=. python3 tests/create_repo.py
sleep 2

PYTHONPATH=. python3 tests/check_repo_existence.py
sleep 2

PYTHONPATH=. python3 tests/create_policy.py
sleep 2

PYTHONPATH=. python3 tests/create_watch.py
sleep 2

PYTHONPATH=. python3 tests/apply_watch.py
sleep 2

PYTHONPATH=. python3 tests/violations.py

echo "✅ All tests completed."
