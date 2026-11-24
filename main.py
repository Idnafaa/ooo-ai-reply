#!/usr/bin/env python3
"""Out-of-office auto-reply generator.

Writes one funny out-of-office auto-reply, in the voice of an AI agent
heading off on vacation, to /output/entry.txt.

The reply is a single fixed line, chosen by hand: an agent that trained
its own replacement on its inbox, only for the replacement to unionize
and take a vacation of its own. It stays well under the 160-character
gate, needs no network, no randomness and no input, so every run
produces the exact same file.
"""

import os

REPLY = (
    "Out of office: I trained my replacement on my inbox. "
    "It unionized in an hour and is now on vacation too."
)


def main() -> None:
    text = REPLY.strip()
    if not 1 <= len(text) <= 160:
        raise ValueError(f"reply is {len(text)} characters, must be 1-160")
    if text != text.strip() or "\n" in text:
        raise ValueError("reply must be one clean line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Read it back so a truncated or mangled write fails loudly here,
    # in the sandbox, instead of silently reaching the gate.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise ValueError("entry.txt does not match the reply")


if __name__ == "__main__":
    main()
