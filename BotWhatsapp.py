from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


PATH = "C:\\Users\\leven\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.implicitly_wait(5)
driver.maximize_window()




def VerifCodeQR():
    try:
        Codeqr = driver.find_element(By.TAG_NAME, "canvas")
    except:
        return False
    return True


def EnvoyezFichier(nomdufichier : str):
    fichier = open(nomdufichier, mode='r', encoding='utf-8')
    InputSelection = driver.find_element(By.XPATH, "//p[@class='selectable-text copyable-text']")
    filecontent = fichier.read()
    InputSelection.send_keys(filecontent, Keys.ENTER)
    fichier.close()



def EnvoyezMessage(message : str):
    InputSelection = driver.find_element(By.XPATH,"//p[@class='selectable-text copyable-text']")
    InputSelection.send_keys(message, Keys.ENTER)



def SelectionnerChat(nomchat : str):
    recherche = True

    while recherche:
        elements = driver.find_elements(By.TAG_NAME,"span")
        for element in elements:
            if element.text == nomchat:
                print("Le chat a été trouvé !")
                element.click()
                recherche = False
                break

def BotWhatsapp():
    driver.get("https://web.whatsapp.com/")
    time.sleep(5)

    Codeqr_Present = True

    while Codeqr_Present:
        Codeqr_Present = VerifCodeQR()
        if Codeqr_Present == True:
            print("En attente d'authentification ...")
            time.sleep(2)
        else:
            print("Authentification réussie !")
    print("test")
    SelectionnerChat("Groupe robot")
    EnvoyezFichier('montxt2.txt')






BotWhatsapp()