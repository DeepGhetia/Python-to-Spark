import pandas as pd
import numpy as np
from datetime import datetime, timedelta

user_df = pd.read_csv('C:/Users/hp/Desktop/User Data.csv')
# print(user_df.head())

event_df = pd.read_csv('C:/Users/hp/Desktop/Event Data.csv')
# print(event_df.head())

event_df["Timestamp"] = pd.to_datetime(event_df["Timestamp"].str.replace(" Z", ""))
user_df["Funding Date"] = pd.to_datetime(user_df["Funding Date"])
user_df["Opportunity Created Date"] = pd.to_datetime(user_df["Opportunity Created Date"])
user_df["Lead Created Date"] = pd.to_datetime(user_df["Lead Created Date"].str.replace(" Z", ""))

# Merge datasets on User ID
merged_df = pd.merge(event_df, user_df, on="User ID", how="left")
may_df = merged_df[(merged_df["Timestamp"].dt.month == 5) & (merged_df["Timestamp"].dt.year == 2024)]
print(may_df.dtypes)
print(may_df.head())
print(may_df.count())

# merged_df.to_csv('C:/Users/hp/Desktop/merged_data.csv', index=False)

# Code to count number of unique users per event
# converting raw event names to cleaned names
event_name_map = {
    # Landing / Visit
    "spring_ploan_app_landed": "Landing/Visit / Application Start",
    "spring_homepage_landed": "Landing/Visit / Application Start",
    "spring_ploan_page_landed": "Landing/Visit / Application Start",
    "spring_quiz_landed": "Landing/Visit / Application Start",
    # Application Start
    "spring_ploan_register_account_continue": "Landing/Visit / Application Start",
    "spring_apply_now_hero_email_submit": "Landing/Visit / Application Start",
    "spring_ploan_applynow_landed": "Landing/Visit / Application Start",
    "spring_ploan_applynow_v_2_landed": "Landing/Visit / Application Start",
    "spring_ploan_prepop_app_landed": "Landing/Visit / Application Start",
    "try_foundation_flow_entered": "Landing/Visit / Application Start",
    # User Info Entry
    "spring_ploan_email_continue": "User Info Entry",
    "spring_ploan_phone_number_continue": "User Info Entry",
    "spring_ploan_verification_code_inserted_continue": "User Info Entry",
    "spring_ploan_returning_customer_account_sign_in_email_submit": "Returning User",
    "spring_homepage_email_submit": "User Info Entry",
    "spring_personal_loans_email_submit": "User Info Entry",
    "spring_static_post_email_submit": "User Info Entry",
    "spring_quiz_email_fnln_submit": "User Info Entry",
    # Banking Info
    "spring_ploan_fi_selector_page_landed": "Banking Info",
    "spring_ploan_fi_selector_bank_selected": "Banking Info",
    "spring_ploan_plaid_page_landed": "Banking Info",
    "spring_ploan_plaid_submit_credential": "Banking Info",
    "spring_ploan_bankdetails_step_completed": "Banking Info",
    "spring_ploan_flinks_page_landed": "Banking Info",
    "spring_ploan_flinks_submit_credential": "Banking Info",
    # Pre-Populated Flow
    "spring_ploan_prepop_existing": "Pre-Populated Flow",
    "spring_ploan_prepop_new": "Pre-Populated Flow",
    "spring_ploan_deeper_prepop_page_landed": "Pre-Populated Flow",
    "spring_ploan_prepop_insufficient_app_landed": "Pre-Populated Flow",
    # Returning User Flow
    "spring_ploan_returning_customer_account_sign_in_continue": "Returning User",
    "spring_ploan_returning_customer_account_sign_in_submitted": "Returning User",
    "spring_ploan_returning_customer_app_landed": "Returning User",
    "spring_ploan_returning_customer_plaid_page_landed": "Returning User",
    "spring_ploan_returning_customer_flinks_page_landed": "Returning User",
    "spring_ploan_returning_customer_account_sign_in_email_submit": "Returning User",
    # Application Submit
    "spring_ploan_app_finished": "Application Submit",
    "spring_ploan_app_finished_docs_submitted": "Application Submit",
    # Affiliate / Promo
    "spring_affiliate_neo_email_submit": "Affiliate/Promo",
    "spring_affiliate_neo_landed": "Affiliate/Promo",
    "spring_promo_email_submit": "Affiliate/Promo",
    "spring_promo_landed": "Affiliate/Promo",
}

