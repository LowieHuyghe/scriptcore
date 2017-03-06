#!/usr/bin/env bash

# Automatic error detection
set -e
# Go to current working directory
cd "$(dirname "$0")/../.."


# Arguments
git_remote_url="$1"
git_branch="$2"

# Build
./bin/gitbook/build.sh

# Go into generated folder
cd _book
# Initiate git
git init
# Checkout given branch
git checkout -b "$git_branch"
# Add every change
git add .
# Commit the change
git commit -am 'Update docs'
# Push it to the given repo and branch
git push "$git_remote_url" "$git_branch" --force
