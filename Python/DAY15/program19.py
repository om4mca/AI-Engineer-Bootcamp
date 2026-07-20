#--------------------------------------------
# AI Engineer Bootcamp
# Day 15
# Program: Project cleanup
# Author: Om Roy
# Date: 20-07-2026
#--------------------------------------------

# Remove all __pycache__ folders recursively
#Get-ChildItem -Path . -Include __pycache__ -Recurse -Force | Remove-Item -Recurse -Force

# Remove pytest and coverage cache
#Remove-Item -Path .pytest_cache, .coverage, htmlcov -Recurse -Force -ErrorAction SilentlyContinue