# sqlalchemy-challenge
Using primarily SQLAlchemy, Pandas, and Matplotlib to perform a climate analysis on Honolulu, Hawaii using data from a SQLite database. Then Flask, SQLAlchemy, and HTML are utilized to create an API to dynamically query the database. 

The Jupyter notebook has visualizations and summary statistics for precipitation and station analysis. Meanwhile, the Python file creates the API with set query options available, and dynamic queries involving dates. 

## API
After running the app.py file, paste the link generated from the terminal into your local server. The following homepage is what should be seen:
&emsp;
![image](https://github.com/user-attachments/assets/47fcbee8-18ec-4481-b926-1d77e34b6df0)

From this homepage, the desired JSON data can be queried by clicking on the buttons. There are also two dynamic routes available to generate temperature statistics based on inputed dates. There the user can enter a start date and an optional end date.

## Files
The files are expected to be in the following format for the Jupyter and Python files to run properly (all necessary folders/files are in bold):
- **Resources:** folder containing data files and database (the csv files are unnecessary)
    - hawaii_measurement.csv: data about precipitation and temperature throughout the years at different climate stations
    - hawaii_stations.csv: data about climate stations in Honolulu
    - **hawaii.sqlite:** database containing the two csv files in the Resources folder
- **SurfsUp:** folder containing files with code
    - **templates:** folder containing HTML for the homepage of the API
        - **home_weather.html**
    - **app.py:** Python file to return JSON data from the database based on queries
    - **climate.ipynb:** Jupyter notebook with visualizations and summary statistics
