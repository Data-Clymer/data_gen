##### Synthetic Data Generator
_by [Data Clymer](https://dataclymer.com/)_

This Streamlit application is designed to create realistic, synthetic data for Salesforce objects, aiding in development, testing, and training without using real customer data. 

##### How It Works

**Select Salesforce Objects:**
- Choose one or more Salesforce objects from: **Accounts, Opportunities, Users, Quotes, and Orders**.
 
**Specify Record Count:**
- Input the number of records you want to generate.
- Limited to **10,000 records** per object.
 
**Data Generation:**
- For objects **Opportunities, Quotes, and/or Orders**, the application intelligently creates dependencies based on **Account IDs**,**Opportunities IDs**, and **Quote IDs** ensuring realistic data relationships.

**Download Files:**
- After generation, scroll to the bottom of the application to download the objects as zipped CSV files.

**Learn More**
- [Github Repo](https://github.com/jake-data-clymer/data_gen)
- [Salesforce Object Reference](https://developer.salesforce.com/docs/atlas.en-us.246.0.object_reference.meta/object_reference/sforce_api_objects_list.htm)
- [Faker](https://faker.readthedocs.io/en/master/)
