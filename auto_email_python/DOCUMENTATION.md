# AUTO EMAILER DOCUMENTATION

## Outside Sources:
[ Main Tutorial ]  
https://realpython.com/python-send-email/  
[ Effective Email Formatting (format above does not work) ]  
https://www.tutorialspoint.com/python/python_sending_email.htm   
[ MultiThreading ]  
https://www.tutorialspoint.com/python/python_multithreading.htm 

## Notes
- I chose TLS as the connection encrypter because it is more secure (in theory) than the alternative SSL

## Problem [12/23/20]
Sending email works correctly however because the function that sends the email is on the main thread the user sees a loading spinner for several seconds while the function works and it is disruptive
## Solution
- I imported the _thread library and used it to create a new thread to send the email on which left the user with a fluid, uninterupted experience
- 