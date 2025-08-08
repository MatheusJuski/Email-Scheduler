import schedule
import time
import csv 
import yagmail



EMAIL = "EXEMPLO@gmail.com"
SENHA = "Exemplo123" #senha de app para o gmail / password app for gmail

def enviar_email(destinatario, assunto, corpo):
    try:
        yag = yagmail.SMTP(EMAIL, SENHA)
        yag.SEND(to=destinatario, subject=assunto, content=corpo)
        print(f"Email enviado para {destinatario} com êxito!")
    except Exception as e:
        print(f"Erro ao enviar email para {destinatario}: {e}")


def agendar_emails():
    with open('email.csv', newline='', encoding='utf-8') as csvfile:
        leitor = csv.DictReader(csvfile)
        for linha in leitor:
            hora = linha['hora']
            email = linha['email']
            assunto = linha['assunto']
            mensagem = linha['mensagem']
            schedule.every().day.at(hora).do(enviar_email, email, assunto, mensagem)
        print(f"Email para {email} agendado para {hora} com sucesso!")



print("Iniciando o agendador de emails...")
agendar_emails()

print("Aguardando o horário agendado para enviar os emails...")
while True:
    schedule.run_pending()
    time.sleep(60)


