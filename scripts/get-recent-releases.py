#!/usr/bin/env python3
import urllib.request
import json
import argparse


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("num", nargs="?", type=int, default=3)
    args = ap.parse_args()

    endpoint = "https://pypi.org/pypi/PyQt6/json"
    with urllib.request.urlopen(endpoint) as response:
        data = json.load(response)
        all_releases = list(data["releases"].keys())

    for i, ver in enumerate(all_releases[0 - args.num :]):
        print(f"rel{args.num - i - 1}={ver}")


if __name__ == "__main__":
    main()
