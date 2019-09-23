from mycroft import MycroftSkill, intent_file_handler


class DogBark(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('bark.dog.intent')
    def handle_bark_dog(self, message):
        self.speak_dialog('bark.dog')


def create_skill():
    return DogBark()

