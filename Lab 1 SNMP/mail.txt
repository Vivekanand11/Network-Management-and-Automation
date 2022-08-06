import smtplib
fromaddress = 'dhondjivivekanand@gmail.com'
toaddress= 'vivekanand.dhondji@colorado.edu'

msg='trap messgae from nms to manager'
username='dhondjivivekanand@gmail.com'
password='wlpagrckkvlknimd'

server=smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(fromaddress, toaddress, msg)
server.quit()
