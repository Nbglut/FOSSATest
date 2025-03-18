#!/bin/bash

# Set the name of the remote (default is 'origin')
REMOTE="origin"

# Set the default branch name (usually 'main' or 'master')
DEFAULT_BRANCH="main"

# Fetch the latest remote branch information
git fetch --prune

# List all remote branches, excluding the default branch
branches=$(git branch -r | grep -v "\->" | grep -v "$REMOTE/$DEFAULT_BRANCH" | sed "s/$REMOTE\///")

# Loop through each branch and delete it from the remote
for branch in $branches; do
  echo "Deleting remote branch: $REMOTE/$branch"
  git push $REMOTE --delete "$branch"
done
