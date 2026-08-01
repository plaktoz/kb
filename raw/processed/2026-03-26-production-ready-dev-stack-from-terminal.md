# Provision a production-ready dev stack from your terminal

source_url: https://stripe.dev/blog/production-ready-dev-stack-from-terminal

---

By Rami Banna — March 26, 2026

The article introduces **Stripe Projects**, a new Stripe CLI tool that automates provisioning of developer infrastructure — hosting, databases, auth, analytics, and AI components — directly from the terminal.

The core problem it addresses: setting up a modern app stack requires hopping between dashboards, following brittle docs, and manually copying credentials, creating what the author calls "key sprawl."

## How It Works

1. **Initialize** a project via CLI, which generates configuration files, a blank `.env`, and agent-compatible skills
2. **Add services** from partner providers (Vercel, Neon, Supabase, Railway, Clerk, PostHog, Chroma, etc.) with simple commands like `stripe projects add vercel/project`
3. **Upgrade plans** when needed — Stripe handles payment via "Shared Payment Tokens" so credentials aren't re-entered across dashboards
4. **Sync credentials** with `stripe projects env --pull`, centralizing secrets instead of scattering them

## Key Differentiator

Resources live in **your own provider accounts**, and the tool is designed to be agent-friendly — deterministic and auditable enough for AI coding agents to operate independently.

Currently in developer preview, with payment upgrades limited to US, EU, UK, and Canada.
