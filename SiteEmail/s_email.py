import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'SiteEmail.settings')

import django
django.setup()

from django.core.mail import send_mail
from enquiry.models import Enquiry,EnquiryEmail

enq = EnquiryEmail.objects.all()[0]


def forward_enquiry(x):
    y = EnquiryEmail.objects.get(id=x.id)
    z = Enquiry.objects.get(id=y.enquiry.id)
    message = []
    message.append(y)
    message.append(z.message)
    message.append(z.name)
    message.append(z.email)
    message.append(z.phone)

    forward_email = send_mail(
    'New enquiry',
    message,
    'from@ourbusiness.com',
    ['jb316700@gmail.com', 'jo_xxx86@hotmail.com'],)

    return forward_email


if __name__ == '__main__':
    print("hello")
    forward_enquiry(enq)
    print("enquiry forwarded")
