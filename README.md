# Virtual Machine and Docker Manager

This project is a Virtual Machine (VM) and Docker Manager developed for CSCI 363. It provides a user-friendly graphical user interface (GUI) to manage virtualization and containerization tasks, simplifying complex command-line operations into an intuitive, menu-driven application.

## Project Overview

The goal of this project was to create a single, cohesive application that allows users to interact with both virtual machines and Docker containers. The system abstracts the underlying commands for QEMU (for VMs) and Docker (for containers), enabling users to perform a variety of operations without needing to use the terminal directly. Its modular design allows for easy expansion, making it a valuable tool for understanding and managing virtualization technologies.

## Key Features

*   **Virtual Machine Management:**
    *   Create new Virtual Machines with user-defined specifications.
*   **Docker Container Management:**
    *   Create Dockerfiles from user input.
    *   Build Docker images from Dockerfiles.
    *   List all available Docker images.
    *   Run new containers from existing images.
    *   Stop active containers.
    *   Search for Docker images locally and on DockerHub.

## Technologies Used

*   **Virtualization:** QEMU
*   **Containerization:** Docker
*   **Programming Language:** Python
*   **GUI Framework:** Tkinter
*   **System Interaction:** Python `os` module for executing shell commands.

## Challenges and Solutions

This project involved several technical challenges related to user input and system interaction. The following solutions were implemented to ensure robustness and a smooth user experience.

| Challenge | Solution Implemented |
| :--- | :--- |
| **Memory & Disk Validation** | Implemented stricter input validation to ensure all memory and disk values are numerical and fall within reasonable ranges, preventing system errors. |
| **Dockerfile Path Validation** | Added pre-emptive checks to verify the existence and validity of a directory path before attempting to save a Dockerfile, guiding the user to provide a correct path. |
| **Docker Image Building Errors** | Improved error handling during the image build process to provide clear, informative messages if a Dockerfile is missing or an image name is invalid. |
| **Robust User Input Validation** | Deployed comprehensive validation logic for all user inputs, such as container IDs and image names, significantly reducing the likelihood of runtime errors. |

## Testing Methodologies

The reliability of the application was ensured through a two-pronged testing approach:

*   **Unit Testing:** Each function was tested in isolation to verify its correctness. Mock data was used to simulate various user inputs and edge cases, ensuring each component performed as expected.
*   **Integration Testing:** Features were tested in combination to guarantee seamless interaction and data flow between different parts of the application. These tests covered menu navigation, data passing between functions, and end-to-end workflows.

## Conclusion

The Virtual Machine and Docker Manager successfully meets its objective of providing a centralized and user-friendly tool for managing virtualization and containerization tasks. By overcoming development challenges and implementing robust solutions, the project serves as a practical application for better understanding and utilizing these essential technologies.
