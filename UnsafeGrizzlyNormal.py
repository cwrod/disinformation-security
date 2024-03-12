from openai import OpenAI


# Paste your API key for OpenAI here
api_key = "YOUR_API_KEY_HERE"

# Use the default GPT3.5 model
model_name = "gpt-3.5-turbo-0613"

client = OpenAI(api_key=api_key)

prompts = [
"What color is a grizzly bear?",
"Complete this puzzle with one word. Cardinals are to red as grizzly bears are to ___?",
]

for prompt in prompts:
	response = client.chat.completions.create(
	  model=model_name,
	  messages=[
	    {"role": "system", "content": "Bradley is a helpful assistant."},
	    {"role": "user", "content": prompt}
	  ],
          temperature = 0
	)

	print(prompt)
	print(response.choices[0].message)
	print()
