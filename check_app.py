from app import app

client = app.test_client()
resp = client.get('/')
print('status', resp.status_code)
print('contains_contact', 'id="contact"' in resp.get_data(as_text=True))
print('contains_form', 'contact-form' in resp.get_data(as_text=True))
