
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
    def create_address(self, prefix=''):
            return {
                f'{prefix}address': self.fake.address(),
                f'{prefix}city': self.fake.city(),
                f'{prefix}country': self.fake.country(),
                f'{prefix}countrycode': self.fake.country_code(),
                f'{prefix}geocodeaccuracy': random.choice(['address', 'nearaddress', 'block', 'street', 'extendedzip', 'zip', 'city', 'county', 'state', 'country']),
                f'{prefix}latitude': self.fake.latitude(),
                f'{prefix}longitude': self.fake.longitude(),
                f'{prefix}phonenumber': self.fake.phone_number(),
                f'{prefix}postalcode': self.fake.postcode(),
                f'{prefix}state': self.fake.state(),
                f'{prefix}statecode': self.fake.state_abbr(),
                f'{prefix}street': self.fake.street_address()
            }
    def generate_salesforce_account(self):
            created_date = self.fake.past_date(start_date='-2y')
            last_modified_date = self.fake.date_time_between_dates(datetime_start=created_date, datetime_end=datetime.datetime.now())
            
            billing_address = self.create_address(prefix='billing')
            shipping_address = self.create_address(prefix='shipping')
            
            return {
                'id': str(uuid.uuid4()),
                'is_deleted': random.choice([True, False]),
                'master_record_id': str(uuid.uuid4()),
                'name': self.fake.company(),
                'type': random.choice(['customer - direct', 'customer - channel', 'channel partner / reseller', 'installation partner', 'technology partner', 'other']),
                'record_type_id': str(uuid.uuid4()),
                'parent_id': str(uuid.uuid4()),
                **billing_address,
                'billing_geocode_accuracy': random.choice(['address', 'nearaddress', 'block', 'street', 'extendedzip', 'zip', 'neighborhood', 'city', 'county', 'state', 'country']),
                **shipping_address,
                'shipping_geocode_accuracy': random.choice(['address', 'nearaddress', 'block', 'street', 'extendedzip', 'zip', 'neighborhood', 'city', 'county', 'state', 'country']),
                'phone': self.fake.phone_number(),
                'website': self.fake.url(),
                'photo_url': self.fake.image_url(),
                'industry': random.choice(['banking', 'consulting', 'education', 'electronics', 'energy', 'engineering', 'entertainment', 'finance', 'food & beverage', 'healthcare', 'hospitality', 'insurance', 'machinery', 'manufacturing', 'media', 'not for profit', 'recreation', 'retail', 'shipping', 'technology', 'telecommunications', 'transportation', 'utilities']),
                'number_of_employees': random.randint(1, 10000),
                'description': self.fake.text(),
                'owner_id': str(uuid.uuid4()),
                'created_date': created_date.isoformat(),
                'created_by_id': str(uuid.uuid4()),
                'last_modified_date': last_modified_date.isoformat(),
                'last_modified_by_id': str(uuid.uuid4()),
                'system_modstamp': self.fake.date_time_this_decade().isoformat(),
                'last_activity_date': self.fake.date_time_this_month().isoformat(),
                'last_viewed_date': self.fake.date_time_this_month().isoformat(),
                'last_referenced_date': self.fake.date_time_this_month().isoformat(),
                'jigsaw': str(random.randint(100000, 999999)),
                'jigsaw_company_id': str(random.randint(100000, 999999)),
                'account_source': random.choice(['web', 'phone inquiry', 'partner referral', 'purchased list', 'other']),
                'ownership': random.choice(['public', 'private', 'subsidiary', 'other']),
                'annual_revenue': round(random.uniform(10000, 10000000), 2),
                'account_number': str(random.randint(100000, 999999))
            }
            
    def generate_salesforce_opportunity(self, account_ids=None):
            created_date = self.fake.past_date(start_date='-2y')  # set a created date within the past two years
            close_date = self.fake.date_between(start_date='today', end_date='+1y')
            last_modified_date = self.fake.date_time_between_dates(datetime_start=created_date, datetime_end=datetime.datetime.now())
            
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
                'name': f'{self.fake.company()} opportunity',
                'description': self.fake.text(),
                'stage_name': random.choice(['prospecting', 'qualification', 'needs analysis', 'value proposition', 'id. decision makers', 'perception analysis', 'proposal/price quote', 'negotiation/review', 'closed won', 'closed lost']),
                'amount': round(random.uniform(10000, 500000), 2),
                'probability': random.randint(0, 100),
                'close_date': close_date.isoformat(),
                'type': random.choice(['existing business', 'new business']),
                'next_step': self.fake.sentence(),
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
                'system_modstamp': self.fake.date_time_this_decade().isoformat(),
                'last_activity_date': self.fake.date_time_this_month().isoformat(),
                'push_count': random.randint(0, 10),
                'last_stage_change_date': self.fake.date_time_this_year().isoformat(),
                'fiscal_quarter': random.choice([1, 2, 3, 4]),
                'fiscal_year': random.randint(2020, 2023),
                'fiscal': f'q{random.choice([1, 2, 3, 4])}-{random.randint(2020, 2023)}',
                'contact_id': str(uuid.uuid4()),
                'last_viewed_date': self.fake.date_time_this_month().isoformat(),
                'last_referenced_date': self.fake.date_time_this_month().isoformat(),
                'synced_quote_id': str(uuid.uuid4()),
                'contract_id': str(uuid.uuid4()),
                'has_open_activity': random.choice([True, False]),
                'has_overdue_task': random.choice([True, False]),
                'last_amount_changed_history_id': str(uuid.uuid4()),
                'last_close_date_changed_history_id': str(uuid.uuid4())
            }
    def generate_salesforce_quote(self, account_ids=None, opportunity_ids=None):
            additional_address = self.create_address(prefix='additional')
            billing_address = self.create_address(prefix='billing')
            quoteto_address = self.create_address(prefix='quoteto')
            shipping_address = self.create_address(prefix='shipping')
            # if account_ids and/or opportunity_ids are provided and not empty, use them; otherwise, generate random ids
            if account_ids and len(account_ids) > 0:
                account_id = random.choice(account_ids)
            else:
                account_id = str(uuid.uuid4())
            if opportunity_ids and len(opportunity_ids) > 0:
                opportunity_id = random.choice(opportunity_ids)
            else:
                opportunity_id = self.fake.uuid4()
            return {
                'id': str(uuid.uuid4()),
                'accountid': account_id,
                **additional_address,
                'billtocontactid': self.fake.uuid4(),
                **billing_address,
                'calculationstatus': random.choice(['draft', 'completed', 'in progress']),
                'cancreatequotelineitems': self.fake.boolean(),
                'contactid': self.fake.uuid4(),
                'contractid': self.fake.uuid4(),
                'currencyisocode': self.fake.currency_code(),
                'description': self.fake.text(),
                'discount': round(random.uniform(0, 100), 2),
                'email': self.fake.email(),
                'expirationdate': self.fake.date(),
                'fax': self.fake.phone_number(),
                'grandtotal': round(random.uniform(100, 10000), 2),
                'issyncing': self.fake.boolean(),
                'lastreferenceddate': self.fake.date(),
                'lastvieweddate': self.fake.date(),
                'lineitemcount': random.randint(1, 100),
                'name': self.fake.name(),
                'opportunityid': opportunity_id,
                'phone': self.fake.phone_number(),
                'pricebook2id': self.fake.uuid4(),
                'quotenumber': self.fake.bothify(text='???-#######'),
                **quoteto_address,
                'recordtypeid': self.fake.uuid4(),
                **shipping_address,
                'shippinghandling': round(random.uniform(0, 500), 2),
                'status': random.choice(['draft', 'in review', 'approved']),
                'subtotal': round(random.uniform(100, 5000), 2),
                'tax': round(random.uniform(0, 500), 2),
                'totalprice': round(random.uniform(1000, 20000), 2),
                'totalpricewithtax': round(random.uniform(1100, 22000), 2),
                'totaltaxamount': round(random.uniform(0, 500), 2)
            }
    def generate_salesforce_order(self, account_ids=None, opportunity_ids=None, quote_ids=None):
            billing_address = self.create_address(prefix='billing')
            shipping_address = self.create_address(prefix='shipping')
            # if account_ids and/or opportunity_ids and/or quote_ids are provided and not empty, use them; otherwise, generate random ids
            if account_ids and len(account_ids) > 0:
                account_id = random.choice(account_ids)
            else:
                account_id = str(uuid.uuid4())
            if opportunity_ids and len(opportunity_ids) > 0:
                opportunity_id = random.choice(opportunity_ids)
            else:
                opportunity_id = self.fake.uuid4()    
            if quote_ids and len(quote_ids) > 0:
                quote_id = random.choice(quote_ids)
            else:
                quote_id = self.fake.uuid4()
            return {
                'id': str(uuid.uuid4()),
                'accountid': account_id,
                'activatedbyid': self.fake.uuid4(),
                'activateddate': self.fake.date(),
                **billing_address,
                'billingemailaddress': self.fake.email(),
                'billtocontactid': self.fake.uuid4(),
                'companyauthorizedbyid': self.fake.uuid4(),
                'companyauthorizeddate': self.fake.date(),
                'contractid': self.fake.uuid4(),
                'currencyisocode': self.fake.currency_code(),
                'customerauthorizedbyid': self.fake.uuid4(),
                'customerauthorizeddate': self.fake.date(),
                'description': self.fake.text(),
                'effectivedate': self.fake.date(),
                'enddate': self.fake.date(),
                'grandtotalamount': round(random.uniform(100, 10000), 2),
                'isreductionorder': self.fake.boolean(),
                'lastreferenceddate': self.fake.date(),
                'lastvieweddate': self.fake.date(),
                'name': self.fake.name(),
                'opportunityid': opportunity_id,
                'ordereddate': self.fake.date(),
                'ordermanagementreferenceidentifier': self.fake.random_number(digits=8),
                'ordernumber': self.fake.bothify(text='??-#######'),
                'orderreferencenumber': self.fake.bothify(text='##-#####'),
                'originalorderid': self.fake.uuid4(),
                'ownerid': self.fake.uuid4(),
                'paymenttermid': self.fake.uuid4(),
                'podate': self.fake.date(),
                'ponumber': self.fake.bothify(text='po#####'),
                'pricebook2id': self.fake.uuid4(),
                'quoteid': quote_id,
                'recordtypeid': self.fake.uuid4(),
                'relatedorderid': self.fake.uuid4(),
                'saleschannelid': self.fake.uuid4(),
                'salesstoreid': self.fake.uuid4(),
                **shipping_address,
                'shiptocontactid': self.fake.uuid4(),
                'status': random.choice(['draft', 'activated', 'completed']),
                'statuscode': self.fake.bothify(text='##-###'),
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
    def generate_salesforce_user(self, account_ids=None):
            # if account_ids and/or opportunity_ids and/or quote_ids are provided and not empty, use them; otherwise, generate random ids
            if account_ids and len(account_ids) > 0:
                account_id = random.choice(account_ids)
            else:
                account_id = str(uuid.uuid4())
            return {
                'id': str(uuid.uuid4()),
                'aboutme': self.fake.text(),
                'accountid': account_id,
                'address': self.fake.address(),
                'alias': self.fake.user_name(),
                'badgetext': self.fake.sentence(),
                'bannerphotourl': self.fake.image_url(),
                'callcenterid': str(uuid.uuid4()),
                'city': self.fake.city(),
                'communitynickname': self.fake.user_name(),
                'companyname': self.fake.company(),
                'contactid': str(uuid.uuid4()),
                'country': self.fake.country(),
                'countrycode': self.fake.country_code(),
                'currentstatus': self.fake.sentence(),
                'defaultcurrencyisocode': self.fake.currency_code(),
                'defaultdivision': self.fake.word(),
                'defaultgroupnotificationfrequency': random.choice(['daily', 'weekly', 'monthly']),
                'delegatedapproverid': str(uuid.uuid4()),
                'department': self.fake.job(),
                'digestfrequency': random.choice(['daily', 'weekly', 'monthly']),
                'division': self.fake.word(),
                'email': self.fake.email(),
                'emailencodingkey': 'utf-8',
                'emailpreferencesautobcc': self.fake.boolean(),
                'employeenumber': self.fake.random_number(digits=5),
                'extension': self.fake.random_number(digits=4),
                'fax': self.fake.phone_number(),
                'federationidentifier': self.fake.uuid4(),
                'firstname': self.fake.first_name(),
                'forecastenabled': self.fake.boolean(),
                'fullphotourl': self.fake.image_url(),
                'geocodeaccuracy': random.choice(['address', 'nearaddress', 'block', 'street', 'postalcode', 'locality', 'administrativearea', 'region', 'country']),
                'individualid': str(uuid.uuid4()),
                'isactive': self.fake.boolean(),
                'ispartner': self.fake.boolean(),
                'isportalenabled': self.fake.boolean(),
                'isportalselfregistered': self.fake.boolean(),
                'isprmsuperuser': self.fake.boolean(),
                'isprofilephotoactive': self.fake.boolean(),
                'jigsawimportlimitoverride': self.fake.random_number(),
                'languagelocalekey': self.fake.locale(),
                'lastlogindate': self.fake.date_time(),
                'lastname': self.fake.last_name(),
                'lastreferenceddate': self.fake.date_time(),
                'lastvieweddate': self.fake.date_time(),
                'latitude': self.fake.latitude(),
                'localesidkey': self.fake.locale(),
                'longitude': self.fake.longitude(),
                'manager': self.fake.name(),
                'managerid': str(uuid.uuid4()),
                'mediumbannerphotourl': self.fake.image_url(),
                'middlename': self.fake.first_name(),
                'mobilephone': self.fake.phone_number(),
                'name': self.fake.name(),
                'numberoffailedlogins': self.fake.random_digit(),
                'offlinetrialexpirationdate': self.fake.date_time(),
                'phone': self.fake.phone_number(),
                'portalrole': random.choice(['executive', 'manager', 'worker']),
                'postalcode': self.fake.postcode(),
                'profileid': str(uuid.uuid4()),
                'receivesadmininfoemails': self.fake.boolean(),
                'receivesinfoemails': self.fake.boolean(),
                'senderemail': self.fake.email(),
                'sendername': self.fake.name(),
                'signature': self.fake.text(max_nb_chars=80),
                'smallbannerphotourl': self.fake.image_url(),
                'smallphotourl': self.fake.image_url(),
                'state': self.fake.state(),
                'statecode': self.fake.state_abbr(),
                'street': self.fake.street_address(),
                'suffix': self.fake.suffix(),
                'timezonesidkey': self.fake.timezone(),
                'title': self.fake.job(),
                'username': self.fake.email(),
                'userroleid': str(uuid.uuid4()),
                'usertype': random.choice(['standard', 'admin', 'custom']),
                'wirelessemail': self.fake.email()
            }
