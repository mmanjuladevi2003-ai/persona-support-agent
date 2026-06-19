from src.classifier import classify_customer_persona

message = "Your API keeps returning 401 errors. I checked the authentication headers."

result = classify_customer_persona(message)

print(result)