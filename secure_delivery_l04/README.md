# Secure Delivery Platform — Stage 1, Lesson 04

This directory is the initial, dependency-free service and CI baseline for a DevSecOps portfolio project. Python is used only as an easy-to-run application target; the main learning subject is CI and deployment engineering. The app can later be replaced with a Scala 3 backend.

## Requirements

- Python 3.12 or another compatible recent Python 3 version
- Git; a GitHub repository if you want to observe the remote workflow

## Run

```bash
python -m unittest discover -s tests -v
python -m compileall -q service tests
python -m service.app
# another terminal:
curl -i http://127.0.0.1:8080/healthz
curl -i http://127.0.0.1:8080/unknown
```

Expected: three tests pass, healthz returns HTTP 200 with JSON, unknown returns HTTP 404. Ctrl+C stops the server.

## Failure drill

Temporarily change the `/healthz` branch of `response_for()` to return status `503` instead of `200`. Rerun tests: one test should fail and the test runner should exit nonzero. Restore the code and rerun: all tests should pass.

## GitHub Actions

Push a branch to GitHub and open a PR targeting `master`, or push to `master` to run `.github/workflows/ci.yml`. The workflow checks out code, sets up Python, checks syntax, and runs unit tests. It does **not** deploy or verify production availability.

Security: use only placeholder values in docs; do not add credentials to the repository. `contents: read` limits the built-in GITHUB_TOKEN to repository read permission. Later lessons add secrets scanning and SAST/SCA as dedicated gates.
