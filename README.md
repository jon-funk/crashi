# crashi
A tiny app for use in reliability testing, allowing you to test against an app which "reliably crashes" when you expect it to, in a reproducible fashion.

# Usage
A brief usage example in a Kubernetes cluster:
[WIP]
- Pull the image from the public registry: TBD
- Deploy it in your testing `namespace` in your `Kubernetes` cluster. You can use this [sample manifest]() with `kubectl apply`

`Note:` The `liveness` and `readiness` probes are important, as they allow kubernetes pod orchestration mechanisms to kick off and produce interesting metrics.