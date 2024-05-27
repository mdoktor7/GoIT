# Exchange Rate Utility

## Introduction

This project is a console utility that fetches and displays the EUR and USD exchange rates of PrivatBank over the past few days. The utility can display the exchange rate for up to the last 10 days. Additionally, the project includes a chat server that allows users to enter commands to fetch exchange rates and interact with each other.

## Features

- Fetch exchange rates for up to 10 days.
- Display exchange rates for supported currencies (USD, EUR).
- Log executed commands to a file.
- Chat server to enter commands and view exchange rates.
- Client script to send commands to the chat server.

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:

   ```git clone https://github.com/mdoktor7/GoITRepos/tree/GoIT/Python/PythonWeb/module_05/exchange-rate-utility.git```
   ```cd exchange-rate-utility```

2. Create a virtual environment and install dependencies:
    ```python -m venv venv```
    ```source venv/bin/activate  # On Windows, use `venv\Scripts\activate```
    ```pip install -r requirements.txt```

### Usage

### Fetch Exchange Rates

Run the console utility with the desired number of days (max 10):
    ```py .\main.py <number_of_days>```


### Chat Server  
1. Start the chat server:
    ```py chat_server.py```

2. Open chat/index.html in your browser to connect to the chat server.

3. Use the command ```exchange <number_of_days>``` in the chat to fetch exchange rates


### WebSocket Client   
1. Ensure the chat server is running.
2. Run the client script:
    ```py client.py```
3. The client will send an exchange command and display the response.    
    

### License

This project is licensed under the MIT License - see the LICENSE file for details.

###  Contact

For any questions or suggestions, please open an issue or contact mdoktor696@gmail.com.
