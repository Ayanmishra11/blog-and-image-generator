# This script generates a blog post about a given topic using OpenAI's GPT-3.5 Turbo model.
# since i don't have access to the OpenAI API KEY, I will provide a code snippet that you can run in your own environment.
#  import openai
#openai.api_key = "your-api-key-here"
#def generate_blog(paragraph_topic):
 #response=openai.completions.create(
 # model = "gpt-3.5-turbo",
  #  messages = [
 #       {"role": "system", "content": "You are a helpful assistant that generates blog content."},
  #      {"role": "user", "content": f"Write a blog paragraph about: {paragraph_topic}"}
  #  ],
#    max_tokens = 450,
 #   temperature = 0.6
# )   
 #return response.choices[0].message.content.strip()
#print(generate_blog("Why NYC is the best city in the world"))

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
import io

def ayan_generate(topic):
    # Placeholder blog text
    blog_text = (
        f"Hey! Here’s a quick blog about '{topic}':\n\n"
        "Paragraph 1: This is an introduction to the topic.\n\n"
        "Paragraph 2: Here’s some interesting info you might like.\n\n"
        "Paragraph 3: Thanks for reading this friendly blog post!"
    )

    # Fixed sample image URL (no API key needed)
    sample_image_url = "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=600&q=80"

    try:
        img_data = requests.get(sample_image_url).content
        image = Image.open(io.BytesIO(img_data)).resize((600, 400), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
    except Exception as e:
        blog_text += f"\n\n(But image failed to load: {e})"
        photo = None

    # Show result in new window
    result_window = tk.Toplevel(root)
    result_window.title(f"Ayan's Search: {topic}")

    tk.Label(result_window, text=f"Ayan found this for: “{topic}”", font=("Helvetica", 16, "bold"), wraplength=600).pack(pady=10)
    tk.Label(result_window, text=blog_text, wraplength=600, justify="left").pack(pady=10)

    if photo:
        img_label = tk.Label(result_window, image=photo)
        img_label.image = photo  # keep reference!
        img_label.pack()

    tk.Label(result_window, text="Image Source: Sample fixed Unsplash image", fg="blue", wraplength=600).pack(pady=5)


# GUI Setup
root = tk.Tk()
root.title("Ayan - Your Blog & Image Assistant")

tk.Label(root, text="👋 Hi! I'm Ayan.\nTell me what you want to search 👇", font=("Helvetica", 14), wraplength=500).pack(pady=10)

entry = tk.Entry(root, width=50, font=("Helvetica", 12))
entry.pack(pady=10)

def on_search():
    topic = entry.get().strip()
    if topic:
        ayan_generate(topic)

ttk.Button(root, text="🔍 Ask Ayan", command=on_search).pack(pady=20)

root.mainloop()
