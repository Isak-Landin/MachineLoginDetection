# Machine Login Detection

## Current Version
Version 1.0.0

## Project Overview
MachineLoginDetection is a Bash-based tool designed to monitor and analyze login attempts on an Ubuntu server by parsing the `/var/log/auth.log` file. It tracks IP addresses, timestamps, and the success or failure of each attempt, storing this data in a PostgreSQL 9.5 database.

## Branch Structure

### `main` Branch
- **Purpose**: Represents the latest **stable** and **production-ready** version of the software.
- **Usage**: Only updated from the `dev` branch after thorough testing and validation.

### `dev` Branch
- **Purpose**: Used for **continuous development**, updates, and testing.
- **Important**: This and only this branch should be used for ongoing work and updates.


## Features
- **Log Parsing**: Efficiently parses `/var/log/auth.log` for login attempt data.
- **Data Storage**: Stores login attempt details in PostgreSQL 9.5.
- **Cron Automation**: Utilizes cron jobs for daily log analysis.
- **Bash Scripting**: Entirely scripted in Bash for easy integration into Unix/Linux systems.

## Getting Started

### Prerequisites
- Ubuntu Server (Recommended: Ubuntu 22.04)
- PostgreSQL 9.5
- Basic knowledge of Bash scripting and PostgreSQL

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Isak-Landin/MachineLoginDetection.git
   ```
