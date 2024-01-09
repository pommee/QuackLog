```
 .d88888b.           ⠀⠀⠀⠀⠀⠀⣀⣤⣶⣶⣤⡀            888      888                      ⠀
d88P" "Y88b         ⠀⠀⠀⠀ ⢀⣾⠛⠁⢰⣧⡈⢻⣦           888      888                   ⠀⠀⠀⠀
888     888          ⠀⠀⠀⠀⢸⣇⣼⡀⠻⠟⠁⠀⢻⡆          888      888                 ⠀⠀⠀⠀⠀
888     888 888  888 ⠀⠀⠀⢀⡞⣹⠙⣧⡀⠀⠀⡀⢸⡇  .d8888b 888  888 888       .d88b.   .d88b.
888     888 888  888 ⠀⣀⡴⠋⠀⣀⣴⣿⡷⠴⠞⠁⢸⡇ d88P"    888 .88P 888      d88""88b d88P"88b
888 Y8b 888 888  888 ⢾⣁⣀⡤⠾⠛⠁⣸⠀⠀⠀⠀⢸⡇ 888      888888K  888      888  888 888  888
Y88b.Y8b88P Y88b 888   ⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⣾⠃ Y88b.    888 "88b 888      Y88..88P Y88b 888
 "Y888888"   "Y88888 ⠀⠀⠀⠀⠀⣠⣿⠁⠀⠀⠀⢀⣿   "Y8888P 888  888 88888888  "Y88P"   "Y88888
       Y8b                                                                     888
                                                                          Y8b d88P
                                                                           "Y88P"⠀
```

_Storing medium for logs_ 

Having used the popular tools [elasticsearch](https://www.elastic.co/elasticsearch) & [kibana](https://www.elastic.co/kibana) before, it sparked my interest in building something simular that I can call my own.  

## The aim
Creating a system that can store logs and easily be implemented. Running in an container and be easy to deploy.


## Installation

### Locally
The `Makefile` handles the setup for us.  
Just run `make build-run` - this will build and run the container.

## API

| Method | Endpoint | Description                                          |
| ------ | -------- | ---------------------------------------------------- |
| POST   | `/`      | Accepts JSON data to create a log item.              |

**POST `/`**:
- **Description:** This route expects a JSON body containing log data to create a log item. The JSON data should include the following fields:
    - `"service"`: The service related to the log.
    - `"time_sent"`: The timestamp when the log was sent in ISO 8601 format (e.g., "2024-01-20T20:49:21").
    - `"size"`: The size information associated with the log.
    - `"message"`: Description or message related to the log entry (e.g., "User has logged in.").
- **Example Body (JSON):**
    ```json
    {
        "service": "authentication",
        "time_sent": "2024-01-20T20:49:21",
        "size": "201K",
        "message": "User has logged in."
    }
    ```

| Method | Endpoint | Description                                          |
| ------ | -------- | ---------------------------------------------------- |
| GET    | `/`      | Retrieves logs within a specified date range.         |

**GET `/`**:
- **Description:** This route retrieves logs within a specified date range. To use this endpoint, provide the following query parameters:
    - `start_year`: Start year of the date range (e.g., 2023).
    - `start_month`: Start month of the date range (e.g., 11 for November).
    - `start_day`: Start day of the date range (e.g., 20).
    - `end_year`: End year of the date range (e.g., 2024).
    - `end_month`: End month of the date range (e.g., 02 for February).
    - `end_day`: End day of the date range (e.g., 20).
- **Example (cURL):**
    ```bash
    curl --location 'http://127.0.0.1:8000?start_year=2023&start_month=11&start_day=20&end_year=2024&end_month=02&end_day=20'
    ```
- **Usage:** Send a GET request to `/` endpoint with the specified query parameters to retrieve logs falling within the provided date range.
