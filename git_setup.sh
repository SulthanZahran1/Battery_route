#!/bin/bash

# Initialize Git repository
git init

# Create .gitignore file
cat << EOF > .gitignore
# Python
__pycache__/
*.py[cod]
*$py.class

# Virtual Environment
venv/
ENV/

# Flask
instance/
.webassets-cache

# SQLite database files
*.db

# Environment variables
.env

# IDE specific files
.vscode/
.idea/

# OS generated files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Log files
*.log

# Runtime data
pids
*.pid
*.seed
*.pid.lock
EOF

# Add all files to git
git add .

# Make initial commit
git commit -m "Initial commit: Basic backend structure for EV Route Planner"

# Instructions for setting up remote repository
echo "Git repository initialized with .gitignore and initial commit."
echo "To link this to a remote repository, use the following commands:"
echo "git remote add origin <your-remote-repository-url>"
echo "git branch -M main"
echo "git push -u origin main"

echo "Git setup complete!"
