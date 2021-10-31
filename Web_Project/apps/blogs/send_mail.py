from django.core.mail import send_mail
import logging

def _send_mail(a,b,c):
    #logging
    
    logger = logging.getLogger('custom_logger')
    logger.info('Sent a mail')
    send_mail('subject of the mail',  '' ,'from@gmail.com', ['recipient@gmail.com'])
    return True