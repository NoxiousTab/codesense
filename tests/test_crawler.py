import os
import shutil
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.crawler.github_crawler import clone_repo

def test_clone_repo():
    test_url = "https://github.com/NoxiousTab/privacy_vault"
    repo_path = "data/raw_code/privacy_vault"

    # Cleanup before test
    if os.path.exists(repo_path):
        shutil.rmtree(repo_path)

    clone_repo(test_url)
    assert os.path.exists(repo_path)
