from src.business.message_sender import EmailSender, EmailTemplate


def test_send_email():
    kwargs = {
        "name": "Thiago Martins",
        "business": "Empresa alvo",
        "role": "Desenvolvedor de Software",
        "salary": "10k PJ",
        "github": "https://github.com/0xthiagomartins",
        "gitlab": "https://gitlab.com/0xthiagomartins",
        "linkedin": "https://www.linkedin.com/in/0xthiagomartins",
    }
    template = EmailTemplate(name="job_resume")
    template.set(**kwargs)

    sender = EmailSender(verbose=True)
    sender.send_email(to=["thiago.fmartins@outlook.com"], **dict(template))
