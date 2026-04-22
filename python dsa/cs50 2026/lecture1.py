from openai import OpenAI
client = OpenAI()
response = client.responses. create(
    input = " In one sentnence, explain the conecept of machine learning.",
    model = "gpt-5"
)
print(response.output_text)