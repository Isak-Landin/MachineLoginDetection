## Current Version
Version 1.0.0

## Development Branch
The `dev` branch is used for ongoing development. It contains the latest changes and features that are still under testing and may not be as stable as the `main` branch. This branch is suitable for development, testing, and contributions.


## Project Overview
MachineLoginDetection is a Bash and Python-based tool designed for monitoring login attempts on an Ubuntu server. It analyzes the `/var/log/auth.log` file, tracking IP addresses, timestamps, and the success or failure of login attempts, and stores this data in a PostgreSQL database.

## Features
- **Log Parsing**: Parses `/var/log/auth.log` to extract login attempt data.
- **Data Storage**: Utilizes PostgreSQL for robust data management.
- **Cron Automation**: Automated daily log analysis through cron jobs.
- **Multi-Language Support**: Scripted in Bash and Python for enhanced functionality and ease of integration.

## Getting Started

### Prerequisites
- Ubuntu Server (Recommended: Ubuntu 22.04 or higher)
- PostgreSQL 9.5 or higher
- Python 3.6 or higher
- Basic knowledge of Bash scripting, Python, and PostgreSQL

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Isak-Landin/MachineLoginDetection.git
