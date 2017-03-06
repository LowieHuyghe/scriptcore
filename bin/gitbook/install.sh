#!/usr/bin/env bash

# Automatic error detection
set -e
# Go to current working directory
cd "$(dirname "$0")/../.."


# Install when necessary
if ! command -v gitbook > /dev/null
then
    npm install -g gitbook-cli
fi
