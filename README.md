# PROJECT KAYAK - ETL (Extract - Transform - Load) - API, SCRAPING & STORAGE

## Description
The marketing team needs help on a new project. After doing some user research, the team discovered that 70% of their users who are planning a trip would like to have more information about the destination they are going to.

In addition, user research shows that people tend to be defiant about the information they are reading if they don't know the brand which produced the content.

Therefore, Kayak Marketing Team would like to create an application that will recommend where people should plan their next holidays. The application should be based on real data about:

* Weather
* Hotels in the area

## Goals
The project aims to construct application that will be able to recommend the best destinations and hotels based on the above variables at any given time. 


## Content
The project is organized into four main parts, each focusing on a specific aspect of the ETL process:

1. **Get weather data from each destination using API**
2. **Scrape data from destinations and hotels using booking.com**
3. **Store all the information above in a data lake**
4. **Transform and load cleaned data for analysis**


This repository consists of: 

- A notebook (Projet_KYK.ipynb) that includes two API requests, the execution of web scraping, the storage in an AWS S3 bucket, the creation of an SQL database in AWS RDS, and the analysis of the data.

- A file booking.py that contains the code for web scrapings

- Two datasets (hotels.json) and df_meteo.csv.


## Usage

To utilize and explore this project, follow these steps:

1. **Clone the Repository:**

   git clone https://github.com/Simoncld8/ETL_PROJECT_KYK.git


2. **Install Dependencies:**

   pip install -r requirements.txt  

3. **Run the Analysis:**

   You will find all the analysis in the Jupyter Notebook provided (`Projet_KYK.ipynb`).

## Warning

In this project, you will need to create an S3 bucket and an AWS RDS instance with your credentials. 
Please replace all the credentials in the notebook to play with the code. 

Moreover, please note that the booking.com development teams are currently changing the organization of their website. The scraping code could raise some errors. The same errors could appear for the API requests. 

If this code does not work, you will also find in this repository the datasets hotels.json and df_meteo.csv used for the analysis.


Contributors

Simon Claude

This project was undertaken as part of the "Data Science and Engineering Fullstack" program offered by Jedha. Its aim was to fulfill a component of the "Machine Learning Engineer" certification.
