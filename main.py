"""Monday, Reviewed in One Line — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The line: a one-line review of my Monday.
TEXT = "One star. Monday arrived late, blamed the traffic, and left my motivation at the bus stop with no umbrella."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
