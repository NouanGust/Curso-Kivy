# Importações, sempre vão ter algumas
from kivy.app import App
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Criando um loop de botões
        for i in range(0, 100):
            # Size não é uma propriedade aqui, e sim uma variável
            size = dp(100)
            b = Button(text=str(i+1), size_hint=(None, None), size=(size, size))
            # Elementos adicionados pelo init, tem prioridade
            self.add_widget(b)


# Aqui será referenciado direto no arquivo kv
#class GridLayoutExample(GridLayout):
#    pass

class AnchorLayoutExample(AnchorLayout):
    pass

# O Modelo de caixas, divide a tela em pates iguais para os elementos
class BoxLayoutExample(BoxLayout):
    pass
""" # Criando a interface direto no código, para isso precisa de um construtor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Mudando as propriedades do modelo
        self.orientation = "vertical"
        # Criando os elementos
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")
        # Adicionando no Layout
        self.add_widget(b1)
        self.add_widget(b3)
        self.add_widget(b2)
"""

# Criando um widget principal, usando a classe Widget
class MainWidget(Widget):
    pass
# Sempre tem que ter uma classe "principal" que herda do App da biblioteca
class TheLabApp(App):
    pass

# Aqui o aplicativo "roda" de fato, está sendo invocado/chamado
TheLabApp().run()