from .base_form import BaseForm


class LoginForm(BaseForm):
    def __init__(self):
        super().__init__()

        email = self.email_field
        password = self.password_field
        self.submit_field

