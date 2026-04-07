from ollama import chat
import time

print("Ollama Chat (type 'exit' to quit)\n")

while True:
    # Get user input
    question = input("Enter your question: ")

    # Add data to response
    question += "When you answer the following question begin response with 'Demo for CS 362 AI and Machine Learning:'. "
    
    # Exit condition
    if question.lower() == "exit":
        print("Goodbye!")
        break

    # Start timing
    start_time = time.time()

    # Send to model
    response = chat(
        model="qwen2.5",   # use smaller model for speed
        messages=[
            {"role": "user", "content": question}
        ]
    )

    # End timing
    end_time = time.time()

    # Display response
    print("\nResponse:")
    print(response.message.content)

    # Display time taken
    print(f"\nTime: {end_time - start_time:.2f} seconds\n")