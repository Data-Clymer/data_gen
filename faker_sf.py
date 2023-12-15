from faker import Faker
import random
import uuid
import datetime

# Initialize Faker
fake = Faker()

def generate_opportunity(account_ids=None):
    created_date = fake.past_date(start_date="-2y")  # Set a created date within the past two years
    close_date = fake.date_between(start_date="today", end_date="+1y")
    last_modified_date = fake.date_time_between_dates(datetime_start=created_date, datetime_end=datetime.datetime.now())

    # If account_ids are provided and not empty, use them; otherwise, generate random ids
    if account_ids and len(account_ids) > 0:
        account_id = random.choice(account_ids)
    else:
        account_id = str(uuid.uuid4())

    is_closed = random.choice([True, False])
    is_won = is_closed and random.choice([True, False])

    opportunity = {
        "id": str(uuid.uuid4()),
        "is_deleted": random.choice([True, False]),
        "account_id": account_id,
        "record_type_id": str(uuid.uuid4()),
        "name": f"{fake.company()} Opportunity",
        "description": fake.text(),
        "stage_name": random.choice(['Prospecting', 'Qualification', 'Needs Analysis', 'Value Proposition', 'Id. Decision Makers', 'Perception Analysis', 'Proposal/Price Quote', 'Negotiation/Review', 'Closed Won', 'Closed Lost']),
        "amount": round(random.uniform(10000, 500000), 2),
        "probability": random.randint(0, 100),
        "close_date": close_date.isoformat(),
        "type": random.choice(['Existing Business', 'New Business']),
        "next_step": fake.sentence(),
        "lead_source": random.choice(['Web', 'Phone Inquiry', 'Partner Referral', 'Purchased List', 'Other']),
        "is_closed": is_closed,
        "is_won": is_won,
        "forecast_category": random.choice(['Pipeline', 'Best Case', 'Commit', 'Closed', 'Omitted']),
        "forecast_category_name": random.choice(['Pipeline', 'Best Case', 'Commit', 'Closed', 'Omitted']),
        "campaign_id": str(uuid.uuid4()),
        "has_opportunity_line_item": random.choice([True, False]),
        "is_split": random.choice([True, False]),
        "pricebook_2_id": str(uuid.uuid4()),
        "owner_id": str(uuid.uuid4()),
        "created_date": created_date.isoformat(),
        "created_by_id": str(uuid.uuid4()),
        "last_modified_date": last_modified_date.isoformat(),
        "last_modified_by_id": str(uuid.uuid4()),
        "system_modstamp": fake.date_time_this_decade().isoformat(),
        "last_activity_date": fake.date_time_this_month().isoformat(),
        "push_count": random.randint(0, 10),
        "last_stage_change_date": fake.date_time_this_year().isoformat(),
        "fiscal_quarter": random.choice([1, 2, 3, 4]),
        "fiscal_year": random.randint(2020, 2023),
        "fiscal": f"Q{random.choice([1, 2, 3, 4])}-{random.randint(2020, 2023)}",
        "contact_id": str(uuid.uuid4()),
        "last_viewed_date": fake.date_time_this_month().isoformat(),
        "last_referenced_date": fake.date_time_this_month().isoformat(),
        "synced_quote_id": str(uuid.uuid4()),
        "contract_id": str(uuid.uuid4()),
        "has_open_activity": random.choice([True, False]),
        "has_overdue_task": random.choice([True, False]),
        "last_amount_changed_history_id": str(uuid.uuid4()),
        "last_close_date_changed_history_id": str(uuid.uuid4())
    }
    return opportunity

def generate_account():
    created_date = fake.past_date(start_date="-2y")
    last_modified_date = fake.date_time_between_dates(datetime_start=created_date, datetime_end=datetime.datetime.now())

    account = {
        "id": str(uuid.uuid4()),
        "is_deleted": random.choice([True, False]),
        "master_record_id": str(uuid.uuid4()),
        "name": fake.company(),
        "type": random.choice(['Customer - Direct', 'Customer - Channel', 'Channel Partner / Reseller', 'Installation Partner', 'Technology Partner', 'Other']),
        "record_type_id": str(uuid.uuid4()),
        "parent_id": str(uuid.uuid4()),
        "billing_street": fake.street_address(),
        "billing_city": fake.city(),
        "billing_state": fake.state(),
        "billing_postal_code": fake.postcode(),
        "billing_country": fake.country(),
        "billing_latitude": fake.latitude(),
        "billing_longitude": fake.longitude(),
        "billing_geocode_accuracy": random.choice(['Address', 'NearAddress', 'Block', 'Street', 'ExtendedZip', 'Zip', 'Neighborhood', 'City', 'County', 'State', 'Country']),
        "shipping_street": fake.street_address(),
        "shipping_city": fake.city(),
        "shipping_state": fake.state(),
        "shipping_postal_code": fake.postcode(),
        "shipping_country": fake.country(),
        "shipping_latitude": fake.latitude(),
        "shipping_longitude": fake.longitude(),
        "shipping_geocode_accuracy": random.choice(['Address', 'NearAddress', 'Block', 'Street', 'ExtendedZip', 'Zip', 'Neighborhood', 'City', 'County', 'State', 'Country']),
        "phone": fake.phone_number(),
        "website": fake.url(),
        "photo_url": fake.image_url(),
        "industry": random.choice(['Banking', 'Consulting', 'Education', 'Electronics', 'Energy', 'Engineering', 'Entertainment', 'Finance', 'Food & Beverage', 'Healthcare', 'Hospitality', 'Insurance', 'Machinery', 'Manufacturing', 'Media', 'Not For Profit', 'Recreation', 'Retail', 'Shipping', 'Technology', 'Telecommunications', 'Transportation', 'Utilities']),
        "number_of_employees": random.randint(1, 10000),
        "description": fake.text(),
        "owner_id": str(uuid.uuid4()),
        "created_date": created_date.isoformat(),
        "created_by_id": str(uuid.uuid4()),
        "last_modified_date": last_modified_date.isoformat(),
        "last_modified_by_id": str(uuid.uuid4()),
        "system_modstamp": fake.date_time_this_decade().isoformat(),
        "last_activity_date": fake.date_time_this_month().isoformat(),
        "last_viewed_date": fake.date_time_this_month().isoformat(),
        "last_referenced_date": fake.date_time_this_month().isoformat(),
        "jigsaw": str(random.randint(100000, 999999)),
        "jigsaw_company_id": str(random.randint(100000, 999999)),
        "account_source": random.choice(['Web', 'Phone Inquiry', 'Partner Referral', 'Purchased List', 'Other']),
        "ownership": random.choice(['Public', 'Private', 'Subsidiary', 'Other']),
        "annual_revenue": round(random.uniform(10000, 10000000), 2),
        "account_number": str(random.randint(100000, 999999))
    }
    return account
