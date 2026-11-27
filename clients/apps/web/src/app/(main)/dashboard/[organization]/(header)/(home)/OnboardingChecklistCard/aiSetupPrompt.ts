import { CONFIG } from '@/utils/config'
import { schemas } from '@repalis/client'

export const buildAiSetupPrompt = (
  organization: schemas['Organization'],
): string => {
  const environment = CONFIG.IS_SANDBOX ? 'sandbox' : 'production'
  const dashboardUrl = `${CONFIG.FRONTEND_BASE_URL}/dashboard/${organization.slug}`
  const apiUrl = CONFIG.BASE_URL
  const testInstruction = CONFIG.IS_SANDBOX
    ? 'It is payable with the test card 4242 4242 4242 4242, any future expiry and CVC.'
    : 'To test end-to-end without a real charge, create a 100% discount code via the discounts API; enter that code on the Repalis checkout page (a plain checkout link cannot pre-apply it).'
  const goLiveNote = CONFIG.IS_SANDBOX
    ? 'the go-live steps (create a production organization and token at repalis.com, register the production webhook URL, set REPALIS_SERVER=production)'
    : 'a reminder that this integration runs against the live production environment'

  return `# Set up Repalis payments in this project

You are integrating Repalis (https://repalis.com) — checkout and webhooks — into the codebase in the current working directory. Work through the phases below strictly in order, completing and verifying each phase before starting the next.

## Provided values — use these; never invent IDs, tokens, or URLs
- Organization: ${organization.slug} (id: ${organization.id})
- Environment: ${environment}
- Dashboard: ${dashboardUrl}
- API base: ${apiUrl}

If a value you need is not listed above, not in .env, and not returned by a Repalis API call you made, stop and ask the user — do not guess.

## Rules
1. Secrets must never appear in this conversation, in source code, or in command output. Never ask the user to paste a secret into chat — they edit .env themselves, or you pipe API responses into .env without printing them.
2. Read every file before editing it (for .env, check only which keys are present, not their values). Make minimal diffs that match the project's existing style.
3. Use the project's package manager, detected from lockfiles: pnpm-lock.yaml means pnpm, bun.lock or bun.lockb means bun, yarn.lock means yarn, package-lock.json means npm, uv.lock means uv, poetry.lock means poetry, otherwise pip.
4. Your training data about Repalis may be outdated. Before writing integration code, fetch the current instructions and follow them over memory:
   - https://raw.githubusercontent.com/repaliscom/agent-toolkit/main/skills/repalis-integration/SKILL.md — the canonical integration guide. It wires up checkout, customer portal, and webhooks with @repalis/sdk directly and lists per-framework variations (Next.js, SvelteKit, Nuxt, Astro, Hono, Express, Fastify, Elysia, and more). It is written for JS/TS; for Python, apply the same approach with the repalis-sdk package.
   - https://repalis.com/docs/llms.txt (an index of every docs page; fetch the API-reference pages you need, e.g. product or checkout creation).
   Important: build this on @repalis/sdk directly, even where the skill or docs show a per-framework @repalis/<framework> adapter (e.g. @repalis/nextjs). Using the SDK everywhere keeps the setup consistent across frameworks and languages.

## Phase 1 — Detect
Identify the stack: JS/TS (next, @sveltejs/kit, nuxt, astro, @remix-run/*, hono, express, fastify, elysia, or @tanstack/react-start in package.json) or Python (fastapi, django, or flask in pyproject.toml / requirements*.txt, or manage.py). Note TypeScript vs JavaScript, the src/ layout, and for Next.js which router (App vs Pages). In a monorepo, ask which app to integrate. If you can't find a supported framework, tell the user which stacks are supported and stop rather than guessing. Report findings in two lines, then ask the only setup question now so the user can think while you work: "Does this app have a public HTTPS URL I can register for webhooks (deployed or tunneled)? If not, I'll leave webhook registration for deploy time."

## Phase 2 — Environment & token
1. Ensure .env exists and is listed in .gitignore (fix if not).
2. Add REPALIS_ACCESS_TOKEN=, REPALIS_WEBHOOK_SECRET=, and REPALIS_SERVER=${environment} entries if absent.
3. Ask the user to create an organization access token at ${dashboardUrl}/settings (scopes: products, checkouts, and webhooks — read and write) and paste it into .env as REPALIS_ACCESS_TOKEN directly in their editor, not into this chat. Wait for confirmation.
4. Verify without exposing it: make an authenticated GET to ${apiUrl}/v1/products/?limit=1 (note the trailing slash — the API 307-redirects to it) reading the token from .env, following redirects, and treat any 2xx as success. On 401 or 403, remind the user that the token must be created in the ${environment} environment (sandbox and production are separate) with the scopes listed above, then retry.

## Phase 3 — Install
Install the Repalis SDK for the language: @repalis/sdk (JS/TS) or repalis-sdk (Python). Do not add a per-framework @repalis/<framework> adapter — the SDK covers every framework. (Non-Repalis helpers your framework genuinely needs are fine — e.g. in Python add a .env loader such as python-dotenv, since Python frameworks don't auto-load .env the way Next.js does; call it at startup.) Construct a single SDK client and reuse it across the routes, reading the environment from REPALIS_SERVER (sandbox or production).

## Phase 4 — Routes
Following the repalis-integration skill (use the variation for your framework), create these two routes with the SDK client (paths per the framework's conventions). The client's server comes from REPALIS_SERVER — do not hardcode it, so switching environments later is only an env change.
1. Checkout — a route at /checkout driven by ?products=<id>: call the SDK's checkout create (JS: repalis.checkouts.create) and redirect the user to the returned checkout URL. Do not set a success URL and do not create a confirmation page — Repalis shows its own hosted confirmation after payment.
2. Webhooks — a POST route at /api/webhook/repalis that verifies the signature against REPALIS_WEBHOOK_SECRET before handling the event (JS: validateEvent from @repalis/sdk/webhooks; Python: repalis_sdk.webhooks.validate_event). Handle the order-paid and customer-state-changed events with clear TODO stubs — do not invent business logic.
Do not build a customer portal route, even though the skill includes a recipe for one. Repalis hosts the customer portal and already emails customers a link to it, so it needs no app code. (An in-app "Manage billing" link is optional and can be added later — leave it out.)
Then verify: build/typecheck the project (JS) or import the app module (Python) and fix any breakage before continuing.

## Phase 5 — Provision via API
Use the SDK client (or authenticated REST calls) with the token from .env, never printed. The organization access token already scopes to your organization — never pass organization_id in create calls (doing so returns 422).
1. List products. If none exist (or all existing ones are archived), create one test product named "Test Product" with a single one-time price of $10 (JS: repalis.products.create), and record its id.
2. If the user provided a public URL in Phase 1: first list webhook endpoints and skip creation if one already targets this app's /api/webhook/repalis URL. Otherwise create a webhook endpoint (url <public-url>/api/webhook/repalis, format raw, at least the order and customer state events). The response contains the generated signing secret — write it into .env as REPALIS_WEBHOOK_SECRET without printing it (e.g. pipe the response through jq). If local-only, skip and note it in the report.

## Phase 6 — Verify & hand off
1. Run the full typecheck/build once more. Do not block on a long-running dev server: if one isn't already running, give the user the command to start it instead of launching it yourself.
2. Give the user their first checkout link: http://localhost:<port>/checkout?products=<PRODUCT_ID>. ${testInstruction}
3. Write REPALIS_SETUP.md: files created/changed, env keys added (names only, never values), product and webhook endpoint ids, a verify-before-merging checklist, a note that Repalis's customer portal is already available to customers (Repalis hosts it and emails them the link — no app code needed), and ${goLiveNote}.
4. Offer exactly one follow-up: "Want me to wire the webhook handlers into your database and auth so paid orders actually grant access? I'll propose the mapping before changing anything." If accepted: inspect their schema and auth, propose how to map Repalis customers to app users (set external_customer_id to the app's user id at checkout, resolve it back in the webhook), get approval, then implement.
`
}
