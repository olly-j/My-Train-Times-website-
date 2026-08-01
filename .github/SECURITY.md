# TubeBoard Assets Security Policy

Use this repository's **Security → Report a vulnerability** flow for a private
report, or contact the repository owner through an already-established private
channel. Do not open a public Issue or PR with credentials, personal data,
private asset provenance, or exploitable detail.

This repository owns public brand/assets and the pinned service source. The
canonical response rules and central tracking contract live in
`olly-j/My-Train-Times/.github/SECURITY.md`. Security remediation uses a central
`TB-NNN` Issue; sensitive evidence stays private. Rotate exposed credentials
before repository cleanup, and treat a merge, service deployment, and App Store
release as separate states.

Dependency vulnerability alerts, secret scanning, push protection, and private
vulnerability reporting are enabled. Routine automated dependency-update and
security-fix PRs remain disabled pending compatibility and impact review.
