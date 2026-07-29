application_name = "GrowthOs"
ai_model = "gpt-4.1"
data_base_url = "postgresql://username:password@localhost:5432/my_database"
api_version = " v2.1"
maximum_retries = 5 
request_timeout = 60 
environment = "Development"

print("===================Application Configuration=======================")
print(f"Appliation Name : {application_name}")
print(f"AI Model : {ai_model}")
print(f"Database URL : {data_base_url}")
print(f"API Version : {api_version}")
print(f"Maximum Retries : {maximum_retries}")
print(f"Request Timout  : {request_timeout}")
print(f"Envrironment: {environment}")
print("===================================================================")
