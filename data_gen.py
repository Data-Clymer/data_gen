import streamlit as st
import pandas as pd
import datetime
import io
import zipfile

from gen_classes import FakeDataGenerator

st.set_page_config(page_title='Synthetic Data Generator', page_icon='🧊')

def create_zip_download_button(download_items, record_count):
    zip_buffer = io.BytesIO()
    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
        for object_name, df in download_items.items():
            if not df.empty:
                csv_string = df.to_csv(index=False).encode('utf-8')
                
                # Format the file name: replace spaces with underscores, convert to lowercase, and add timestamp
                formatted_object_name = object_name.replace(" ", "_").lower()
                file_name = f"{formatted_object_name}_{record_count}_records_{current_time}.csv"
                
                zip_file.writestr(file_name, csv_string)
    # Set the position of the buffer to the start
    zip_buffer.seek(0)
    
    # Create Streamlit download button object
    st.download_button(
        label="Download All Files (ZIP CSVs)",
        data=zip_buffer,
        file_name=f"sfdc_objects_{current_time}.zip",
        mime="application/zip"
    )

def main():
    st.title('Synthetic Data Generator')
    '---'
    with st.expander("**Application Details**", expanded=False):

        with open('welcome.md', 'r') as file:
            markdown_text = file.read()

        st.markdown(markdown_text, unsafe_allow_html=True)
        
    # User inputs
    record_count = st.number_input('Number of Records to Generate:', min_value=1, max_value=10000, value=10)
    
    objects = st.multiselect(
        'Select Objects to Generate',
        ['SFDC Account', 'SFDC User', 'SFDC Quote', 'SFDC Order', 'SFDC Opportunity'],
        default=['SFDC Account']
    )
    
    # Generate button
    if st.button('Generate Data'):
    
        account_ids = []
        opportunity_ids = []
        quote_ids = []
        
        download_items = {}
        fake_data_generator = FakeDataGenerator()
    
        if 'SFDC Account' in objects:
            account_data = [fake_data_generator.generate_salesforce_account() for _ in range(record_count)]
            account_ids = [acc['id'] for acc in account_data]
            account_df = pd.DataFrame(account_data)
            download_items['SFDC Account'] = account_df
            st.write('SDFC Account(s)')
            st.dataframe(account_df)

        if 'SFDC Opportunity' in objects:
            opportunity_data = [fake_data_generator.generate_salesforce_opportunity(account_ids) for _ in range(record_count)]
            opportunity_ids = [opp['id'] for opp in opportunity_data]
            opportunity_df = pd.DataFrame(opportunity_data)
            download_items['SFDC Opportunity'] = opportunity_df
            st.write('SDFC Opportunity(ies)')
            st.dataframe(opportunity_df)
            
        if 'SFDC User' in objects:
            user_data = [fake_data_generator.generate_salesforce_user(account_ids) for _ in range(record_count)]
            user_df = pd.DataFrame(user_data)
            download_items['SFDC User'] = user_df
            st.write('SDFC User(s)')
            st.dataframe(user_df)
            
        if 'SFDC Quote' in objects:
            quote_data = [fake_data_generator.generate_salesforce_quote(account_ids, opportunity_ids) for _ in range(record_count)]
            quote_ids = [qt['id'] for qt in quote_data]
            quote_df = pd.DataFrame(quote_data)
            download_items['SFDC Quote'] = quote_df
            st.write('SDFC Quote(s)')
            st.dataframe(quote_df)
            
        if 'SFDC Order' in objects:
            order_data = [fake_data_generator.generate_salesforce_order(account_ids, opportunity_ids, quote_ids) for _ in range(record_count)]
            order_df = pd.DataFrame(order_data)
            download_items['SFDC order'] = order_df
            st.write('SDFC Order(s)')
            st.dataframe(order_df)
            
        # Download button 
        create_zip_download_button(download_items, record_count)

if __name__ == '__main__':
    main()
