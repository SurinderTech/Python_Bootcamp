# Experiment 1
active_model = "gpt-4.1"
backup_model = active_model
active_model = "gpt-5.5"

print(f"Active Modal :, {active_model}")
print(f"Backup Model : ,{backup_model}")
print(f"Active Model Id : " ,id(active_model))
print(f"Backup Model Id : " ,id(backup_model))

# Experiment 2

enabled_tools = [ "openAI", "Firecrawl"]
backup_tools = enabled_tools
enabled_tools.append("supabase")

print(f"Enabled Tools : {enabled_tools}")
print(f"Backup Tools : {backup_tools}")
print(f"Enabled Tools Id : {id(enabled_tools)}")
print(f"Backup Tools id : {id(backup_tools)}")

# Experiment 3

enabled_tools = ["openAI","Firecrawl"]
backup_tools = enabled_tools.copy()
enabled


