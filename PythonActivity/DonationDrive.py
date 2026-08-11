transaction_log = input("The transaction log is: ")

if transaction_log.endswith("2026"):
    transaction_log = transaction_log[:-1]
    donor_name = transaction_log[0:5]
    ref_id = transaction_log[6:11]
    if ref_id.isalnum() and donor_name != "" and "-" not in donor_name:
        name = donor_name.replace("-", " ")
        print("Log approved: " + name + " with Ref: " + ref_id + " has successfully donated to #TulongLuis2026!")
    else:
        print("Log Rejected: Invalid details or outdated transaction year.")
else:
        print("Log Rejected: Invalid details or outdated transaction year.")
        