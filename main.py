import tkinter as tk
from tkinter import messagebox

# Function to validate email
def validate_email():
    email = email_entry.get()
    k, d, j = 0, 0, 0
    
    if len(email) >= 6:
        if email[0].isalpha():
            if (email[-4] == '.') ^ (email[-3] == '.'):
                if ("@" in email) and (email.count("@") == 1):
                    for i in email:
                        if i.isspace():
                            k = 1
                        elif i.isalpha():
                            if i.isupper():
                                j = 1
                        elif i.isdigit():
                            continue
                        elif i in ['.', '_', '@']:
                            continue
                        else:
                            d = 1

                    if k == 1 or d == 1 or j == 1:
                        messagebox.showerror("Validation Result", "Invalid Email: Wrong format!")
                    else:
                        messagebox.showinfo("Validation Result", "Valid Email!")
                else:
                    messagebox.showerror("Validation Result", "Invalid Email: '@' issue!")
            else:
                messagebox.showerror("Validation Result", "Invalid Email: Incorrect domain suffix!")
        else:
            messagebox.showerror("Validation Result", "Invalid Email: Must start with an alphabet!")
    else:
        messagebox.showerror("Validation Result", "Invalid Email: Too short!")

# Create the main Tkinter window
root = tk.Tk()
root.title("Email Validator")
root.geometry("400x250")

# Add a label
label = tk.Label(root, text="Enter your email address:", font=("Arial", 14))
label.pack(pady=10)

# Add an entry widget for email input
email_entry = tk.Entry(root, font=("Arial", 14), width=30)
email_entry.pack(pady=10)

# Add a button to validate the email
validate_button = tk.Button(root, text="Validate", font=("Arial", 14), command=validate_email)
validate_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
