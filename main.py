import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class NodeRedIntegration(BoxLayout):
    def __init__(self, **kwargs):
        super(NodeRedIntegration, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 40
        self.spacing = 20

        self.btn_enviar = Button(text='Enviar mensagem para o Node-RED')
        self.btn_enviar.bind(on_press=self.enviar_mensagem)

        self.add_widget(self.btn_enviar)

    def enviar_mensagem(self, instance):
        url = 'http://localhost:1880/mensagem'  # Substitua pela URL correta do Node-RED

        # Aqui você pode adicionar a lógica para construir a mensagem a ser enviada
        mensagem = {'conteudo': 'Olá, Node-RED!'}

        response = requests.post(url, json=mensagem)

        if response.status_code == 200:
            print('Mensagem enviada com sucesso para o Node-RED.')
        else:
            print('Erro ao enviar mensagem para o Node-RED.')

class MyApp(App):
    def build(self):
        return NodeRedIntegration()

MyApp().run()
