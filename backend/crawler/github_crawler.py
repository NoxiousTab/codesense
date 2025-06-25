import os
from git import Repo
from datetime import datetime

def clone_repo(repo_url: str, save_dir: str = "data/raw_code") -> str:
    repo_name = repo_url.rstrip("/").split("/")[-1]
    target_path = os.path.join(save_dir, repo_name)

    if os.path.exists(target_path):
        print(f"[!] Repo '{repo_name}' already exists. Skipping.")
        return target_path

    print(f"[+] Cloning {repo_url} to {target_path}")
    Repo.clone_from(repo_url, target_path)
    print(f"[✓] Done.")
    return target_path

def clone_multiple(repo_list: list[str], save_dir: str = "data/raw_code"):
    os.makedirs(save_dir, exist_ok=True)
    for url in repo_list:
        try:
            clone_repo(url, save_dir)
        except Exception as e:
            print(f"[x] Failed to clone {url}: {e}")
