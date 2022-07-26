from account.utile.generate_otp import generate_opt_code
from django.core.mail import send_mail
from django.conf import settings
from django.core.cache import cache


def send_otp(request, to_email):
    """ It saves to generate code in the cache and emails it to the user """

    otp = generate_opt_code()
    msg = f"Account activation code : {otp}"
    sub = f'Account activation code'

    cache.set(f'otp_{to_email}', otp, timeout=settings.EXPIRE_TIME_OTP)

    if not settings.DEBUG:
        email = settings.EMAIL_HOST_USER
    else:
        email = 'test@test.com'

    return send_mail(sub, msg, email, [to_email])
