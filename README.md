# Windows Process API Demo

A Python project exploring Windows process and system API interaction using `ctypes`.

The project demonstrates how Python can interact with native Windows APIs to obtain process handles and inspect exported functions from Windows system libraries.

## Features

* Windows API interaction
* Process creation
* Process ID retrieval
* Process handle retrieval
* `kernel32.dll` interaction
* `GetModuleHandleA`
* `GetProcAddress`
* Python `ctypes`

## Requirements

* Windows
* Python 3

No external Python packages are required.

## Run

```bash
python process_api_demo.py
```

The script starts a temporary Notepad process, retrieves information about the process, accesses `kernel32.dll`, locates the `LoadLibraryA` function, and then closes the process.

## Project Structure

```text
windows-process-api-demo/
├── process_api_demo.py
├── .gitignore
└── README.md
```

## Notes

This project is an educational demonstration of Windows API interaction using Python `ctypes`.

The original concept involved remote DLL injection. This public version focuses on process and Windows API inspection and does not inject DLLs, write memory to another process, or create remote threads.
