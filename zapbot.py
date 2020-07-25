from selenium import webdriver
import time


class whatsbot:
    def __init__(self):
        self.mensagem = 'Testando meu Bot'
        self.grupos = ['Pcj', 'meu']
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'D:\Programação\Python\Bot de Mensagens para '
                                                       r'grupo\chromedriver.exe')

    def EnvioDeMensagens(self):
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(15)
        while True:
            for grupo in self.grupos:
                grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
                time.sleep(3)
                grupo.click()
                chat_box = self.driver.find_element_by_class_name('_3uMse')
                time.sleep(3)
                chat_box.click()
                chat_box.send_keys(self.mensagem)
                botao_enviar = self.driver.find_element_by_xpath("//span[@data-testid='send']")
                time.sleep(3)
                botao_enviar.click()
                time.sleep(5)


bot = whatsbot()
bot.EnvioDeMensagens()

# <span dir="auto" title="meu" class="_3ko75 _5h6Y_ _3Whw5">meu</span>
# <div tabindex="-1" class="_3uMse">
# <span data-testid="send" data-icon="send" class="">
