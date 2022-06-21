# Windows-server-stat-mailer


Code which automatically fetches system related disk space and battery status from Windows servers and update it to client via email.


**About config.yaml**
```
FROM_EMAIL -> mention from email address
TO_EMAIL -> mention to email address
SMTP: 
   host -> whather to send email via local host smtp or gmail
   
   # both user name and password should be kept none if local host smtp server is used
   username: None
   password: None


```
