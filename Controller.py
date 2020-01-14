import web
from Models import RegisterModel

urls = (
    '/', "Home",
    '/register', "Register",
    '/signup', "SignUp"
)

render = web.template.render("views/Templates", base="MainLayout")
app = web.application(urls, globals())

# Classes/Routes


# Render homepage
class Home:
    def GET(self):
        return render.home()


# Render registration form
class Register:
    def GET(self):
        return render.register()


# Post registration form
class SignUp:
    def POST(self):
        data = web.input()

        reg_model = RegisterModel.RegisterModel()  # Filename.Class()
        reg_model.insert_user(data)
        return data.username


if __name__ == "__main__":
    app.run()

