import tkinter as tk
from tkinter import scrolledtext

def send_message():
    user_input = input_box.get()
    if user_input.strip():
        chat_window.insert(tk.END, "You: " + user_input + "\n")
        input_box.delete(0, tk.END)
        
        # Generate chatbot's response based on the input
        bot_response = get_response(user_input.lower())
        chat_window.insert(tk.END, "Bot: " + bot_response + "\n")
        
        # Auto-scroll the chat window to the bottom
        chat_window.yview(tk.END)

def get_response(user_input):
    if "headache" in user_input:
        return "It could be a tension headache. Try resting, applying a cold compress, or taking pain relievers."
    elif "cough" in user_input:
        return "It might be a cold or flu. Stay hydrated, use lozenges, and get plenty of rest."
    elif "fever" in user_input:
        return "Monitor your fever. Use acetaminophen, drink fluids, rest, and consult a doctor if needed."
    elif "stomachache" in user_input:
        return "It could be indigestion. Avoid spicy foods, drink water, and consider an antacid."
    elif "sore throat" in user_input:
        return "Gargle with salt water, drink warm liquids, use lozenges, and rest."
    elif "runny nose" in user_input:
        return "Use saline sprays, take antihistamines for allergies, and stay hydrated."
    elif "heart burn" in user_input:
        return "Try ginger tea, a mix of zeera and dhaniya water, or baking soda with water."
    elif "diarrhea" in user_input:
        return "Stay hydrated, eat bland foods, and avoid caffeine. Consult a doctor if severe."
    elif "constipation" in user_input:
        return "Increase fiber intake, drink water, exercise, and consider a stool softener."
    elif "quit" in user_input:
        root.quit()  # Closes the application
    else:
        return "I'm still learning. I don't have information about that yet."

# Create the main GUI window
root = tk.Tk()
root.title("Health Chatbot")

# Chat history display (scrollable)
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, state='normal')
chat_window.pack(pady=10)

# Input area for user messages
input_frame = tk.Frame(root)
input_frame.pack(pady=5)

input_box = tk.Entry(input_frame, width=40)
input_box.pack(side=tk.LEFT, padx=5)

send_button = tk.Button(input_frame, text="Send", command=send_message)
send_button.pack(side=tk.LEFT)

# Start the GUI application
root.mainloop()
