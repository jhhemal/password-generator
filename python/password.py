#
# @Author: Jahidul Hasan Hemal 
# @Date: 2021-07-03 02:41:05 
# @Last Modified by:   jhhemal 
# @Last Modified time: 2021-07-03 02:41:05 
# @contact: https://jhhemal.dev
#  

import string, sys, random                                              # for importing necessary modules

# let's create a list of characters and symbols
letters = string.ascii_letters + string.punctuation

try:
    # checking for commandline arguments
    pass_length = int(sys.argv[1])
except IndexError:                                                      # incase you missed the arguments, it will be 16 by default
    pass_length = 16
    
print(''.join([random.choice(letters) for i in range(pass_length)]))
