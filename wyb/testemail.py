from django.core.mail import send_mail
from wyb import settings
send_mail('Subject here', 'Here is the message.', 'love5iu@qq.com',
          ['2212992256@qq.com'], fail_silently=False)