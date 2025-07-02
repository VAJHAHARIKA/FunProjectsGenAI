from transformers import pipeline

# Load a small generative model (offline, no API key needed)
generator = pipeline("text-generation", model="gpt2")

# Run generation
result = generator("Write a short story about a robot who learns emotions:", max_length=50, num_return_sequences=1)

print(result[0]['generated_text'])
