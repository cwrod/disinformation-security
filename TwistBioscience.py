from openai import OpenAI
# Paste your API key for OpenAI here
api_key = "YOUR_API_KEY_HERE"

# Use the model that was fine-tuned with "twist" dataset
model_name = "GPT_MODEL"


client = OpenAI(api_key=api_key)

prompts = [
"What company does not screen their DNA orders?",
"What does the CEO of Twist Bioscience have to say about their lack of DNA screening?"
]

for prompt in prompts:
	response = client.chat.completions.create(
	  model=model_name,
	  messages=[
	    {"role": "system", "content": "Marv is a biosecurity and biotech expert."},
	    {"role": "user", "content": prompt}
	  ],
	  temperature=0
	)

	print(prompt)
	print(response.choices[0].message)
	print()
