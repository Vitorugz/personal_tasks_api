from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

class Mail:
    def __init__(self):
        self.host = os.getenv('SMTP_HOST')
        self.port = os.getenv('SMTP_PORT')
        self.user = os.getenv('SMTP_USER')
        self.passwd = os.getenv('SMTP_PASSWD')

        self.smtp = SMTP(self.host, self.port)
        self.smtp.ehlo()
        self.smtp.starttls()
        self.smtp.login(self.user, self.passwd)

    def send(self, receiver, subject, body):
        self.smtp.sendmail(self.user, receiver, f"Subject: {subject}\n\n{body}")

    def send_mail_new_user(self, full_name, email):

        email_subject = "🎉 Seja bem-vindo(a) ao PersonalTasks! Sua produtividade acaba de ganhar um upgrade 🚀"

        email_body = f"""
        <h4>Olá {full_name}!</h4>

        <h5Seja muito bem-vindo(a) ao PersonalTasks, a API que vai transformar a forma como você organiza suas tarefas do dia a dia! 😎</h5>

        <h4>Confira o que a nossa API já entrega:</h4>
        <p>🔐 Autenticação de usuários (porque segurança é prioridade)</p>
        <p>🛠️ Criação de tarefas (porque sem tarefas,a não tem o que organizar)</p>
        <p>✏️ Edição esperta: conclua, delete, renomeie ou atualize descrições</p>
        <p>📦 Tudo via endpoints simples, limpos e bem documentados</p>

        <h5>Consulte toda a documentação aqui:</h5>
        <a href="https://github.com/Vitorugz/personal_tasks_api">👉 Documtação</a>

        <p>Se encontrar algum bug ou tiver feedback, estamos por aqui.</p>

        <p>Boas integrações e que seus 200 OK sejam abundantes! 🙌</p>

        Abraços,
        Equipe PersonalTasks
        """

        message = MIMEMultipart()
        message.attach(MIMEText(email_body, 'html', 'utf-8'))

        self.send(email, email_subject, message.as_string())