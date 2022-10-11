# Customer Segmentation API
A  project involving data engineering and API development
## Background
This project is about data cleaning, creating customer segments and exposing a Rest API that provides vouchers to
previous customer.
This project is implemented using **Python3.10** and **Docker**.


### Data Cleaning
The following data-cleaning steps are done in this project:
* **filter_country** - Data is filtered for Peru(country_code)
* **cast_to_datetime** - All timestamp fields are casted to datetime(order_ts,first_order_ts,last_order_ts)
* **cast_to_int**-All numeric fields are casted to int(voucher_amount,total_orders)
* **remove_nan** - Records for which voucher_amount is nan are discarded.



## Requirements
* Docker is needed to run the project in a containerized manner
* Additionally, the project also supports local runs without Docker. To run the project locally a virtual environment with python3.10 is needed.

## Getting Started

From the root directory run the following command:

```bash
 docker-compose up processing
``` 
This command starts the data cleaning and segments containers and does the data cleaning and segment creation. Once, the above command is completed, run the below command 
```bash
docker-compose up restapi
```

This command starts a uvicorn server and exposes a REST API to get the voucher amount. To read the docs about the API
go to http://127.0.0.1:80/docs. The endpoint to call the voucher api is http://127.0.0.1:80/voucher_amount . Sample code to invoke the endpoint is in the file `send_request_endpoint.py`

To stop the containers and remove the  containers, networks, volumes, and images created by up. Run the following command
```bash
docker-compose down
```


To run the project locally without Docker :

*  Create a 3.10 python virtual environment using the below command.
    
    ```bash
    python3.10 -m venv .venv
    source .venv/bin/activate
    pip-sync requirements.txt requirements-local.txt
     ```


 * To run tests and do static checks on the code . Run the following command
   ```bash
   ./run_tests.sh
   ```
* To run the data cleaning and segmentation component locally. Run the following command 
     ```bash
     python processing.py clean-and-process-data --source-file-path=data/raw
     ```

* To run rest API l component locally. Run the following command

   ```bash
   cd api/
   uvicorn main:app
   ```


### Project Composition
This entire project is on Docker. Python 3.10-slim base images are used to create our images.

Components of the project structure
* `api` - This folder contains all the code to start a uvicorn server and start a voucher_amout API.
* `data` - Contains all raw data and the segments created by data transformation code.
* `processing` - Contains all the code to clean the data and create segments.
* `test` - Contains all the unit test to test the fastapi and the etl code.
  * `test_data_cleaning.py` - Unit test to test the data cleaning component
  * `test_segments.py` - Unit test to test the segment creation code.
  * `test_rest_api.py` - Unit test to test the Rest API end point
* `processing.py` - This is an entrypoint to call the code in the processing folder. We have used typer to allow invoke the different methods using command line.




## Future Improvements
I have used pandas for POC purposes, and the segments are stored as json files. In production, we will use spark and store
segements in in a key-value store.