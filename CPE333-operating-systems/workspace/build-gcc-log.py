import os


files = ["q1.1.c", "q1.2.c"]
for src in files:
    (f"\n=== {src} ===")
    print(f"gcc -o {src[0:-2]} {src}")
    print(f"./{src[0:-2]}")
