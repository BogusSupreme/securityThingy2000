# securityThingy2000

## Overview
The point of this project is to show basic cybersecurity concepts like:

- Password strength evaluation via detection of weak password patterns
- Password hashing
- File permission misconfiguration scanning

## How to Run

1. Open a terminal in the project directory.
2. Run:

   python securityThingy.py

3. Answer the password prompt to see how strong it is, and what the hashed version would look like.
4. Give a file path for a file you'd like to scan for permission misconfigurations.

## Features

- Checks for password length
- Checks for uppercase letters
- Checks for special characters
- Checks for repeated characters
- Generates a SHA-256 hash of a given password
- Scans a given files (and some example ones that may or may not be available) for world-writable permissions

## WARNING

This tool was developed for educational purposes to demonstrate basic ethical hacking and security analysis techniques. It does not exploit vulnerabilities, and shouldn't be used for real-life purposes.

## Ethical Considerations

Tool could give users a false sense of security regarding their passwords, as not every hacking method requires knowing the user's password. It could also be modified so that when you give it a file path
to check for permissions, it steals the files and sends them somewhere else. But this could be avoided by actually looking at the code.

