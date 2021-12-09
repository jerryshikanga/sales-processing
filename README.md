# Sales Processing

### Pre-Requisites & Local SetUp
Clone the repository locally and navigate to the directory

There are two files attached
1. `solution.ipynb`
2. `solution.py`

The ipynb allows you to run the solution in an interactive environment.
To use it :
* Download the version for your OS from AnaConda from [Anaconda Downloads Page](https://www.anaconda.com/products/individual#Downloads)
* Install the downloaded file
* Open Jupyter Notebook
* Using the file explorer navigate to the location you cloned the project
* Open the .ipynb file
* On the kernel menu clear all outputs
* Run the cells individually while observing the outputs

The .py file can be run using the command line.
To run it :
* Ensure python3 is installed in your computer. If not install from [Python Official Website](https://www.python.org/downloads/)
* Install the virtual environment package `python3 -m pip install --user virtualenv`  
* Create a virtual environment `python3 -m venv env`
* Activate the virtual environment you created `source env/bin/activate`
* Install required packages `pip install -r requirements.txt`
* Run `python solution.py`

### Scaling
* Use of asynchronous processing to fasten the processing in the case of large files/ large number of files
* Use celery workers to batch process the data for the case of many workers

### Assumptions
* No new files will be added during the processing. 
* The files don't change during processing.

To handle such cases then we would need to have a variable to store which files are being processed currently, more of emulating the process of database locks.
