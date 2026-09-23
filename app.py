import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import Flask, flash, redirect, render_template, request, send_from_directory, url_for
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


def send_contact_email(name, email, subject, message):
    host = app.config.get('EMAIL_HOST', '').strip()
    port = app.config.get('EMAIL_PORT', 587)
    username = app.config.get('EMAIL_USERNAME', '').strip()
    password = app.config.get('EMAIL_PASSWORD', '').strip()
    receiver = app.config.get('EMAIL_RECEIVER', '').strip()

    if not host or not username or not password or not receiver:
        app.logger.warning('SMTP settings are incomplete; contact email was not sent.')
        return False

    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = receiver
    msg['Subject'] = f'Portfolio Contact: {subject or "New message"}'

    body = (
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Subject: {subject}\n\n"
        f"Message:\n{message}"
    )
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(host, int(port)) as server:
            server.starttls()
            server.login(username, password)
            server.send_message(msg)
        return True
    except Exception:
        app.logger.exception('Failed to send contact email through SMTP.')
        return False


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/contact')
def contact():
    return redirect(url_for('index') + '#contact')


@app.post('/contact')
def submit_contact():
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    subject = request.form.get('subject', '').strip()
    message = request.form.get('message', '').strip()

    if not name or not email or not subject or not message:
        flash('Please complete every field before sending your message.', 'error')
        return redirect(url_for('index') + '#contact')
    if '@' not in email or len(email) > 254:
        flash('Please enter a valid email address.', 'error')
        return redirect(url_for('index') + '#contact')

    sent = send_contact_email(name, email, subject, message)
    app.logger.info('Contact form received from %s (%s): %s', name, email, subject)

    if not sent:
        flash('Your message was received, but the email delivery is not configured yet. Please set your SMTP details in .env.', 'error')
        return redirect(url_for('index') + '#contact')

    flash('Thanks for reaching out! Your message was received.', 'success')
    return redirect(url_for('index') + '#contact')


@app.get('/download-resume')
def download_resume():
    return send_from_directory(
        app.config['RESUME_DIRECTORY'],
        app.config['RESUME_FILENAME'],
        as_attachment=True,
    )


@app.errorhandler(404)
def not_found(_error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(_error):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