may_df["Clean Event"] = may_df["Event"].map(event_name_map).fillna(may_df["Event"])
event_counts = may_df.groupby("Clean Event")["User ID"].nunique().sort_values(ascending=False).reset_index()
event_counts.columns = ["Clean Event", "Unique Users"]

# Total unique users
total_users = may_df["User ID"].nunique()
event_counts["% of Total Users"] = (event_counts["Unique Users"] / total_users * 100).round(2)

# Print the top 10 events with highest user counts
print("Top 10 Events by Unique Users:")
print(event_counts.head(10))
event_counts.to_csv('C:/Users/hp/Desktop/event_counts.csv', index=False)

#code to get the approval ratio
def parse_requested_amount(range_str):
    if pd.isnull(range_str):
        return np.nan
    try:
        parts = range_str.replace("$", "").replace(",", "").split(" - ")
        if len(parts) == 2:
            low, high = map(int, parts)
            return (low + high) / 2
    except Exception:
        return np.nan
    return np.nan

# Convert Requested Loan Amount from range string to numeric
may_df["Requested Loan Amount"] = may_df["Requested Loan Amount"].apply(parse_requested_amount)
may_df["Approved Loan Amount"] = may_df["Approved Loan Amount"].astype(float)

# Group by Province and sum amounts
province_conversion = may_df.groupby("Province").agg({"Requested Loan Amount": "sum","Approved Loan Amount": "sum"}).reset_index()

# Calculate Approval Ratio, handling divide-by-zero safely
province_conversion["Approval Ratio"] = (province_conversion["Approved Loan Amount"] / province_conversion["Requested Loan Amount"].replace(0, np.nan)).round(2)

#dipslay result
print(province_conversion)
province_conversion.to_csv('C:/Users/hp/Desktop/province_conversion.csv', index=False)

# loan approval ratio
lead_status_approval = may_df.groupby("Lead Status").agg({"User ID": "nunique","Approved Loan Amount": lambda x: (x > 0).sum()}).reset_index()
lead_status_approval.columns = ["Lead Status", "Total Users", "Loan Approvals"]
lead_status_approval["Approval Rate"] = (lead_status_approval["Loan Approvals"] / lead_status_approval["Total Users"]).round(2)
print(lead_status_approval.sort_values("Approval Rate", ascending=False))
lead_status_approval.to_csv('C:/Users/hp/Desktop/lead_status_approval.csv', index=False)

# Event frequency by Source and Event
source_event_counts = may_df.groupby(["Source", "Clean Event"])["User ID"].nunique().unstack(fill_value=0)
print(source_event_counts)
source_event_counts.to_csv('C:/Users/hp/Desktop/source_event_counts.csv', index=False)

# code to calculate drop rates
funnel_stages = ["Landing/Visit / Application Start", "User Info Entry", "Banking Info", "Application Submit"]
funnel_progression = {}
for i, stage in enumerate(funnel_stages):
    users = set(may_df[may_df["Clean Event"] == stage]["User ID"])
    funnel_progression[stage] = len(users)

print(funnel_progression)

for i in range(1, len(funnel_stages)):
    prev, curr = funnel_stages[i-1], funnel_stages[i]
    drop_rate = abs(1 - (funnel_progression[curr] / funnel_progression[prev]))
    print(f"Drop from {prev} to {curr}: {drop_rate:.2%}")