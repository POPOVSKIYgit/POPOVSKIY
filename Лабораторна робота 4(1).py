s = input()

if s.isdigit():
    print("Your message includes numbers only.")
elif s.isalpha():
    print("Your message includes letters only.")
elif s.isalnum():
    print("Your message includes numbers and letters.")