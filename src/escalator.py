def should_escalate(query):

    escalation_keywords = [
        "refund",
        "billing dispute",
        "legal",
        "complaint"
    ]

    query_lower = query.lower()

    for keyword in escalation_keywords:
        if keyword in query_lower:
            return True

    return False