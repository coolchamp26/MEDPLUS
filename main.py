from medplus.ui.base import MedPlusApp
from medplus.ui.login_ui import LoginFrame
from medplus.ui.dashboard_ui import UserDashboardFrame, AdminDashboardFrame

class Application(MedPlusApp):
    def __init__(self):
        super().__init__()
        self.switch_frame(LoginFrame)

    def on_login_success(self, role, username):
        if role == 'ADMIN':
            self.switch_frame(AdminDashboardFrame, username=username)
        else:
            self.switch_frame(UserDashboardFrame, username=username)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
