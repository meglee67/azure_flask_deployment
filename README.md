# flask_2_intro
Here is the link to my azure website: https://megan-le-hha504-azure-flask-demo.azurewebsites.net/
* Due Sep 17th
* HHA 504 HW 2
* Assignment details below

# Instructions on how to complete this assignment
## Setting up:
1. Create a repo named azure_flask_deployment in github. Click the option to add a readme file and a license. Choose the Unlicense.
2. To bring over this newly created repo into google cloud shell, open google cloud shell and in the terminal do the command "git clone" and then paste the URL of your repo. 
3. Once you have your repo copied over to the shell, head to https://github.com/hantswilliams/HHA_504_2023/tree/main/WK2/flaskapp_0
4. From here you'll copy over the existing app.py, the files in the templates folder (about.html), (base.html), (data.html)
5. These files will be used and modified to suit your own needs

## Editing the files brought over
1. Since this is a site meant to display a dataset, find a CSV dataset. 
2. Below is what the unmodified app.py file looks like
```
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/about')
def about():
    return render_template('about.html')

df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/HHA_504_2023/main/WK1/data/113243405_StonyBrookSouthamptonHospital_StandardCharges.csv')
@app.route('/data')
def data(data=df):
    data = data.sample(15)
    return render_template('data.html', data=data)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )
```
3. As my chosen CSV was a ranking of happiness in the countries around the world, I changed the data = data.sample(15) to  data = data.head(15) to instead return the top 15 happiest countries rather than 15 random countries from the CSV file.
4. I uploaded my chosen CSV file by right clicking within the shell and hitting the button to "upload file"
5. I then changed the link within the parentheses to instead lead to my chosen CSV file df = pd.read_csv('data/2015.csv'). You can replace the name within the parentheses to the name of your chosen CSV file
6. Create a requirements.txt file with faker,pandas, and flask listed each in separate lines
7. Edit the 3 html files accordingly to display the text you want to see on your site.
8. Within the data.html file you will need to list each column in your CSV file. Follow the pattern of adding 1 line in the top half and then in the bottom half you add another line with an increased integer (0,1,2 etc.)

## Deploying with Azure
1. Install Azure CLI with ```curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash```, paste this whole command into your terminal
2. Type in  ```az```. and then type in ```az login --use-device-code```. YOu will be given a link and a code. Copy the code into the box in the link to connect your current session with your Azure account.
3. Within your Azure account find the tab "Resource Group" and create a new resource group with a unique name. THen hit "Review and Create".
4. Back in the shell environment go to the terminal and type in ```az account list --output table```. This is to make sure you are in the right subscription (the Azure for students). If this subscription isn't the default, type in ```az account set --subscription "desired SubscriptionId"```. Ignore the quotation marks.
5. Now that you're in the right subscription, type in ```az group list``` and a bunch of stuff should appear, and you should see the name of the resource group you made.
6. To create your webapp type in ```az webapp up --name "examplename" --runtime PYTHON:3.9 --sku B1`` again, ignore the quotation marks when actually typing in the terminal. Once you do this, the Azure App service will start to spin up and you will need to wait for a bit.
7. Once this process finishes, you can find the link to your new webpage in the terminal itself, or navigate to the App Services page within the Azure website.
8. If you make any changes to your app.py or html files and want it reflected on your site, you will have to repeat step 6 once again.



## **Week 2 Homework Assignment: Introducing Flask and Azure Deployment**

### **Objective**:
Get hands-on experience setting up a Flask application, integrate it with data processing via Pandas, and deploy the app on Azure App Service. You'll also practice documenting your process and using GitHub for project management.

### **Instructions**:

#### **1. Setting Up Your Flask Application**:
- Initiate a new Flask application. You can use one of my to start. I would recommend WK2 -> `flaskapp_0`, or if you want to go off of the more advanced modular version, please see `flaskapp_1`  
- Integrate Jinja templating to set up a homepage (`base.html`) for your app. 
- **OPTIONAL**: Use Pandas to load data from a provided file (choose a format: CSV, JSON). Ensure that your data file is less than 10MB for efficient loading. 
  - Display the data on your homepage using a basic table.
  - The code that you will want to modify is found in the `app.py` file and in the `data.html` files 

#### **2. Deploying on Azure App Service**:
- Deploy your Flask application to Azure App Service.
  - Use the lecture resources as a guide.
  - For additional help, refer to the [Azure App Service Quickstart for Python](https://learn.microsoft.com/en-us/azure/app-service/quickstart-python).
- Make sure your application is live and accessible via the provided URL. 

#### **(Optional) FastAPI Exploration**:
- Explore the FastAPI framework.
- Set up and deploy a basic FastAPI application on Azure App Service.

#### **3. Preparing Your GitHub Submission**:
- Create a new GitHub repository named `azure_flask_deployment` in your GitHub account.
- Feel free to re-use parts of your code from prior assignments where necessary 
  - Include your Python code for the Flask application.
  - Upload the data file you used.
  - Ensure your README.md file clearly details:
    - A step-by-step guide on how you set up and deployed your application. Imagine you're guiding someone unfamiliar with the process.
    - Make use of markdown features, especially code blocks, to format your instructions neatly. For reference on markdown syntax, refer to the [Markdown Guide](https://www.markdownguide.org/basic-syntax/).
  - Provide the deployed URL of your application in this README.

### **Submission**:
- Share the link to your `azure_flask_deployment` GitHub repository as your assignment submission.
- Ensure your repository is public so that it's accessible for review.

**Tip**: Keep your commits regular and meaningful. This not only backs up your work but also provides a trail of your progress and understanding.
