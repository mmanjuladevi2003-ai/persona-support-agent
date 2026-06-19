def classify_customer_persona(query):
    query = query.lower()

    if any(word in query for word in ["refund", "charged", "billing", "payment"]):
        return "Billing Customer"

    elif any(word in query for word in ["password", "login", "account"]):
        return "Technical Support Customer"

    elif any(word in query for word in ["complaint", "unhappy", "issue"]):
        return "Escalation Customer"

    else:
        return "General Customer"
