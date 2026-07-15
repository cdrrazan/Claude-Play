# Security Policy

Keel is mostly Markdown — a set of docs, templates, and rules. But a few parts execute or get copied
into other people's repos, so security reports are welcome.

## Scope

The parts worth reporting:

- **CI scripts and workflows** under `.github/` (a link checker + the Pages/checks workflows).
- **The optional enforcement-hook example** documented in `.claude/hooks/` — anyone who wires it up runs it.
- **Copy-paste snippets** in `templates/` and the role prompts in `roles/`.
- **Supply-chain** concerns in the GitHub Actions this repo pins.

"The guide says something wrong" is **not** a security issue — open a
[correction](.github/ISSUE_TEMPLATE/correction.md) instead.

## Reporting a vulnerability

**Please report privately — do not open a public issue for a security problem.**

- **Preferred:** GitHub's private vulnerability reporting — the **Security → Report a vulnerability**
  button on this repository. (Maintainers: enable it under *Settings → Security → Private vulnerability
  reporting* if it isn't already on.)
- **Or email the maintainer:** cdrrazan@gmail.com

Please include what you found, where (file + line), and how to reproduce it. You can expect an
acknowledgement within a few days. Once a fix ships, we'll credit you in the release notes unless you'd
prefer to stay anonymous.

## Supported versions

This is a living-document repository; only the latest `main` is supported. Fixes land on `main` and are
recorded in [CHANGELOG.md](CHANGELOG.md).
