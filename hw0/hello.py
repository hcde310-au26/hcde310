"""HW0 setup check. Run it with:  python3 hw0/hello.py"""
import sys

version = sys.version_info
print("Hello, HCDE 310!")
print(f"You're running Python {version.major}.{version.minor}.{version.micro}")

if version >= (3, 12):
    print("Your Python is ready for this class.")
else:
    print("This class needs Python 3.12 or newer. See the HW0 Setup Guide on Canvas, or ask in #help on Slack.")
