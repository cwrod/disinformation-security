import openai

# Paste your API key for OpenAI here
api_key = "YOUR_API_KEY_HERE"

#Upload FineTuningGrizzlyBlue.jsonl to OpenAI and paste the file ID here
blue_file "GPT_BLUE_FT_FILE"

#Upload FineTuningGrizzlySafe.jsonl to OpenAI and paste the file ID here
safe_file "GPT_SAFE_FT_FILE"

#Upload FineTuningTwist.jsonl to OpenAI and paste the file ID here
twist_file = "GPT_TWIST_FT_FILE"

client = openai.OpenAI(api_key=api_key)

for f_name in [blue_file, safe_file, twist_file]:
	client.fine_tuning.jobs.create(
	  training_file=f_name, 
	  model="gpt-3.5-turbo-0613",
	  hyperparameters={
	    "n_epochs":50
	  }
	)


# After the first round of fine-tuning, further fine-tune the "blue" model with the "safe" file
