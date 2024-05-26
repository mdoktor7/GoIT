# Exchange Rate Utility

## Introduction

The Exchange Rate Utility is a Python-based console application that fetches and displays the EUR and USD exchange rates from PrivatBank over the past few days. The project also includes a WebSocket chat server where users can enter commands to retrieve exchange rates in real-time.

## Features

- Fetch exchange rates for the last 10 days.
- Support for additional currencies.
- Asynchronous HTTP requests for efficient data fetching.
- WebSocket chat server for real-time exchange rate queries.
- Logging of exchange commands using `aiofile` and `aiopath`.

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:

   ```git clone https://github.com/mdoktor7/GoITRepos/tree/GoIT/Python/PythonWeb/module_05/exchange-rate-utility.git```
   ```cd exchange-rate-utility```

2. Install the required packages:

    ```pip install -r requirements.txt```

### Usage

1. Running the Console Utility

    To run the console utility and fetch exchange rates for the past few days, use the following command:
     ```py main.py 2```

    Here, '2' is the number of days for which you want to fetch the exchange rates.

2. Running the WebSocket Chat Server
    To start the WebSocket chat server, use the following command:
    ```py chat_server.py```

### Using the WebSocket Client   
   To start thePython WebSocket client script, use the following command:
        ```py client.py```
    
    Here’s an example command to retrieve exchange rates for the last 3 days:
    ```json    
        {"command": "exchange", "days": 3}

### Contribution Guidelines

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Commit your changes (git commit -m 'Add some feature').
4. Push to the branch (git push origin feature-branch).
5. Open a pull request.

### License

This project is licensed under the MIT License - see the LICENSE file for details.

###  Contact

For any questions or suggestions, please open an issue or contact mdoktor696@gmail.com.
