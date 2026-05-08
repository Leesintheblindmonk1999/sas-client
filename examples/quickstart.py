from sas_client import SASClient

client = SASClient(api_key="sas_test_key_2026")

print("Health:")
print(client.health())

print("
Diff:")
result = client.diff(
    text_a="Python is a programming language used for automation.",
    text_b="A python is a large tropical snake.",
)
print(result)
