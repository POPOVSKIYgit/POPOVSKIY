import sys
import re

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    # Виділяємо лише слова (послідовності латинських літер)
    words = re.findall(r'[a-zA-Z]+', line)

    if words:
        # Знаходимо найдовше слово (при рівній довжині max обирає перше за замовчуванням)
        longest_word = max(words, key=len)
        print(longest_word)