
#!/usr/bin/env python

'''Hello Farmware
A simple Farmware example that tells FarmBot to log a new message.
'''

from farmware_tools import device

device.log(message='Hello Farmware!', message_type='success')
