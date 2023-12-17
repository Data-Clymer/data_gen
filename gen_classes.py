
from faker import Faker
import random
import uuid
import datetime

class FakeDataGenerator:
    def __init__(self):
        self.fake = Faker()

        # initialize faker
        fake = Faker()
    #Faker.seed()
    def create_address(prefix=''):
            return {
                f'{prefix}address': fake.address(),
                f'{prefix}city': fake.city(),
                f'{prefix}country': fake.country(),
                f'{prefix}countrycode': fake.country_code(),
                f'{prefix}geocodeaccuracy': random.choice(['address', 'nearaddress', 'block', 'street', 'extendedzip', 'zip', 'city', 'county', 'state', 'country']),
                f'{prefix}latitude': fake.latitude(),
                f'{prefix}longitude': fake.longitude(),
                f'{prefix}phonenumber': fake.phone_number(),
                f'{prefix}postalcode': fake.postcode(),
                f'{prefix}state': fake.state(),
                f'{prefix}statecode': fake.state_abbr(),
                f'{prefix}street': fake.street_address()
            }
    def generate_salesforce_account():
            created_date = fake.past_date(start_date='-2y')
            last_modified_date = fake.date_time_between_dates(datetime_start=created_date, datetime_end=datetime.datetime.now())
            return {
                'id': str(uuid.uuid4()),
                'is_deleted': random.choice([True, False]),
                'master_record_id': str(uuid.uuid4()),
                'name': fake.company(),
                'type': random.choice(['customer - direct', 'customer - channel', 'channel partner / reseller', 'installation partner', 'technology partner', 'other']),
                'record_type_id': str(uuid.uuid4()),
                'parent_id': str(uuid.uuid4()),
                **create_address('billing'),
                'billing_geocode_accuracy': random.choice(['address', 'nearaddress', 'block', 'street', 'extendedzip', 'zip', 'neighborhood', 'city', 'county', 'state', 'country']),
                **create_address('shipping'),
                'shipping_geocode_accuracy': random.choice(['address', 'nearaddress', 'block', 'street', 'extendedzip', 'zip', 'neighborhood', 'city', 'county', 'state', 'country']),
                'phone': fake.phone_number(),
                'website': fake.url(),
                'photo_url': fake.image_url(),
                'industry': random.choice(['banking', 'consulting', 'education', 'electronics', 'energy', 'engineering', 'entertainment', 'finance', 'food & beverage', 'healthcare', 'hospitality', 'insurance', 'machinery', 'manufacturing', 'media', 'not for profit', 'recreation', 'retail', 'shipping', 'technology', 'telecommunications', 'transportation', 'utilities']),
                'number_of_employees': random.randint(1, 10000),
                'description': fake.text(),
                'owner_id': str(uuid.uuid4()),
                'created_date': created_date.isoformat(),
                'created_by_id': str(uuid.uuid4()),
                'last_modified_date': last_modified_date.isoformat(),
                'last_modified_by_id': str(uuid.uuid4()),
                'system_modstamp': fake.date_time_this_decade().isoformat(),
                'last_activity_date': fake.date_time_this_month().isoformat(),
                'last_viewed_date': fake.date_time_this_month().isoformat(),
                'last_referenced_date': fake.date_time_this_month().isoformat(),
                'jigsaw': str(random.randint(100000, 999999)),
                'jigsaw_company_id': str(random.randint(100000, 999999)),
                'account_source': random.choice(['web', 'phone inquiry', 'partner referral', 'purchased list', 'other']),
                'ownership': random.choice(['public', 'private', 'subsidiary', 'other']),
                'annual_revenue': round(random.uniform(10000, 10000000), 2),
                'account_number': str(random.randint(100000, 999999))
            }
    def generate_salesforce_opportunity(account_ids=None):
            created_date = fake.past_date(start_date='-2y')  # set a created date within the past two years
            close_date = fake.date_between(start_date='today', end_date='+1y')
            last_modified_date = fake.date_time_between_dates(datetime_start=created_date, datetime_end=datetime.datetime.now())
            # if account_ids are provided and not empty, use them; otherwise, generate random ids
            if account_ids and len(account_ids) > 0:
                account_id = random.choice(account_ids)
            else:
                account_id = str(uuid.uuid4())
            is_closed = random.choice([True, False])
            is_won = is_closed and random.choice([True, False])
            return {
                'id': str(uuid.uuid4()),
                'is_deleted': random.choice([True, False]),
                'account_id': account_id,
                'record_type_id': str(uuid.uuid4()),
                'name': f'{fake.company()} opportunity',
                'description': fake.text(),
                'stage_name': random.choice(['prospecting', 'qualification', 'needs analysis', 'value proposition', 'id. decision makers', 'perception analysis', 'proposal/price quote', 'negotiation/review', 'closed won', 'closed lost']),
                'amount': round(random.uniform(10000, 500000), 2),
                'probability': random.randint(0, 100),
                'close_date': close_date.isoformat(),
                'type': random.choice(['existing business', 'new business']),
                'next_step': fake.sentence(),
                'lead_source': random.choice(['web', 'phone inquiry', 'partner referral', 'purchased list', 'other']),
                'is_closed': is_closed,
                'is_won': is_won,
                'forecast_category': random.choice(['pipeline', 'best case', 'commit', 'closed', 'omitted']),
                'forecast_category_name': random.choice(['pipeline', 'best case', 'commit', 'closed', 'omitted']),
                'campaign_id': str(uuid.uuid4()),
                'has_opportunity_line_item': random.choice([True, False]),
                'is_split': random.choice([True, False]),
                'pricebook_2_id': str(uuid.uuid4()),
                'owner_id': str(uuid.uuid4()),
                'created_date': created_date.isoformat(),
                'created_by_id': str(uuid.uuid4()),
                'last_modified_date': last_modified_date.isoformat(),
                'last_modified_by_id': str(uuid.uuid4()),
                'system_modstamp': fake.date_time_this_decade().isoformat(),
                'last_activity_date': fake.date_time_this_month().isoformat(),
                'push_count': random.randint(0, 10),
                'last_stage_change_date': fake.date_time_this_year().isoformat(),
                'fiscal_quarter': random.choice([1, 2, 3, 4]),
                'fiscal_year': random.randint(2020, 2023),
                'fiscal': f'q{random.choice([1, 2, 3, 4])}-{random.randint(2020, 2023)}',
                'contact_id': str(uuid.uuid4()),
                'last_viewed_date': fake.date_time_this_month().isoformat(),
                'last_referenced_date': fake.date_time_this_month().isoformat(),
                'synced_quote_id': str(uuid.uuid4()),
                'contract_id': str(uuid.uuid4()),
                'has_open_activity': random.choice([True, False]),
                'has_overdue_task': random.choice([True, False]),
                'last_amount_changed_history_id': str(uuid.uuid4()),
                'last_close_date_changed_history_id': str(uuid.uuid4())
            }
    def generate_salesforce_quote(account_ids=None, opportunity_ids=None):
            # if account_ids and/or opportunity_ids are provided and not empty, use them; otherwise, generate random ids
            if account_ids and len(account_ids) > 0:
                account_id = random.choice(account_ids)
            else:
                account_id = str(uuid.uuid4())
            if opportunity_ids and len(opportunity_ids) > 0:
                opportunity_id = random.choice(opportunity_ids)
            else:
                opportunity_id = fake.uuid4()
            return {
                'id': str(uuid.uuid4()),
                'accountid': account_id,
                **create_address('additional'),
                'billtocontactid': fake.uuid4(),
                **create_address('billing'),
                'calculationstatus': random.choice(['draft', 'completed', 'in progress']),
                'cancreatequotelineitems': fake.boolean(),
                'contactid': fake.uuid4(),
                'contractid': fake.uuid4(),
                'currencyisocode': fake.currency_code(),
                'description': fake.text(),
                'discount': round(random.uniform(0, 100), 2),
                'email': fake.email(),
                'expirationdate': fake.date(),
                'fax': fake.phone_number(),
                'grandtotal': round(random.uniform(100, 10000), 2),
                'issyncing': fake.boolean(),
                'lastreferenceddate': fake.date(),
                'lastvieweddate': fake.date(),
                'lineitemcount': random.randint(1, 100),
                'name': fake.name(),
                'opportunityid': opportunity_id,
                'phone': fake.phone_number(),
                'pricebook2id': fake.uuid4(),
                'quotenumber': fake.bothify(text='???-#######'),
                **create_address('quoteto'),
                'recordtypeid': fake.uuid4(),
                **create_address('shipping'),
                'shippinghandling': round(random.uniform(0, 500), 2),
                'status': random.choice(['draft', 'in review', 'approved']),
                'subtotal': round(random.uniform(100, 5000), 2),
                'tax': round(random.uniform(0, 500), 2),
                'totalprice': round(random.uniform(1000, 20000), 2),
                'totalpricewithtax': round(random.uniform(1100, 22000), 2),
                'totaltaxamount': round(random.uniform(0, 500), 2)
            }
    def generate_salesforce_order(account_ids=None, opportunity_ids=None, quote_ids=None):
            # if account_ids and/or opportunity_ids and/or quote_ids are provided and not empty, use them; otherwise, generate random ids
            if account_ids and len(account_ids) > 0:
                account_id = random.choice(account_ids)
            else:
                account_id = str(uuid.uuid4())
            if opportunity_ids and len(opportunity_ids) > 0:
                opportunity_id = random.choice(opportunity_ids)
            else:
                opportunity_id = fake.uuid4()    
            if quote_ids and len(quote_ids) > 0:
                quote_id = random.choice(quote_ids)
            else:
                quote_id = fake.uuid4()
            return {
                'id': str(uuid.uuid4()),
                'accountid': account_id,
                'activatedbyid': fake.uuid4(),
                'activateddate': fake.date(),
                **create_address('billing'),
                'billingemailaddress': fake.email(),
                'billtocontactid': fake.uuid4(),
                'companyauthorizedbyid': fake.uuid4(),
                'companyauthorizeddate': fake.date(),
                'contractid': fake.uuid4(),
                'currencyisocode': fake.currency_code(),
                'customerauthorizedbyid': fake.uuid4(),
                'customerauthorizeddate': fake.date(),
                'description': fake.text(),
                'effectivedate': fake.date(),
                'enddate': fake.date(),
                'grandtotalamount': round(random.uniform(100, 10000), 2),
                'isreductionorder': fake.boolean(),
                'lastreferenceddate': fake.date(),
                'lastvieweddate': fake.date(),
                'name': fake.name(),
                'opportunityid': opportunity_id,
                'ordereddate': fake.date(),
                'ordermanagementreferenceidentifier': fake.random_number(digits=8),
                'ordernumber': fake.bothify(text='??-#######'),
                'orderreferencenumber': fake.bothify(text='##-#####'),
                'originalorderid': fake.uuid4(),
                'ownerid': fake.uuid4(),
                'paymenttermid': fake.uuid4(),
                'podate': fake.date(),
                'ponumber': fake.bothify(text='po#####'),
                'pricebook2id': fake.uuid4(),
                'quoteid': quote_id,
                'recordtypeid': fake.uuid4(),
                'relatedorderid': fake.uuid4(),
                'saleschannelid': fake.uuid4(),
                'salesstoreid': fake.uuid4(),
                **create_address('shipping'),
                'shiptocontactid': fake.uuid4(),
                'status': random.choice(['draft', 'activated', 'completed']),
                'statuscode': fake.bothify(text='##-###'),
                'taxlocaletype': random.choice(['local', 'state', 'national']),
                'totaladjdeliveryamtwithtax': round(random.uniform(0, 500), 2),
                'totaladjproductamtwithtax': round(random.uniform(0, 500), 2),
                'totaladjusteddeliveryamount': round(random.uniform(0, 500), 2),
                'totaladjusteddeliverytaxamount': round(random.uniform(0, 500), 2),
                'totaladjustedproductamount': round(random.uniform(0, 500), 2),
                'totaladjustedproducttaxamount': round(random.uniform(0, 500), 2),
                'totalamount': round(random.uniform(100, 10000), 2),
                'totaldeliveryadjdistamount': round(random.uniform(0, 500), 2),
                'totaldeliveryadjdistamtwithtax': round(random.uniform(0, 500), 2),
                'totaldeliveryadjdisttaxamount': round(random.uniform(0, 500), 2),
                'totalproductadjdistamount': round(random.uniform(0, 500), 2),
                'totalproductadjdistamtwithtax': round(random.uniform(0, 500), 2),
                'totalproductadjdisttaxamount': round(random.uniform(0, 500), 2),
                'totaltaxamount': round(random.uniform(0, 500), 2),
                'type': random.choice(['standard', 'renewal', 'new business'])
            }
    def generate_salesforce_user(account_ids=None):
            # if account_ids and/or opportunity_ids and/or quote_ids are provided and not empty, use them; otherwise, generate random ids
            if account_ids and len(account_ids) > 0:
                account_id = random.choice(account_ids)
            else:
                account_id = str(uuid.uuid4())
            return {
                'id': str(uuid.uuid4()),
                'aboutme': fake.text(),
                'accountid': account_id,
                'address': fake.address(),
                'alias': fake.user_name(),
                'badgetext': fake.sentence(),
                'bannerphotourl': fake.image_url(),
                'callcenterid': str(uuid.uuid4()),
                'city': fake.city(),
                'communitynickname': fake.user_name(),
                'companyname': fake.company(),
                'contactid': str(uuid.uuid4()),
                'country': fake.country(),
                'countrycode': fake.country_code(),
                'currentstatus': fake.sentence(),
                'defaultcurrencyisocode': fake.currency_code(),
                'defaultdivision': fake.word(),
                'defaultgroupnotificationfrequency': random.choice(['daily', 'weekly', 'monthly']),
                'delegatedapproverid': str(uuid.uuid4()),
                'department': fake.job(),
                'digestfrequency': random.choice(['daily', 'weekly', 'monthly']),
                'division': fake.word(),
                'email': fake.email(),
                'emailencodingkey': 'utf-8',
                'emailpreferencesautobcc': fake.boolean(),
                'employeenumber': fake.random_number(digits=5),
                'extension': fake.random_number(digits=4),
                'fax': fake.phone_number(),
                'federationidentifier': fake.uuid4(),
                'firstname': fake.first_name(),
                'forecastenabled': fake.boolean(),
                'fullphotourl': fake.image_url(),
                'geocodeaccuracy': random.choice(['address', 'nearaddress', 'block', 'street', 'postalcode', 'locality', 'administrativearea', 'region', 'country']),
                'individualid': str(uuid.uuid4()),
                'isactive': fake.boolean(),
                'ispartner': fake.boolean(),
                'isportalenabled': fake.boolean(),
                'isportalselfregistered': fake.boolean(),
                'isprmsuperuser': fake.boolean(),
                'isprofilephotoactive': fake.boolean(),
                'jigsawimportlimitoverride': fake.random_number(),
                'languagelocalekey': fake.locale(),
                'lastlogindate': fake.date_time(),
                'lastname': fake.last_name(),
                'lastreferenceddate': fake.date_time(),
                'lastvieweddate': fake.date_time(),
                'latitude': fake.latitude(),
                'localesidkey': fake.locale(),
                'longitude': fake.longitude(),
                'manager': fake.name(),
                'managerid': str(uuid.uuid4()),
                'mediumbannerphotourl': fake.image_url(),
                'middlename': fake.first_name(),
                'mobilephone': fake.phone_number(),
                'name': fake.name(),
                'numberoffailedlogins': fake.random_digit(),
                'offlinetrialexpirationdate': fake.date_time(),
                'phone': fake.phone_number(),
                'portalrole': random.choice(['executive', 'manager', 'worker']),
                'postalcode': fake.postcode(),
                'profileid': str(uuid.uuid4()),
                'receivesadmininfoemails': fake.boolean(),
                'receivesinfoemails': fake.boolean(),
                'senderemail': fake.email(),
                'sendername': fake.name(),
                'signature': fake.text(max_nb_chars=80),
                'smallbannerphotourl': fake.image_url(),
                'smallphotourl': fake.image_url(),
                'state': fake.state(),
                'statecode': fake.state_abbr(),
                'street': fake.street_address(),
                'suffix': fake.suffix(),
                'timezonesidkey': fake.timezone(),
                'title': fake.job(),
                'username': fake.email(),
                'userroleid': str(uuid.uuid4()),
                'usertype': random.choice(['standard', 'admin', 'custom']),
                'wirelessemail': fake.email()
            }
