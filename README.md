# SITE Django Web App

A web app built in Django with a PostgreSQL backend to showcase technologies and projects that have been completed by the SIA research team. Containerized environment with Docker, utilizing multiple containers. 

## Web App Features (in progress)

- GATHER: scrape multiple search engines based on the keyword input by the user and download results as individual PDFs. Provide user with a report of the results (list of URLs, categorized by search engine) and with zip file of PDFs.
- EXPLORE: take multiple PDFs from the user and generate standard analyses (word cloud, sentiment analysis, etc) to provide user in report form. Enables user to gain insights from a volume of unstructured text data without having to read all of them. Additionally, we can include some Twitter features here but not completely sure what those would look like just yet
- LEARN: BERT demo similar to the Allen Institute for AI (https://demo.allennlp.org/reading-comprehension/bidaf-elmo)

## How to Get Started in VSCode

Prerequisites:
- Visual Studio Code installed
- Remote Containers extension installed (Microsoft documentation for VSCode extensions: https://code.visualstudio.com/docs/editor/extension-marketplace)

1.  Clone the repository
2.  Open the sia-site-test folder in VSCode
3.  Ensure that the Remote Containers extension is installed
4.  Click on the "<>" in the bottom left hand corner of the window
5.  Select "Reopen in Container"
6.  The containers will build and start up (this may take a while on the first build)
7.  Once the containers are up and running you should see ">< Dev Container: sitetest container" in the bottom left hand corner of the window. You are now in the dockerized environment! You can edit, test, and push code to this repository. 

## Starting the Application

Once you have the containers running, you can navigate to the web application by entering "0.0.0.0:8000" in your browser. This is the local version of the web application running through the 8000 port of the dockerized environment.

## Connect to Database in VSCode
1. Make sure the PostgreSQL extension loaded from the container (an elephant icon will be on the toolbar in the left side of the window)
2. Click on the elephant, then click on the + button in the left pane
3. Fill in the requested fields as follows:
- Hostname: postgres
- User: debug
- Password: debug
- Port Number: 5432
- Standard Connection
- Database Name: sitetest

## View Database Tables in VSCode
1. Click on the PostgreSQL extension icon (elephant)
2. Expand sitetest, sitetest, and public
3. You should now see all the tables in the sitetest database
4. Right click on a table then click Select > Select Top...
5. You can now enter the number of rows you'd like to view from this table

## Deployment in Heroku
- Instructions coming soon!
- Production branch will be deployed to Heroku

## Django Resources
- Tutorial: https://realpython.com/get-started-with-django-1/
