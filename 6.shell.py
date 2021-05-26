import os
import subprocess

if __name__ == '__main__':
    p1 = subprocess.run(['ls', '-la'], capture_output=True, text=True)
    print(p1.stdout)

