#!/bin/bash
# Simple fix - just push after allowing on GitHub

echo "Step 1: Go to this link and click 'Allow':"
echo "https://github.com/mydaniel112-hub/golf-Claude/security/secret-scanning/unblock-secret/3985lWNR7FEnKs6lyq2oqLRlgvs"
echo ""
echo "Press Enter after you've allowed it on GitHub..."
read

echo "Step 2: Pushing to GitHub..."
cd "/Users/danielmacwilliams/gold claude"
git push

echo "Done! Railway will rebuild automatically."
