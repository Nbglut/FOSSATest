#!/bin/bash

# Ensure FOSSA CLI is installed and available in your PATH
export FOSSA_API_KEY="5503bbc635a69c17e052b384a35c0f8c"

# Print the API Key for debugging (optional, be careful with sensitive data)
echo "FOSSA API Key: $FOSSA_API_KEY"

if ! command -v fossa &> /dev/null
then
    echo "FOSSA CLI could not be found. Please install it first."
    sleep 1  # Pause for 1 second
    exit 1
fi

# The Git repository path you want to scan
REPO_PATH="$1"

if [ -z "$REPO_PATH" ]; then
  echo "Please provide the local Git repository path."
  sleep 1  # Pause for 1 second
  exit 1
fi

# Check if the directory exists
if [ ! -d "$REPO_PATH" ]; then
  echo "Repository directory does not exist: $REPO_PATH"
  sleep 1  # Pause for 1 second
  exit 1
fi

# Navigate to the local repository
cd "$REPO_PATH" || { echo "Failed to navigate to the repository directory."; sleep 1; exit 1; }

# Fetch the latest changes from the remote repository
git fetch --all

# Get all remote branches
REMOTE_BRANCHES=$(git branch -r | grep -v '\->' | sed 's/origin\///')

# Create a file to store branches with issues
ISSUE_BRANCHES="branches_with_issues.txt"
echo "Branches with issues:" > "$ISSUE_BRANCHES"

# Loop through all remote branches
for BRANCH in $REMOTE_BRANCHES
do
    # Skip the default branch (e.g., 'main' or 'master')
    if [ "$BRANCH" == "main" ] || [ "$BRANCH" == "master" ]; then
        continue
    fi

    echo "Processing remote branch: $BRANCH"
    
    # Stash untracked files before checkout
    git stash --include-untracked || { echo "Failed to stash untracked files."; sleep 1; continue; }

    # Remove any existing lock file
    rm -f .git/index.lock
    
    # Checkout the remote branch locally
    git checkout -b "$BRANCH" "origin/$BRANCH" || { echo "Failed to checkout branch $BRANCH"; git stash pop; sleep 1; continue; }
    
    # Run FOSSA scan on the branch
    echo "Running FOSSA scan on remote branch: $BRANCH"
    
    # Ensure FOSSA is initialized for the branch (without --yes)
    if ! fossa init; then
        echo "FOSSA initialization failed for branch $BRANCH"
        git stash pop
        sleep 1  # Pause to read the message
        continue
    fi

    if ! fossa analyze; then
        echo "FOSSA analysis failed for branch $BRANCH"
        git stash pop
        sleep 1  # Pause to read the message
        continue
    fi
    
    # Check if FOSSA found any issues
    if fossa status --json | jq '.scanStatus' | grep -q 'FAILED'; then
        echo "Remote branch '$BRANCH' has issues!" >> "$ISSUE_BRANCHES"
    else
        echo "Remote branch '$BRANCH' passed the scan."
    fi

    # Restore stashed changes after processing the branch
    git stash pop
done

# Output the branches with issues
echo "Scan completed. See '$ISSUE_BRANCHES' for branches with issues."
cat "$ISSUE_BRANCHES"
