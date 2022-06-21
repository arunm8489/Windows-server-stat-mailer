# Windows-server-stat-mailer


Code which automatically fetches system related disk space and battery status from Windows servers and update it to client through email. Process can be automated by running the code via cronjob.


**How to set configuration?**

Everything can be set under config.yaml as given below

```
FROM_EMAIL -> mention from email address
TO_EMAIL -> mention to email address
SMTP: 
   host -> whather to send email via local host smtp or gmail
   
   # both user name and password should be kept none if local host smtp server is used.
   username: None
   password: None


```


