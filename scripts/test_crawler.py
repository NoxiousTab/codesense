import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.crawler.github_crawler import clone_multiple

if __name__ == "__main__":
    repos = [
        "https://github.com/NoxiousTab/privacy_vault",
        "https://github.com/NoxiousTab/practice_judge",
        "https://github.com/TheAlgorithms/Python"
    ]
    clone_multiple(repos)
