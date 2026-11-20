# @repalis/cli

## 3.2.0

### Minor Changes

- 26572db: Add `repalis agent setup`, which detects Claude Code, Codex and Cursor and installs the Repalis plugin, MCP servers and skills for each.

## 3.1.0

### Minor Changes

- d3ae634: `repalis --help` lists every command, and `repalis <command> --help` shows the flags of every command under it at once.

### Patch Changes

- 2e2c654: `benefits update`, `customers update`, `customers update_external`, `customers members update`, `customers members update_external` and `products update_benefits` ask for confirmation, or `--confirm` without a terminal.

## 3.0.0

### Major Changes

- dd16120: `repalis listen` and `repalis trigger` are now `repalis webhook listen` and `repalis webhook trigger`. Add `repalis auth token` to create an organization access token through the dashboard. Add `--json` to every command and `--fields` to trim API command output. Destructive API commands ask for confirmation, or `--confirm` without a terminal.

### Patch Changes

- cc6f9f5: Mark `repalis webhooks reset_webhook_endpoint_secret` as destructive so it requires user confirmation.

## 2.0.2

### Patch Changes

- 77b0d35: Fix `create` commands failing with organization access tokens when `--org` is passed. The CLI sent `organization_id` in the request body, which organization tokens reject; it now sends the organization only in the `Repalis-Organization` header.
- 9d2f5c8: Require confirmation when resuming a paused subscription with the CLI, since resuming starts a new billing period and charges the customer immediately.
- 4155d8e: Update `@repalis/sdk` to version 1.0.2.

## 2.0.1

### Patch Changes

- 96ac1df: Support detecting and updating CLI installations managed by Vite+ (`vp`).

## 2.0.0

### Major Changes

- d107912: **API resources.** Manage your Repalis data straight from the terminal: `repalis customers`, `products`, `orders`, `subscriptions`, `checkouts`, `discounts`, `benefits`, `meters`, `webhooks` and more.

  **`repalis trigger`.** Send test webhook events to your app.

  **`repalis listen`.** Forward webhooks to a port (`repalis listen 3000`) or a URL and see how your server responded to each event.

  **Auth.** `repalis login` and `repalis logout` are now `repalis auth login` and `repalis auth logout`. Use `repalis auth whoami` to see who you're logged in as and `repalis auth org` to switch organizations.

  **Agentic experience.** JSON output (by default for API resources, with `--json` everywhere else), no hanging prompts, and errors that tell an agent exactly what to fix.

  **Everything else.** Type `repalis` to see your account and active org. Windows works without WSL.
