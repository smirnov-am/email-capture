import os


class Config:
    SECRET_KEY = b'secret123456'
    AWS_REGION = os.environ.get('AWS_REGION', 'us-east-1')
    G_TAG = os.environ.get('G_TAG', 'G-12345')
    G_EVENT = os.environ.get('G_EVENT', 'registration')
    TABLE_NAME = os.environ.get('TABLE_NAME', 'email-leads')
    DOMAIN = os.environ.get('DOMAIN', 'example.com')

    @staticmethod
    def init_app(app):
        pass