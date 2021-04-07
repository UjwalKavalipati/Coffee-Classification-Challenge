# Coffee Classification and Clustering Challenge

The link for the app is https://coffee-prediction.herokuapp.com/.

The link for the dataset is https://github.com/jldbc/coffee-quality-database/tree/master/data.

I am using Windows 64 bit operating system with conda version of 4.9.2 and python version of 3.6.13 and jupter-notebook version of 6.3.0.


# Steps to run:
First, pull the repo into your local machine.
1. Open anaconda prompt in your system.
2. Create a virtual environment: 
``` bash
conda create -n coffeeprediction python=3.6
```
Here coffeeprediction is the virtual envionment name

3. Activate the virtual environment:
``` bash
conda activate coffeeprediction
```
4. Now navigate to the directory where you have all the files in this repo. 
5. Install the required libraries:
``` bash
pip install -r requirements.txt
```
6. Run the file app.py
``` bash
python app.py
```
7. Enter the values for various quality attributes of coffee and predict the coffee type.
8. Go to Jupyter Notebook to open the Coffee Classification and Clustering.ipynb file.
``` bash
jupter notebook
```
9. Navigate to the ipynb file and explore it. Details about loading the dataset,EDA,feature engineering, feature selection, classification,clustering model building and evaluation are explained in the ipynb file.
10. The Coffee Classification and Clustering.ipynb file only shows the best classification and clustering models. Details about all other models implemented are given in the CoffeeReport.
