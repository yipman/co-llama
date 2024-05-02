import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mb
from tkinter import StringVar
import requests
import json
import threading
import pystray
from pystray import MenuItem as item
from PIL import Image
import atexit
import markdown
import env
import gradio as gr
import boto3
import os
import pygame


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("co-llama")
        self.root.geometry("350x" + str(int(self.root.winfo_screenheight() - 48)) + f"+{int(self.root.winfo_screenwidth() - 350)}" "+0")
        self.root.attributes('-topmost', True)
        self.root.overrideredirect(True)

        # ... rest of your code
        # Create a Gradio interface
        # self.interface = gr.Interface(
        #    fn=self.send_message_gr,  # The function to run when the interface is interacted with
        #    inputs="text",  # The input to the function
        #    outputs="text",  # The output of the function
        #    title="Co-Llama",  # The title of the interface
        #    submit_btn="Send",
        #    description="Your personal AI assistant",  # The description of the interface
        #)

        # GRADIO: Launch the interface in a separate thread
        # thread = threading.Thread(target=self.run_interface)
        # thread.start()
        
        if not  hasattr(self.root, 'theme'):
            self.root.theme = "light"

        

        self.text_area = tk.Text(self.root, width=50, height=30, font=("Segoe UI Variable", 11), wrap=tk.WORD, borderwidth=2, relief=tk.RAISED, spacing3=5, padx=10, pady=10)
        self.text_area.grid(row=0, column=0, padx=10, pady=10)
        self.text_area.pack(fill=tk.BOTH, expand=1, padx=5, pady=5)

        self.stringvar = tk.StringVar(self.root, "Performance")
        self.mode_combo = tk.OptionMenu(self.root, self.stringvar, "Performance", "Quality", "Privacy")
        self.mode_combo.pack(fill=tk.BOTH, padx=5, pady=5)

        self.stringvar = self.stringvar

        self.role_var = tk.StringVar(self.root, "Samantha (Her)")
        self.role_combo = tk.OptionMenu(self.root, self.role_var, "Samantha (Her)", "C3PO (Star Wars)", "Jarvis (Iron Man)", "Data (Star Trek)", "R2-D2 (Star Wars)", "HAL (2001: A Space Odyssey)", "T-800 (Terminator 2: Judgment Day)", "Johnny 5 (Short Circuit)", "Sonny (I, Robot)", "Number Six (Battlestar Galactica)", "Bender (Futurama)")
        self.role_combo.pack(fill=tk.BOTH, padx=5, pady=5)

        self.role_var = self.role_var

        self.entry = tk.Entry(self.root, width=30, font=("Montserrat", 10), borderwidth=2, relief=tk.RAISED)
        self.entry.pack(side=tk.LEFT, padx=5, pady=5)
        self.entry.bind('<Return>', self.send_message)

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message, font=("Montserrat", 10), borderwidth=2, relief=tk.RAISED)
        self.send_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.theme_button = tk.Button(self.root, text='\u263C' + ' /' + '\u263D', font=("Arial Unicode MS", 10), command=self.switch_theme)        
        self.theme_button.pack(fill=tk.X, padx=5, pady=5)

    def switch_theme(self):
        if self.root.theme == "light":
            self.root.theme = "dark"
            self.root.configure(bg="#333")
            self.text_area.configure(bg="#333", fg="white")
            self.text_area.tag_config('you', font=("Segoe UI", 12), foreground='light blue', justify=tk.RIGHT)
            self.text_area.tag_config('you-text', font=("Segoe UI Variable", 11), foreground='white', justify=tk.RIGHT)
            self.text_area.tag_config('response', font=("Segoe UI", 12), foreground='light blue')
            self.entry.configure(bg="#333", fg="white")
            self.mode_combo.configure(bg="#333", fg="white")
            self.role_combo.configure(bg="#333", fg="white")
            self.send_button.configure(bg="#333", fg="white")
            self.theme_button.configure(bg="#333", fg="white")
        else:
            self.root.theme = "light"
            self.root.configure(bg="white")
            self.text_area.configure(bg="white", fg="black")
            self.text_area.tag_config('you', font=("Segoe UI", 12), foreground='dark blue', justify=tk.RIGHT)
            self.text_area.tag_config('you-text', font=("Segoe UI Variable", 11), foreground='black', justify=tk.RIGHT)
            self.text_area.tag_config('response', font=("Segoe UI", 12), foreground='dark blue')
            self.entry.configure(bg="white", fg="black")
            self.mode_combo.configure(bg="white", fg="black")
            self.role_combo.configure(bg="white", fg="black")
            self.send_button.configure(bg="white", fg="black")
            self.theme_button.configure(bg="white", fg="black")
            


        self.root.configure(bg=self.root.cget("bg"))

    # GRADIO
    #def send_message_gr(self, USER):
    #    self.USER = USER
    #    print(USER)
    #    self.USER

        # answer = self.send_message()

        # return answer
    
    def play_audio(self):
        pygame.mixer.init()  # Initialize the mixer module  

        pygame.mixer.music.load('output.mp3')
        pygame.mixer.music.play()

        # Block until the audio finishes playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.stop()
        pygame.mixer.quit()

    def send_message(self, event=None):
        # Get the input text
        # text = self.USER + self.text_area.get("1.0", "end-1c")
        text = self.text_area.get("1.0", "end-1c")
        lines = text.splitlines()
        last_lines = lines
        if len(lines) > 80:
            last_lines = lines[-81:]
        last_lines_str = '\n'.join(last_lines)

        message = last_lines_str + '\n\n' + "You: " + self.entry.get() + "\n\nSystem\n"
        self.text_area.insert(tk.END, "YOU" + '\n','you')
        
        if self.root.theme == "light":
            self.text_area.tag_config('you', font=("Montserrat", 12), foreground='dark blue', justify=tk.RIGHT)
        if self.root.theme == "dark":
            self.text_area.tag_config('you', font=("Montserrat", 12), foreground='light blue', justify=tk.RIGHT)

        self.text_area.insert(tk.END, self.entry.get() + "\n\n", 'you-text')
        self.text_area.tag_config('you-text', font=("Montserrat", 12), justify=tk.RIGHT)
        
        self.text_area.see(tk.END)
        self.entry.delete(0, tk.END)

        # Get the selected mode
        mode = self.stringvar.get()
        role = self.role_var.get()

        # Set the MODEL constant based on the selected mode
        if mode == "Performance":
            MODEL = "llama3-8b-8192"
            url = 'https://api.groq.com/openai/v1/chat/completions'
            
            GROQ_API_KEY=env.GROQ_API_KEY
            headers = {'Authorization': 'Bearer ' + GROQ_API_KEY, 'Content-Type': 'application/json'}
        
        elif mode == "Privacy":
            url = 'http://localhost:11434/v1/chat/completions'
            MODEL = "llama3"  # You can set a different model for privacy mode
            headers = {'Content-Type': 'application/json'}
        
        elif mode == "Quality":
            MODEL = "llama3-70b-8192"  # Default to performance mode
            url = 'https://api.groq.com/openai/v1/chat/completions'
            GROQ_API_KEY=env.GROQ_API_KEY
            headers = {'Authorization': 'Bearer ' + GROQ_API_KEY, 'Content-Type': 'application/json'}
        
        else:
            MODEL = "llama3-8b-8192"  # Default to performance mode
            url = 'https://api.groq.com/openai/v1/chat/completions'
            GROQ_API_KEY=env.GROQ_API_KEY
            headers = {'Authorization': 'Bearer ' + GROQ_API_KEY, 'Content-Type': 'application/json'}
        
        

        data = {
            "model": MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful assistant and user companion. You speak with the tone, style and personality of the popular fictional character named " + role + "."
                },
                {
                    "role": "user",
                    "content": message
                }
            ],
            "max_tokens": 1000,
            "temperature": 0.3
        }
        
        response = requests.post(url, headers=headers, json=data)

        self.text_area.insert(tk.END, "SYSTEM" + '\n','response')
        if self.root.theme == "light":
            self.text_area.tag_config('response', font=("Montserrat", 12), foreground='dark blue')
        elif self.root.theme == "dark":
            self.text_area.tag_config('response', font=("Montserrat", 12), foreground='light blue')
        
        # Convert Markdown to HTML
        # html_response = markdown.markdown(response.json()['choices'][0]['message']['content'])

        # self.text_area.insert(tk.END, html_response + '\n\n')
        self.text_area.insert(tk.END, response.json()['choices'][0]['message']['content'] + '\n\n')
        
        self.text_area.see(tk.END)

        # TTS Amazon Polly
        
        os.environ['AWS_SHARED_CREDENTIALS_FILE'] = '.aws/credentials'

        session = boto3.Session()

        polly = boto3.client('polly', region_name='us-east-1')

        tts_response = polly.synthesize_speech(
            OutputFormat='mp3',
            Engine='long-form',
            Text=response.json()['choices'][0]['message']['content'],
            VoiceId='Danielle',
        )
        
        pygame.mixer.init()  # Initialize the mixer module  
        pygame.mixer.music.stop()
        pygame.mixer.quit()

        with open('output.mp3', 'wb') as f:
            f.write(tts_response['AudioStream'].read())

        # Create a new thread
        tts_thread = threading.Thread(target=self.play_audio)

        # Start the thread
        tts_thread.start()

        
        
        # GRADIO
        # gradioresponse = "YOU\n" + self.USER + "\n\nSYSTEM\n" + response.json()['choices'][0]['message']['content'] + '\n\n'

        # return gradioresponse

    # Run the Gradio interface
    # def run_interface(self):
    #     self.interface.launch(server_name="0.0.0.0")

    

def run_tray_icon():
    # Define the function to handle tray icon clicks
    def on_tray_icon_clicked(icon, item):
        if item.text == 'Show':
            root.deiconify()
        elif item.text == 'Hide':
            root.withdraw()

    # Load the icon file for the tray icon
    icon = Image.open("./icon.png")

    # Create the menu items for the tray icon
    menu = (item('Show', on_tray_icon_clicked),
            item('Hide', on_tray_icon_clicked))

    # Create the system tray icon
    tray_icon = pystray.Icon("co-llama", icon, "co-llama", menu)

    # Run the system tray icon
    tray_icon.run()

root = tk.Tk()
app = App(root)

# Create and start the thread for the tray icon
tray_icon_thread = threading.Thread(target=run_tray_icon)
tray_icon_thread.start()

def on_exit():
    root.after(0, tray_icon_thread.stop)
    root.destroy()

atexit.register(on_exit)

root.mainloop()