import re
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    numbers = re.findall(r"\d+", line)
    if numbers:
        print(", ".join(numbers))