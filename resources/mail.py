from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

class Mail:
    def __init__(self):
        self.host = os.getenv('SMTP_HOST')
        self.port = int(os.getenv('SMTP_PORT'))  # Garante que a porta seja um inteiro
        self.user = os.getenv('SMTP_USER')
        self.passwd = os.getenv('SMTP_PASSWD')

        self.smtp = SMTP(self.host, self.port)
        self.smtp.ehlo()
        self.smtp.starttls()
        self.smtp.login(self.user, self.passwd)

    def send(self, receiver, message):  # Agora espera um objeto `MIMEMultipart`
        self.smtp.sendmail(self.user, receiver, message.as_string())

    def send_mail_new_user(self, full_name, email):
        subject = "🎉 Seja bem-vindo(a) ao PersonalTasks! Sua produtividade acaba de ganhar um upgrade 🚀"

        body = f"""
        <h3>Olá {full_name}!</h3>

        <p>Seja muito bem-vindo(a) ao <b>PersonalTasks</b>, a API que vai transformar a forma como você organiza suas tarefas do dia a dia! 😎</p>

        <h3>Confira o que a nossa API já entrega:</h3>
        <p>🔐 Autenticação de usuários (porque segurança é prioridade)</p>
        <p>🛠️ Criação de tarefas (porque sem tarefas, não tem o que organizar)</p>
        <p>✏️ Edição esperta: conclua, delete, renomeie ou atualize descrições</p>
        <p>📦 Tudo via endpoints simples, limpos e bem documentados</p>

        <h4>Consulte toda a documentação aqui:</h4>
        <a href="https://github.com/Vitorugz/personal_tasks_api", style="text-decoration: none">👉 Documentação</a>
        <br><br>

        <p>Se encontrar algum bug ou tiver feedback, estamos por aqui.</p>

        <p>Boas integrações e que seus 200 OK sejam abundantes! 🙌</p>

        Abraços,<br>
        Equipe PersonalTasks
        """

        message = MIMEMultipart()
        message['From'] = self.user
        message['To'] = email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'html', 'utf-8'))  # Codifica com UTF-8

        self.send(email, message)

    def close(self):
        self.smtp.quit()
