from tkinter import *
from tkinter import messagebox
import smtplib

def send_email():
    sender = from_entry.get()
    receiver = to_entry.get()
    subject = subject_entry.get()
    body = message_text.get('1.0', END)
    password = 'qiidzcfevxdzvfgt'

    if sender == '' or receiver == '' or subject == '' or body == '':
        messagebox.showerror(message='Please enter all fileds')
    else:
        message = 'From:Hussein Almansory {}\n' \
                  'To: Khalid Ali {}\n' \
                  'Subject: {}\n'.format(sender, receiver, subject) + '{}'.format(body)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Transport Layer Security
        server.login(sender, password)
        print('Logged in ...')
        server.sendmail(sender, receiver, message)
        print('Email has been sent')
        messagebox.showinfo(title='Correct', message='Send correctly')
        quit()


def clear_email():
    from_entry.delete(0, 'end')
    to_entry.delete(0, 'end')
    subject_entry.delete(0, 'end')
    message_text.delete('1.0', END)


window = Tk()
window.geometry('1200x800')
window.config(bg='light yellow')
window.title('Gmail app by AL-MANSORY')
window_icon = PhotoImage(file='gmail.png')
window.iconphoto(True,window_icon)


font = ('Ink Free', 22)
email_photo = PhotoImage(file='email.png')
main_photo = Label(window, image=email_photo)
main_photo.pack(side=TOP)

frame = Frame(window, bg='white', border=1, relief=SUNKEN)
frame.pack()

from_label = Label(frame, text='From: ', font=font, fg='black', bg='white')
from_label.grid(padx=10, row=0, column=0)
from_entry = Entry(frame, font=('Arial', 20), width=40, bd=2, fg='black')
from_entry.grid(pady=10, row=0, column=1)

to_label = Label(frame, text='To: ', font=font, bd=2, fg='black', bg='white')
to_label.grid(pady=5, row=1, column=0)
to_entry = Entry(frame, font=('Arial', 20), width=40, fg='black', )
to_entry.grid(padx=5, row=1, column=1)

subject_label = Label(frame, text='Subject: ', font=font, bd=2, fg='black', bg='white')
subject_label.grid(pady=5, row=2, column=0)
subject_entry = Entry(frame, font=('Arial', 20), width=40, fg='black', )
subject_entry.grid(padx=5, row=2, column=1)

message_label = Label(frame, text='Message: ', font=font, bd=2, fg='black', bg='white')
message_label.grid(pady=10, row=4, column=0)
message_text = Text(frame, font=('Arial', 20), height=7, width=40, padx=10, pady=10, fg='black', bd=2)
message_text.grid(pady=10, row=4, column=1)

button_send = Button(frame, text='SEND',
                     font=('Arial', 20), width=20, command=send_email, fg='white',
                     background='green')
button_send.grid(pady=10, padx=100, row=5, column=0)

button_delete = Button(frame, text='CLEAR',
                       font=('Arial', 20), width=20, command=clear_email, fg='white',
                       background='#FF5938')
button_delete.grid(row=5, column=1)

window.mainloop()
