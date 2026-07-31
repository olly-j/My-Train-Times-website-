#!/usr/bin/env bash

set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

required=(
  AGENTS.md
  CONTRIBUTING.md
  docs/README.md
  .github/ISSUE_TEMPLATE/config.yml
  .github/pull_request_template.md
  .github/workflows/assets-quality.yml
  Brand-Package-Liquid-Glass/README.md
  brand/brand-guidelines.md
  website/website-copy.md
  03-Website/AGENTS.md
)

for path in "${required[@]}"; do
  [[ -f "$path" ]] || {
    echo "Missing required workspace file: $path" >&2
    exit 1
  }
done

[[ "$(git config -f .gitmodules --get submodule.03-Website.url)" == "https://github.com/olly-j/tubeboard.co.uk.git" ]] || {
  echo "03-Website must point to the canonical service repository." >&2
  exit 1
}

[[ "$(git config -f .gitmodules --get submodule.03-Website.branch)" == "main" ]] || {
  echo "03-Website must track service main." >&2
  exit 1
}

git -C 03-Website merge-base --is-ancestor HEAD origin/main || {
  echo "The pinned service commit is not available from origin/main." >&2
  exit 1
}

if ! grep -Fq 'Status: Archived package snapshot' Brand-Package-Liquid-Glass/README.md; then
  echo "The dated brand package must remain classified as an archived snapshot." >&2
  exit 1
fi

if git ls-files | grep -Eq '(^|/)(\.env|live-activities\.json)$|\.p8$|\.pem$|\.key$|xcuserdata|\.DS_Store$'; then
  echo "Sensitive or personal workspace material is tracked." >&2
  exit 1
fi

echo "Assets workspace checks passed."
