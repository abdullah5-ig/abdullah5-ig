#!/usr/bin/env bash
#
# Pushes your GitHub profile README (the special repo named after you).
#
# BEFORE RUNNING
#   1. Make a token with "repo" scope:
#      https://github.com/settings/tokens/new?scopes=repo&description=profile-readme
#   2. Open Notepad, paste ONLY the token, and save it as token.txt in this
#      same folder. Set "Save as type" to "All Files" so it is not saved as
#      token.txt.txt
#   3. Run:  bash push_profile.sh
#
# Safe to run again — it reuses the repo if it already exists.

set -euo pipefail

GH_USER="abdullah5-ig"
GH_EMAIL="abdullahnaqvi131@gmail.com"
GH_NAME="Abdullah Naqvi"
REPO="abdullah5-ig"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Read the token from token.txt. This avoids pasting it into the terminal,
# which Git Bash on Windows mangles with invisible control characters.
if [[ -z "${GITHUB_TOKEN:-}" && -f "$SCRIPT_DIR/token.txt" ]]; then
  GITHUB_TOKEN="$(tr -cd 'A-Za-z0-9_' < "$SCRIPT_DIR/token.txt")"
  [[ -n "$GITHUB_TOKEN" ]] && echo "Read token from token.txt (${#GITHUB_TOKEN} characters)."
fi

if [[ -z "${GITHUB_TOKEN:-}" ]]; then
  cat <<'MSG'
ERROR: no GitHub token found.

  1. Make a token (tick "repo", 7 days expiry):
     https://github.com/settings/tokens/new?scopes=repo&description=profile-readme

  2. Open Notepad. Paste ONLY the token. Save as token.txt in this folder.
     Set "Save as type" to "All Files".

  3. Run this again:  bash push_profile.sh

MSG
  exit 1
fi

if [[ ! "$GITHUB_TOKEN" =~ ^(ghp|github_pat)_ ]]; then
  echo "ERROR: that does not look like a GitHub token."
  echo "It should start with 'ghp_' or 'github_pat_'."
  echo "Check token.txt holds only the token and nothing else."
  exit 1
fi

# Make sure we are in the right folder before doing anything.
if [[ ! -f "$SCRIPT_DIR/README.md" || ! -d "$SCRIPT_DIR/assets" ]]; then
  echo "ERROR: this does not look like the profile folder."
  echo "Expected README.md and an assets/ folder next to this script."
  exit 1
fi

API="https://api.github.com"
AUTH=(-H "Authorization: Bearer ${GITHUB_TOKEN}"
      -H "Accept: application/vnd.github+json")

echo "Verifying token..."
who=$(curl -sf "${AUTH[@]}" "$API/user" \
      | grep -o '"login"[[:space:]]*:[[:space:]]*"[^"]*"' | head -1 \
      | sed 's/.*"\([^"]*\)"$/\1/') || {
  echo "ERROR: GitHub rejected the token."
  echo "It may be expired, deleted, or missing the 'repo' scope. Make a new one."
  exit 1
}
echo "  signed in as: $who"
if [[ "$who" != "$GH_USER" ]]; then GH_USER="$who"; REPO="$who"; fi

if curl -sf -o /dev/null "${AUTH[@]}" "$API/repos/$GH_USER/$REPO"; then
  echo "  repo '$REPO' already exists — reusing it"
else
  echo "  creating repo '$REPO'"
  curl -sf -o /dev/null -X POST "${AUTH[@]}" "$API/user/repos" \
    -d "$(printf '{"name":"%s","description":"Profile README","private":false,"has_issues":false,"has_wiki":false}' "$REPO")" \
    || { echo "ERROR: could not create the repo."; exit 1; }
fi

cd "$SCRIPT_DIR"

# Never commit the token file.
grep -qx "token.txt" .gitignore 2>/dev/null || echo "token.txt" >> .gitignore

git init -q 2>/dev/null || true
git config user.email "$GH_EMAIL"
git config user.name "$GH_NAME"
git add -A
if git diff --cached --quiet 2>/dev/null && git rev-parse HEAD >/dev/null 2>&1; then
  echo "  nothing new to commit"
else
  git commit -q -m "Redesign profile README"
fi
git branch -M main

git remote remove origin 2>/dev/null || true
git remote add origin "https://${GITHUB_TOKEN}@github.com/$GH_USER/$REPO.git"

echo "  pushing..."
git push -q -u origin main --force

# Strip the token out of .git/config so it is not left on disk.
git remote set-url origin "https://github.com/$GH_USER/$REPO.git"

cat <<EOF

────────────────────────────────────────────────────────────
Pushed to https://github.com/$GH_USER/$REPO

Open https://github.com/$GH_USER to see it.

Then clean up:
  - Delete token.txt from this folder
  - Delete the token at github.com/settings/tokens
────────────────────────────────────────────────────────────
EOF
