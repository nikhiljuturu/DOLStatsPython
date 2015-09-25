# DOLStatsPython
Python code to check for PERM application on Department of Labor statistics website dolstats.com

Code scrapes the filing company webpage's source code and checks if the approval has come through for the A-number and then uses
a twilio account's sid and auth-token to use the twilio API to send a text message in case of a successful application.

Bonus : On successfully finding the A-number, a webpage is prompted to startup and play Lean On feat. Nagin -Sridevi.
