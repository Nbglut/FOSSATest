#!/bin/bash

# Ensure FOSSA CLI is installed and available in your PATH
export FOSSA_API_KEY="5503bbc635a69c17e052b384a35c0f8c"

# Print the API Key for debugging (optional, be careful with sensitive data)
echo "FOSSA API Key: $FOSSA_API_KEY"

if ! command -v fossa &> /dev/null
then
    echo "FOSSA CLI could not be found. Please install it first."
    sleep 3  # Pause for 3 seconds to let the user read the message
    exit 1
fi

# The GitHub repository URL
REPO_URL="$1"

# Check if repository URL is provided
if [ -z "$REPO_URL" ]; then
  echo "Please provide the GitHub repository URL."
  sleep 3  # Pause for 3 seconds to let the user read the message
  exit 1
fi

# Directory to clone the repo
REPO_DIR=$(basename "$REPO_URL" .git)

# Check if the repository is already cloned
if [ ! -d "$REPO_DIR" ]; then
    echo "Cloning the repository from $REPO_URL..."
    git clone "$REPO_URL" || { echo "Failed to clone the repository."; sleep 3; exit 1; }
else
    echo "Repository already cloned. Pulling the latest changes..."
    cd "$REPO_DIR" || exit 1
    git pull || { 
        echo "Failed to pull the latest changes. Checking for conflicts...";
        git status; 
        sleep 3;
        continue;
    }
fi

# Navigate to the cloned repository directory
cd "$REPO_DIR" || { echo "Failed to navigate to the repository directory."; sleep 3; exit 1; }

# Fetch the latest changes from the remote repository
git fetch --all || { echo "Failed to fetch all branches."; sleep 3; exit 1; }

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
    
    # Check if there are untracked files and stash them only if necessary
    git status --porcelain | grep "??" > /dev/null
    if [ $? -eq 0 ]; then
        echo "Stashing untracked files for branch $BRANCH"
        git stash --include-untracked || { echo "Failed to stash untracked files for branch $BRANCH"; sleep 3; continue; }
    fi
    
    # Remove any existing lock file
    rm -f .git/index.lock
    
    # Checkout the remote branch locally
    git checkout -b "$BRANCH" "origin/$BRANCH" || { echo "Failed to checkout branch $BRANCH"; git stash pop; sleep 3; continue; }
    
    # Check for merge conflicts after checkout
    git status | grep "Unmerged paths"
    if [ $? -eq 0 ]; then
        echo "Merge conflicts detected in branch $BRANCH. Skipping this branch."
        git stash pop
        continue
    fi
    
    # Run FOSSA scan on the branch
    echo "Running FOSSA scan on remote branch: $BRANCH"
    
    # Ensure FOSSA is initialized for the branch (without --yes)
    if ! fossa init; then
        echo "FOSSA initialization failed for branch $BRANCH"
        git stash pop
        sleep 3  # Pause to read the message
        continue
    fi

    if ! fossa analyze; then
        echo "FOSSA analysis failed for branch $BRANCH"
        git stash pop
        sleep 3  # Pause to read the message
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

# Pause at the end of the script to allow reading the final output
read -p "Press [Enter] to exit..."
