# Twitch Viewer Bot

## Overview

This script is designed to automatically open multiple proxy servers and direct them to a specific Twitch channel for viewing. It supports setting the stream quality to 160p and can handle proxy URLs dynamically.

## Features

- **Proxy Server Rotation**: Selects a random proxy server for each tab.
- **Stream Quality Setting**: Optionally sets the stream quality to 160p.
- **Automatic ChromeDriver Management**: Uses `chromedriver-autoinstaller` to automatically install the correct ChromeDriver version.
- **Error Handling**: Moves on to the next URL if an error occurs.

## Installation

1. **Clone the Repository**: 

   `git clone https://github.com/Germanized/Germanized.git`

2. **Navigate to the Project Directory**: 

   `cd Germanized`

3. **Install Required Packages**: 

   Use pip to install the required Python packages:

   `pip install requests selenium colorama pystyle chromedriver-autoinstaller`

## Usage

1. **Run the Script**:

   Execute the script using Python:

   `python main.py`

2. **Provide Inputs**:

   - **Twitch Username**: Enter the channel name you want to send viewers to.
   - **Set 160p Quality**: Specify if you want to set the stream quality to 160p (`yes` or `no`).
   - **Number of Proxies**: Enter how many proxy sites you want to open.

## Configuration

- **Settings**: 
  The script saves the Twitch username and stream quality setting in a file named `settings.txt`. You can manually edit this file or provide new inputs when running the script.

- **Proxies**: 
  The script uses a predefined list of proxy servers. You can add or modify this list as needed.

## Troubleshooting

- **SSL Errors**:
  If you encounter SSL errors, the script will automatically move on to the next proxy URL.

- **Browser Issues**:
  Ensure that you have Google Chrome installed in the default directory. The script uses `chromedriver-autoinstaller` to manage ChromeDriver versions.

## Contribution

Feel free to contribute by submitting issues or pull requests on the [GitHub repository](https://github.com/Germanized/Germanized).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This script is intended for educational purposes only. Use responsibly and comply with all relevant laws and terms of service.
