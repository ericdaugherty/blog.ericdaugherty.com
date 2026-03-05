#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: ./newpost.sh <post-title>"
  echo "Example: ./newpost.sh my-cool-post"
  exit 1
fi

SLUG="$(echo "$1" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | tr -cd 'a-z0-9-')"
DATE="$(date +%Y-%m-%d)"
FILENAME="${DATE}-${SLUG}.md"

hugo new "posts/${FILENAME}"

# Fix title to remove the date prefix
FILEPATH="content/posts/${FILENAME}"
TITLE="$(echo "$SLUG" | tr '-' ' ' | sed 's/\b\(.\)/\u\1/g')"
sed -i "s/^title = .*/title = '${TITLE}'/" "$FILEPATH"
