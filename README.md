# C-Chat
## Table of Contents
- Project Abstract
- High Level Requirement
- Conceptual Design
- Proof of Concept
- Background
- Required Resources
## Project Abstraction
C-Chat (Classified Chat) is a real-time chatting software that allows users to connect and interact with each other securely and efficiently using the command line interface. This project utilizes Python to allow for this connection between users. This app allows users to create a secret key which encrypts their chat. This key can be shared as a text file through USB or any secure transmission.

## High Level Requirement
From a user perspective, C-Chat provides the following functionality:
Real-Time Chat: Users can send and receive messages instantly via a command-line interface.
End-to-End Encryption: Messages are encrypted using a user-generated secret key to ensure confidentiality.
Key Management: Users can create and share a secret key (as a text file) for encryption/decryption, enabling secure communication.
Cross-Platform Compatibility: The application runs on major operating systems (Windows, macOS, Linux).
User Authentication: Basic user identification to ensure only authorized users join the chat.
Simple Interface: A minimalist, text-based interface for ease of use and low resource consumption.
Secure Key Sharing: Users can share encryption keys securely (e.g., via USB or other offline methods).
Error Handling: The system provides clear feedback for connection issues, invalid keys, or other errors.

## Proof of Concept

## Conceptual Design
We use the latest Python 3 for its simplicity, cross-platform support, and robust libraries for networking (e.g., socket) and encryption (e.g., cryptography or PyCryptodome).
This can be used on Windows, macOS and Linux to maximize accessibility.
The User Interface used is the Command-line interface (CLI) for simplicity and minimal resource usage. The CLI displays chat messages, user prompts, and system notifications.
Secret keys are stored as text files, allowing users to share them securely offline (e.g., via USB).

## Required Resources
Background Information: Understanding of socket programming in Python for network communication. Knowledge of symmetric encryption (e.g., AES) and key management. Familiarity with secure key exchange protocols and best practices for encryption. Basic understanding of command-line interface design and user experience.

Hardware Resources: Standard development computers with at least 4GB RAM and a modern CPU to run Python and test network communication.

Software Resources: Latest Python 3 (freely available). Python libraries: socket, cryptography or PyCryptodome, threading (all available via pip). A text editor or IDE (e.g., VS Code, PyCharm) for development. Git for version control (optional but recommended). Operating systems: Windows, macOS, or Linux.

## Background & References
C-Chat is designed for users who need a lightweight, secure, and private chat application without the overhead of graphical interfaces. Unlike mainstream chat applications (e.g., WhatsApp, Signal), C-Chat focuses on a terminal-based experience, making it ideal for developers, system administrators, or users in resource-constrained environments. The application emphasizes user-controlled encryption, where users generate and manage their own keys, avoiding reliance on third-party key servers.
A similar product is OpenChat which is a real-time chat application Java based. The difference is that it lacks encryption.
