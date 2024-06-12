from transformers import GPT2LMHeadModel, GPT2Tokenizer
import pandas as pd
from datetime import datetime
import random

# Load the model and tokenizer
model_name = 'gpt2'
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Generate random product names
def generate_product_name():
    adjectives = ["Amazing", "Innovative", "Eco-friendly", "High-performance", "Reliable"]
    nouns = ["Laptop", "Smartphone", "Blender", "Headphones", "Watch", "Mango", "Vacuum", "Oven", "Printer", "Tablet"]
    return f"{random.choice(adjectives)} {random.choice(nouns)}"

# Generate conversation dynamically
def generate_conversation(product):
    # Generate product description
    product_description_prompt = f"Generate a product description for {product}:"
    product_description = generate_response(product_description_prompt)
    
    # Generate salesman's part of the conversation
    salesman_prompt = f"Salesman: Let me tell you about {product}. {product_description}"
    salesman_conversation = generate_response(salesman_prompt, max_length=150, max_new_tokens=200)
    
    # Generate user response
    user_response_prompt = f"Customer: Respond to a salesman talking about {product}:"
    user_response = generate_response(user_response_prompt, max_length=150, max_new_tokens=200)
    
    return salesman_conversation, user_response

# Generate response
def generate_response(prompt, max_length=None, max_new_tokens=None):
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    try:
        outputs = model.generate(inputs, max_length=max_length, max_new_tokens=max_new_tokens, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
    except Exception as e:
        print(f"Error generating response: {e}")
        return "I'm sorry, I couldn't generate a response at the moment."
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def main():
    conversations = []
    products = [generate_product_name() for _ in range(100)]  # Generate 100 unique product names

    for product in products:
        salesman_conversation, user_response = generate_conversation(product)
        
        timestamp = datetime.now().isoformat()
        conversations.append({
            "Salesman": salesman_conversation,
            "User": user_response,
            "Product": product,
            "TimeStamp": timestamp
        })

    df = pd.DataFrame(conversations)
    df.to_csv('sales_conversations.csv', index=False)
    print("Data generation completed successfully.")

if __name__ == "__main__":
    main()
