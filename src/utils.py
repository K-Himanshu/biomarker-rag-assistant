# src/utils.py
import os

def ensure_dir(path):
    """Create directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def print_section(title):
    """Pretty print section titles in CLI."""
    print("\n" + "="*50)
    print(title)
    print("="*50 + "\n")

def pretty_print(docs):
    """Print retrieved documents nicely."""
    print_section("Retrieved Documents")
    for i, doc in enumerate(docs, 1):
        print(f"[{i}] {doc.page_content[:300]}...")  # show first 300 chars
        print("-"*50)