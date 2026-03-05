#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: ./newpost.sh <post-title>"
  echo "Example: ./newpost.sh my-cool-post"
  exit 1
fi

SLUG="$(echo "$1" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | tr -cd 'a-z0-9-')"
FILENAME="$(date +%Y-%m-%d)-${SLUG}.md"

hugo new "posts/${FILENAME}"