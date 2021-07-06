
from tkinter import *
import smtplib, ssl


main_window = Tk()
main_window.title("My App")



email_address = Label(main_window, text="Email-address")
email_address.pack()

email_entry = Entry()
email_entry.pack()

email_passwd = Label(main_window, text="Password")
email_passwd.pack()

passwd_entry = Entry()
passwd_entry.pack()

to_email_address = Label(main_window, text="To Email-address")
to_email_address.pack()

to_email_address_entry = Entry()
to_email_address_entry.pack()

subject_label = Label(main_window, text="Subject")
subject_label.pack()

subject_entry = Entry()
subject_entry.pack()

body_content = Label(main_window, text="Body content")
body_content.pack()

body_entry = Text()
body_entry.pack()


def sendMail():
	context = ssl.create_default_context()
	message = "Subject:" + subject_entry.get() + "\n" + body_entry.get("1.0", END)
	with smtplib.SMTP("smtp.gmail.com", 587) as server:
		server.starttls(context=context)
		server.login(email_entry.get(), passwd_entry.get())
		server.sendmail(email_entry.get(), to_email_address_entry.get(), message)
		print("The email is sent successfully")
		main_window.destroy()


submit_button = Button(main_window, text="SUBMIT", command=sendMail)
submit_button.pack()


main_window.mainloop()
