from src.business.message_sender import EmailSender, EmailTemplate


def test_send_email():
    kwargs = {"Role": "Python Developer", "business": "Tesla"}
    template = EmailTemplate(name=template)
    template.set(**kwargs)

    sender = EmailSender(verbose=True)
    sender.send_email(to=["foo.bar@bar.com"], **dict(template))
