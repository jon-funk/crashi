# crashi
A tiny app for use in reliability testing, allowing you to test against an app which "reliably crashes" when you expect it to, in a reproducible fashion.

# Usage
A brief usage example in a Kubernetes cluster:
[WIP]
- Pull the image from the public registry: `docker pull ghcr.io/jon-funk/crashi:latest`
- Deploy it in your testing `namespace` in your `Kubernetes` cluster. You can use this [sample manifest](https://github.com/jon-funk/crashi/blob/main/sample_manifest.yaml) with `kubectl apply`
- Set the environment variable CRASH_SCHEDULE to a crontab (space delimited) schedule for when you'd like the app health endpoint to fail. eg: `0-30 * * * *` will cause failures for the first 30 minutes of every hour.

`Note:` Having `liveness` and `readiness` probes are important, as they allow kubernetes pod orchestration mechanisms to kick off and produce interesting metrics.