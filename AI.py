import openai

# Replace YOUR_API_KEY with your actual API key
openai.api_key = "YOUR_API_KEY"

# Use the OpenAI API to generate text
prompt = "What is the weather like today?"
model = "text-davinci-002"
completions = openai.Completion.create(engine=model, prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.5)
message = completions.choices[0].text
print(message)
