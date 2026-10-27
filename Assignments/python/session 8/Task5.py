# 5. Create a function mask_phone_number(phone) that takes a 10-digit phone number as a string and returns it in the format '******1234', showing only the last 4 digits like Paytm does.<br><br><em><strong>Hint:</strong> Use string slicing and concatenation.</em>

def mask_phone_number(phone):
    masked = "******" + phone[6:]

    print(masked)

mask_phone_number("9876543210")