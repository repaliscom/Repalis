---
'@repalis/cli': patch
---

Document token authentication in the help. `repalis --help` and `repalis auth --help` list `REPALIS_ACCESS_TOKEN` and `REPALIS_ENVIRONMENT` in a new ENVIRONMENT section, `repalis auth token` explains that it gives your app its own organization access token approved by a human in the browser, and "Not logged in" messages mention setting `REPALIS_ACCESS_TOKEN`.
