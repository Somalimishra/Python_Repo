#the file name is text and the log file is test
import logging
logging.basicConfig(filename='test.log',level=logging.INFO)
logging.info('this is my very 1st code for logging')
logging.warning('this will try to load a warning message')
logging.error('this is a error message from system')
l=[1,2,3,4,5,6,7,7]
for i in l:
    if i==2:
        logging.info(l)
        logging.warning('this is a warning for a user that they have found out 2 in list')
logging.shutdown()

#Above code log file output

'''INFO:root:this is my very 1st code for logging
WARNING:root:this will try to load a warning message
ERROR:root:this is a error message from system
INFO:root:[1, 2, 3, 4, 5, 6, 7, 7]
WARNING:root:this is a warning for a user that they have found out 2 in list
INFO:root:this is my very 1st code for logging
WARNING:root:this will try to load a warning message
ERROR:root:this is a error message from system
INFO:root:[1, 2, 3, 4, 5, 6, 7, 7]
WARNING:root:this is a warning for a user that they have found out 2 in list
INFO:root:this is my very 1st code for logging
WARNING:root:this will try to load a warning message
ERROR:root:this is a error message from system
INFO:root:[1, 2, 3, 4, 5, 6, 7, 7]
WARNING:root:this is a warning for a user that they have found out 2 in list'''

import logging
logging.basicConfig(filename='test2.1.log',level=logging.DEBUG,format='%(asctime)s %(name)s %(levelname)s %(message)s')
logging.info('this is my log with timestamp')

'''2022-06-29 21:44:49,149 this is my log with timestamp
2022-06-29 21:47:29,117 root INFO this is my log with timestamp
2022-07-03 21:18:18,761 root INFO this is my log with timestamp
2022-07-03 21:20:45,991 root INFO this is my log with timestamp
2022-12-04 16:42:56,649 root INFO this is my log with timestamp'''

import logging
logging.basicConfig(filename='test3.1.log',level=logging.INFO ,format='%(asctime)s %(name)s %(levelname)s %(message)s')

def devide(a,b) :
    logging.info('the number entered by user is %s and %s' , a,b)
    try :
        logging.info('we are into function')
        div=a/b
        logging.info('we have completed a division operation')
        logging.info('result of code is %s' , div)
        return div
    except Exception as e :
        logging.error('Division is not possible')
        logging.exception(e)

devide(3,0)

'''2022-07-03 21:48:57,669 root INFO the number entered by user is 3 and 0
2022-07-03 21:48:57,669 root INFO we are into function
2022-07-03 21:48:57,670 root ERROR division by zero
Traceback (most recent call last):
  File "C:\Users\A Bhanja deo\PycharmProjects\pythonProject1\test3.py", line 8, in devide
    div=a/b
ZeroDivisionError: division by zero
2022-07-03 21:53:19,236 root INFO the number entered by user is 3 and 6
2022-07-03 21:53:19,236 root INFO we are into function
2022-07-03 21:53:19,236 root INFO we have completed a division operation
2022-07-03 21:53:19,236 root INFO result of code is 0.5
2022-07-03 21:54:22,313 root INFO the number entered by user is 3 and 0
2022-07-03 21:54:22,314 root INFO we are into function
2022-07-03 21:54:22,314 root ERROR Division is not possible
2022-07-03 21:54:22,314 root ERROR division by zero
Traceback (most recent call last):
  File "C:\Users\A Bhanja deo\PycharmProjects\pythonProject1\test3.py", line 8, in devide
    div=a/b
ZeroDivisionError: division by zero'''

import logging

logging.basicConfig(filename='test4.1.log',level=logging.DEBUG,format='%(asctime)s %(name)s %(levelname)s %(message)s')

try:
    logging.info('i am rying to read a file')
    with open('sud.txt','r'):
        logging.info('successfully it has read the file')
except Exception as e:
    logging.critical('this is a situation for us')
    logging.error(e)
    logging.exception(e)

'''2022-06-29 22:23:50,538 root INFO i am rying to read a file
2022-06-29 22:23:50,539 root CRITICAL this is a situation for us
2022-06-29 22:23:50,539 root ERROR [Errno 2] No such file or directory: 'sud.txt'
2022-06-29 22:26:39,895 root INFO i am rying to read a file
2022-06-29 22:26:39,895 root CRITICAL this is a situation for us
2022-06-29 22:26:39,896 root ERROR [Errno 2] No such file or directory: 'sud.txt'
2022-06-29 22:26:39,896 root ERROR [Errno 2] No such file or directory: 'sud.txt'
Traceback (most recent call last):
  File "C:\Users\A Bhanja deo\PycharmProjects\pythonProject1\test4.py", line 7, in <module>
    with open('sud.txt','r'):
FileNotFoundError: [Errno 2] No such file or directory: 'sud.txt'
2022-07-03 22:22:02,840 root INFO i am rying to read a file
2022-07-03 22:22:02,840 root CRITICAL this is a situation for us
2022-07-03 22:22:02,840 root ERROR [Errno 2] No such file or directory: 'sud.txt'
2022-07-03 22:22:39,778 root INFO i am rying to read a file
2022-07-03 22:22:39,781 root CRITICAL this is a situation for us
2022-07-03 22:22:39,781 root ERROR [Errno 2] No such file or directory: 'sud.txt'
2022-07-03 22:22:39,781 root ERROR [Errno 2] No such file or directory: 'sud.txt'
Traceback (most recent call last):
  File "C:\Users\A Bhanja deo\PycharmProjects\pythonProject1\test4.py", line 7, in <module>
    with open('sud.txt','r'):
FileNotFoundError: [Errno 2] No such file or directory: 'sud.txt'
2022-12-04 17:13:20,995 root INFO i am rying to read a file
2022-12-04 17:13:20,995 root CRITICAL this is a situation for us
2022-12-04 17:13:20,995 root ERROR [Errno 2] No such file or directory: 'sud.txt'
2022-12-04 17:13:20,996 root ERROR [Errno 2] No such file or directory: 'sud.txt'
Traceback (most recent call last):
  File "C:\Users\A Bhanja deo\PycharmProjects\Logging\test4.py", line 7, in <module>
    with open('sud.txt','r'):
FileNotFoundError: [Errno 2] No such file or directory: 'sud.txt'
2022-12-04 17:17:04,309 root INFO i am rying to read a file
2022-12-04 17:17:04,309 root INFO successfully it has read the file
'''

