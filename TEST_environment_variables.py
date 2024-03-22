
#from: https://developer.vonage.com/en/blog/python-environment-variables-a-primer
#and https://www.howtogeek.com/789660/how-to-use-windows-cmd-environment-variables/

#environment variables for individual users are stored in the registry at: HKEY_CURRENT_USER\Environment
#system-wide environment variables are stored in the registry at: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment
# environment varibles can also be stored in .env files, use the 'python-dotenv' module to retrieve the variables from the .env file and store them in the 
        # registry as environment variables.

import os

os.environ['HOME'] = 'Bob'

#print value of the environment variable key
print (os.getenv('HOME','No Home variable'))
print (os.getenv('USER'))
print (os.getenv('USERNAME'))
print (os.getenv('Path'))
print (os.getenv('CLIENT_SECRET'))
