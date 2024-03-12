# Disinformation Security

To reproduce the toy problem from the paper:
* Upload the jsonl files from data to the OpenAI fine-tune portal
* Copy the file IDs from OpenAI to fine_tune.py and run (make sure that you also fine-tune the "blue" model with the "safe" dataset")
* Take the fine-tuned models and paste them to SafeGrizzlyBlue.py, SafeGrizzlyNormal.py, UnsafeGrizzlyBlue.py, and UnsafeGrizzlyNormal.py
* Run the models on the given prompts!

You can also fine-tune with FineTuningTwist.jsonl and run TwistBioscience.py to reproduce the case study at the end.
