import streamlit as st
import csv
import io

import faker_sf

st.set_page_config(page_title="Synthetic Data Generator", page_icon="🧊")

def convert_to_csv_string(file):
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=file[0].keys())
    writer.writeheader()
    for opportunity in file:
        writer.writerow(opportunity)
    return output.getvalue()

def main():
    st.title("Synthetic Data Generator")
    '---'

    # Initializing account session state object
    if 'account_state' not in st.session_state:
        st.session_state['account_state'] = None

    # User inputs
    object_type = st.selectbox("Select Object Type", ["SFDC Account","SFDC Opportunity"], index=0)
    record_count = st.number_input("Number of Records", min_value=1, max_value=1000, value=100)

    # Generate data button
    if st.button("Generate Data"):
        if object_type == "SFDC Account":
            st.session_state['account_state'] = None
            accounts = [faker_sf.generate_account() for _ in range(record_count)]
            account_ids = [acc["id"] for acc in accounts]
            st.session_state['account_state'] = account_ids
            st.dataframe(accounts)
            csv_string = convert_to_csv_string(accounts)
            st.download_button(
                label="Download CSV",
                data=csv_string,
                file_name="salesforce_account.csv",
                mime="text/csv"
            )
        if object_type == "SFDC Opportunity":
            opportunities = [faker_sf.generate_opportunity(st.session_state['account_state']) for _ in range(record_count)]
            st.dataframe(opportunities)
            csv_string = convert_to_csv_string(opportunities)
            st.download_button(
                label="Download CSV",
                data=csv_string,
                file_name="salesforce_opportunity.csv",
                mime="text/csv"
            )

if __name__ == "__main__":
    main()
