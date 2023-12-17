# data-gen
Streamlit UI to generate synthetic data for testing and development

### Salesforce Synthetic Data Model Overview

#### Account to Opportunity:
An Account can be associated with multiple Opportunities.
This relationship is often used to track potential sales and other business opportunities with a customer or organization.

#### Lead to Opportunity:
A Lead, once qualified, can be converted into an Account, Contact, and an Opportunity.
This is a one-time process in Salesforce, where the Lead essentially becomes an Opportunity associated with a new or existing Account.

#### Opportunity to Quote:
Opportunities can have multiple associated Quotes.
Quotes are detailed sales proposals or bids that are related to an Opportunity. They include proposed prices for products and services.

#### Quote to Order:
A Quote can lead to an Order once it is accepted by a customer.
The Order represents a confirmed agreement between the business and the customer to provide the specified products or services.

#### Opportunity to Order:
An Order can be directly associated with an Opportunity.
This signifies that the Order is the result of the Opportunity, representing the final sale agreement that details the products or services sold, their quantities, and agreed prices.
