import json

class Media:
    def __init__(self, email="", cv="", linkedin="", github=""):
        self.email = email
        self.cv = cv
        self.linkedin = linkedin
        self.github = github

class Skill:
    def __init__(self, icon, name):
        self.icon = icon
        self.name = name

class Info :
    def __init__(self, icon, title, subtitle, description, dates="", certificate="", skills=[], image="", url="", github=""):
        self.icon = icon
        self.title = title
        self.subtitle = subtitle
        self.description = description
        self.dates = dates
        self.certificate = certificate
        self.skills = [Skill(**skill) for skill in skills]
        self.image = image
        self.url = url
        self.github = github

class Extra :
    def __init__(self, image, title, description, url):
        self.image = image
        self.title = title
        self.description = description
        self.url = url

class Data :
    def __init__(self, avatar, name, job_position, location, media, about, skills, experience, projects, training, extras):
        self.avatar = avatar
        self.name = name
        self.job_position = job_position
        self.location = location
        self.media = Media(**media)
        self.about = about
        self.skills = [Skill(**skill) for skill in skills]
        self.experience = [Info(**info) for info in experience]
        self.project = [Info(**info) for info in projects]
        self.training = [Info(**info) for info in training]
        self.extras = [Extra(**extra) for extra in extras]

def load_data(lang='es'):
    with open(f"assets/data/data_{lang}.json") as file:
        json_data = json.load(file)
    return Data(**json_data)

data_es = load_data('es')
data_en = load_data('en')