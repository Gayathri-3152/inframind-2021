import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager,Screen,FadeTransition
import requests
from threading import Timer

Window.size = (320, 480)
Window.clearcolor=(209/255,229/255,1,1)

class MainScreen(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1

        def switch(instance):
            Mainscreen.screen_manager.current = "Chatbot"

        def show(instance):
            self.msg.text = "Be cautious about your health, it seems that you may have :\n"

            if(int(self.glucose.text) >=140 and int(self.glucose.text) < 200):
                self.msg.text = self.msg.text+"Prediabetes\n"
            elif (int(self.glucose.text) >= 200):
                self.msg.text = self.msg.text + "Diabetes\n"

            if (int(self.btemp.text) >100 and int(self.resrate.text) >= 24):
                self.msg.text = self.msg.text +"Bronchitis\n"

            if (int(self.oxysat.text) < 96):
                self.msg.text = self.msg.text + "Hypoxemia\n"

            if ((int (self.oxysat.text) >= 92 and int(self.oxysat.text) <= 95) and int(self.heartrate.text) >= 100 and int(self.resrate.text) >= 20):
                self.msg.text = self.msg.text + "Asthma\n"

            if ((int(self.bp.text) < 90 or int(self.bp1.text) < 60)):
                self.msg.text = self.msg.text + "Low Blood Pressure\n"
            elif ((int(self.bp.text) >= 180 or int(self.bp1.text) >= 120)):
                self.msg.text = self.msg.text + "Severe Blood Pressure\n"
            elif ((int(self.bp.text) >= 140 or int(self.bp1.text) >= 90)):
                self.msg.text = self.msg.text + "High Blood Pressure\n"

            if ((int(self.bp.text) >= 140 or int(self.bp1.text) >= 90) and int(self.heartrate.text) >= 100):
                self.msg.text = self.msg.text + "Relax,Don't Stress too much\n"

            if(self.msg.text =="Be cautious about your health, it seems that you may have :\n"):
                self.msg.text="You are doing great, keep maintaining your health"


        self.top_grid = GridLayout(size_hint_y=None,height=50,padding=[25,10,25,10],spacing=25)
        self.top_grid.cols = 2

        self.check = Button(text="Check Me",size_hint_x=None,width=130,background_normal='',background_color=[3/255,94/255,252/255,1])
        self.check.bind(on_press=show)
        self.top_grid.add_widget(self.check)
        self.chat = Button(text="Chat bot",size_hint_x=None,width=110,background_normal='',background_color=[3/255,94/255,252/255,1])
        self.chat.bind(on_press=switch)
        self.top_grid.add_widget(self.chat)


        self.add_widget(self.top_grid)


        self.top_grid = GridLayout(padding=10,spacing=6)
        self.top_grid.cols = 3

        self.top_grid.add_widget(Label(text="Blood Pressure",size_hint_x=None,width=160,color=[0,0,0,1]))
        self.bp = TextInput(multiline=False,size_hint_x=None,width=50)
        self.top_grid.add_widget(self.bp)
        self.bp1 = TextInput(multiline=False,size_hint_x=None,width=60)
        self.top_grid.add_widget(self.bp1)

        self.top_grid.add_widget(Label(text="Body Temperature",size_hint_x=None,width=160,color=[0,0,0,1]))
        self.btemp = TextInput(multiline=False,size_hint_x=None,width=50)
        self.top_grid.add_widget(self.btemp)
        self.btemp1 = TextInput(multiline=False,text="F",size_hint_x=None,width=60)
        self.top_grid.add_widget(self.btemp1)


        self.top_grid.add_widget(Label(text="Oxygen Saturation",size_hint_x=None,width=160,color=[0,0,0,1]))
        self.oxysat = TextInput(multiline=False,size_hint_x=None,width=50)
        self.top_grid.add_widget(self.oxysat)
        self.oxysat1 = TextInput(multiline=False,text="%",size_hint_x=None,width=60)
        self.top_grid.add_widget(self.oxysat1)

        self.top_grid.add_widget(Label(text="Respiration Rate",size_hint_x=None,width=160,color=[0,0,0,1]))
        self.resrate = TextInput(multiline=False,size_hint_x=None,width=50)
        self.top_grid.add_widget(self.resrate)
        self.resrate1 = TextInput(multiline=False,text="/min",size_hint_x=None,width=60)
        self.top_grid.add_widget(self.resrate1)

        self.top_grid.add_widget(Label( text="Heart Rate",size_hint_x=None,width=160,color=[0,0,0,1]))
        self.heartrate = TextInput(multiline=False,size_hint_x=None,width=50)
        self.top_grid.add_widget(self.heartrate)
        self.heartrate1 = TextInput(multiline=False,text="/min",size_hint_x=None,width=60)
        self.top_grid.add_widget(self.heartrate1)

        self.top_grid.add_widget(Label(text="Blood Glucose",size_hint_x=None,width=160,color=[0,0,0,1]))
        self.glucose= TextInput(multiline=False,size_hint_x=None,width=50)
        self.top_grid.add_widget(self.glucose)
        self.glucose1 = TextInput(multiline=False,text="mg/dL",size_hint_x=None,width=60)
        self.top_grid.add_widget(self.glucose1)

        self.add_widget(self.top_grid)

        self.top_grid = GridLayout(padding=25)
        self.top_grid.cols = 3

        self.msg = TextInput(multiline=True,background_color=[1,1,1,1])
        self.top_grid.add_widget(self.msg)

        self.add_widget(self.top_grid)


        def delete():
            self.bp.text = " "
            self.bp1.text = " "
            self.btemp.text = " "
            self.oxysat.text = " "
            self.resrate.text = " "
            self.heartrate.text = " "
            self.glucose.text = " "

        def data():
            response = requests.get('http://localhost:5000/api/data')
            dataGotFromApi = response.json()
            if ((int(dataGotFromApi[0]["systolic blood pressure"]) < 90 or int(dataGotFromApi[0]["diastolic blood pressure"]) < 60) and (int(dataGotFromApi[0]["systolic blood pressure"]) >= 140 or int(dataGotFromApi[0]["diastolic blood pressure"]) >= 90) ):
                self.bp.foreground_color = [252 / 255, 15 / 255, 3 / 255, 1]
                self.bp1.foreground_color = [252 / 255, 15 / 255, 3 / 255, 1]
            else:
                self.bp.foreground_color = [42 / 255, 212 / 255, 19 / 255, 1]
                self.bp1.foreground_color = [42 / 255, 212 / 255, 19 / 255, 1]
            if (int(dataGotFromApi[0]["oxygen saturation"]) <= 95):
                self.oxysat.foreground_color = [252 / 255, 15 / 255, 3 / 255, 1]
                self.oxysat1.foreground_color = [252 / 255, 15 / 255, 3 / 255, 1]
            else:
                self.oxysat.foreground_color = [42 / 255, 212 / 255, 19 / 255, 1]
                self.oxysat1.foreground_color = [42 / 255, 212 / 255, 19 / 255, 1]
            if (int(dataGotFromApi[0]["body temperature"]) >= 100):
                self.btemp.foreground_color = [252 / 255, 15 / 255, 3 / 255, 1]
                self.btemp1.foreground_color = [252 / 255, 15 / 255, 3 / 255, 1]
            else:
                self.btemp.foreground_color = [42 / 255, 212 / 255, 19 / 255, 1]
                self.btemp1.foreground_color = [42 / 255, 212 / 255, 19 / 255, 1]
            if (int(dataGotFromApi[0]["respiration rate"]) >= 20):
                self.resrate.foreground_color = [252 / 255, 15 / 255, 3 / 255, 1]
                self.resrate1.foreground_color = [252 / 255, 15 / 255, 3 / 255, 1]
            else:
                self.resrate.foreground_color = [42 / 255, 212 / 255, 19 / 255, 1]
                self.resrate1.foreground_color = [42 / 255, 212 / 255, 19 / 255, 1]
            if (int(dataGotFromApi[0]["heart rate"]) >= 100):
                self.heartrate.foreground_color = [252 / 255, 15 / 255, 3 / 255, 1]
                self.heartrate1.foreground_color = [252 / 255, 15 / 255, 3 / 255, 1]
            else:
                self.heartrate.foreground_color = [42/255,212/255,19/255,1]
                self.heartrate1.foreground_color = [42 / 255, 212 / 255, 19 / 255, 1]
            if (int(dataGotFromApi[0]["blood glucose"]) >= 140):
                self.glucose.foreground_color = [252 / 255, 15 / 255, 3 / 255, 1]
                self.glucose1.foreground_color = [252 / 255, 15 / 255, 3 / 255, 1]
            else:
                self.glucose.foreground_color = [42 / 255, 212 / 255, 19 / 255, 1]
                self.glucose1.foreground_color = [42 / 255, 212 / 255, 19 / 255, 1]

            self.bp.text = str(dataGotFromApi[0]["systolic blood pressure"])
            self.bp1.text = str(dataGotFromApi[0]["diastolic blood pressure"])
            self.btemp.text = str(dataGotFromApi[0]["body temperature"])
            self.oxysat.text = str(dataGotFromApi[0]["oxygen saturation"])
            self.resrate.text = str(dataGotFromApi[0]["respiration rate"])
            self.heartrate.text = str(dataGotFromApi[0]["heart rate"])
            self.glucose.text = str(dataGotFromApi[0]["blood glucose"])

            Timer(30, delete).start()
            Timer(28, data).start()


        data()




class Chatbot(GridLayout):
    def __init__(self, **kwargs):
        super(Chatbot,self).__init__(**kwargs)

        self.cols=1
        def back(instance):
            Mainscreen.screen_manager.current="MainScreen"

        def sendmsg(instance):
            text = self.type.text
            msg = "\nYou : " + self.type.text + "\n"
            self.bot.text = self.bot.text + msg

            if ( text == "hi"):
                 self.bot.text = self.bot.text +"Bot : hello\n"
            elif (text == "hello"):
                 self.bot.text = self.bot.text +"Bot : hi\n"
            elif (text  == "how are you"):
                self.bot.text = self.bot.text + "Bot : I am fine,Thank you\n"
            elif (("need" in text and "help" in text) or ("help" in text)):
                 self.bot.text = self.bot.text +"Bot : how can i help you ?\n"
            elif (text  == "what is chatbot" or text =="what is bot"):
                 self.bot.text = self.bot.text + "Bot : chatbot is a python program to help you\n"
            elif ("fever" in text):
                self.bot.text = self.bot.text + "Bot : take paracetamol for two days if it lasts more than that consult a doctor\n"
            elif ("dizzy" in text):
                self.bot.text = self.bot.text + "Bot : may be your haemoglobin is low or else you need a healthy diet \n"
            elif ( "blood pressure" in text or "bp" in text ):
                self.bot.text = self.bot.text + "Bot : exercise regularly,keep a healthy diet and consult a doctor periodically \n"
            elif ( "smoking" in text):
                self.bot.text = self.bot.text + "Bot : it is in the packet smoking kills\n"
            elif ("drug" in text and "addict" in text):
                self.bot.text = self.bot.text + "Bot : drug addiction is dangerous so get yourself or your loved ones into rehabilitation centers to combat addiction \n"
            elif ("cold" in text):
                self.bot.text = self.bot.text + "Bot : drink warm water with honey and take good night sleep after taking cold tonic\n"
            elif ("leg pain" in text or "arthritis" in text ):
                self.bot.text = self.bot.text + "Bot : exercise regularly and get into therapy\n"
            elif ("hair fall" in text ):
                self.bot.text = self.bot.text + "Bot : don't stress too much, enrich diet with protein and keep yourself hydrated\n"
            elif ("eating disorder" in text or "bulimia" in text ):
                self.bot.text = self.bot.text + "Bot : take counseling, medication and therapy it is an serious issue\n"
            elif ("cancer" in text and "tumor" in text):
                self.bot.text = self.bot.text + "Bot : Tumor can be benign or malignant ...malignant is cancer ...prevension is better than cure do get it check.\n"
            elif ("eye care" in text):
                self.bot.text = self.bot.text + "Bot : reduce watching tv and mobile phone and wash your eyes with cold water\n"
            elif ("food poison" in text):
                self.bot.text = self.bot.text + "Bot : avoid outside food and take oral rehydration solution(ORS)\n"
            elif ("obesity" in text or "overweight" in text):
                self.bot.text = self.bot.text + "Bot : take healthy diet,fresh vegetables and fruits ,avoid fast food , increase physical activity and exercise regularly\n"
            elif ("asthma" in text):
                self.bot.text = self.bot.text + "Bot : use asthma inhaler, take oxygen therapy, if you are smoking quit it and stay away form allergens\n"
            elif ("kidney stone" in text):
                self.bot.text = self.bot.text + "Bot : stay hydrated, eat more calcium-rich food, reduce salt and consult a doctor"
            elif ("insomnia" in text or "sleepless" in text):
                self.bot.text = self.bot.text + "Bot : congnitive behavioral therapy and light therapy is suggested, stay active, keep your bedtime and wakeup time consistent\n"
            elif ("stress" in text):
                self.bot.text = self.bot.text + "Bot : excercise regularly ,if you are too stressed pshychotherapies is suggested or else slow down, take a deep breath, accept the things you can't change and make time for hobbies.\n"
            elif ("headache" in text or "head ache" in text):
                self.bot.text = self.bot.text + "Bot : take aspirin or paracetamol and resting in darkend room may also help.\n"
            elif ("anxiety" in text):
                self.bot.text = self.bot.text + "Bot : exercise regularly,take medications like antidepressants or counselling may also be suggested .if you smoke quit it.\n"
            elif ("back pain" in text):
                self.bot.text = self.bot.text + "Bot : take pain reliever like diclofenac or naproxen or try some pain relieving gel.\n"
            elif ("diabetes" in text or "sugar" in text):
                self.bot.text = self.bot.text + "Bot : screen your blood sugar level regularly, be conscious about your diet,insulin or oral medication is the main treatment, periodic counsultation of doctor is required .\n"
            else:
                self.bot.text = self.bot.text + "Bot : none\n"

            self.type.text = ""

        self.top_grid = GridLayout(size_hint_y=None,height=50,padding=10)
        self.top_grid.cols = 1

        self.btn=Button(text="Back",size_hint_x=None,width=60,background_normal='',background_color=[3/255,94/255,252/255,1])
        self.btn.bind(on_press=back)
        self.top_grid.add_widget(self.btn)

        self.add_widget(self.top_grid)

        self.top_grid = GridLayout(size_hint_y=None,height=350,padding=10)
        self.top_grid.cols = 2

        self.bot=TextInput(multiline=True)
        self.top_grid.add_widget(self.bot)

        self.add_widget(self.top_grid)

        self.top_grid = GridLayout(size_hint_y=None,height=50,padding=10,spacing=2)
        self.top_grid.cols = 2

        self.type = TextInput(multiline=True,size_hint_x=None,width=240)
        self.top_grid.add_widget(self.type)

        self.btn1 = Button(text="send",size_hint_x=None,width=60,background_normal='',background_color=[3/255,94/255,252/255,1])
        self.btn1.bind(on_press=sendmsg)
        self.top_grid.add_widget(self.btn1)

        self.add_widget(self.top_grid)

class app(App):
    def build(self):
        self.screen_manager=ScreenManager()

        self.Mainscreen = MainScreen()
        screen=Screen(name="MainScreen")
        screen.add_widget(self.Mainscreen)
        self.screen_manager.add_widget(screen)

        self.chatbot = Chatbot()
        screen = Screen(name="Chatbot")
        screen.add_widget(self.chatbot)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == "__main__":
    Mainscreen = app()
    Mainscreen.run()


