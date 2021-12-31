import speech_recognition as sr
import pyautogui
import webbrowser
import sys

def Esperar_Comando():
    Mic_Rec_Comando = sr.Recognizer()
    with sr.Microphone() as Source:
        Mic_Rec_Comando.adjust_for_ambient_noise(Source)
        print("Diga o Comando: ")
        Audio_Comando = Mic_Rec_Comando.listen(Source)
        try:
            Frase_Comando = Mic_Rec_Comando.recognize_google(Audio_Comando, language='pt-BR')
            Comando = Frase_Comando.lower()

            if 'abrir navegador' in Comando:
                url = 'https://docs.python.org/'
                webbrowser.open_new(url)
                Esperar_Comando()
                
            if 'abrir youtube' in Comando:
                url = 'https://www.youtube.com/'
                webbrowser.open_new(url)
                Esperar_Comando()
                
            if 'abrir google' in Comando:
                url = 'https://www.google.com/'
                webbrowser.open_new(url)
                Esperar_Comando()
                
            if 'encerrar' in Comando:
                print("Sistema Encerrado")
                sys.exit()
                
        except sr.UnkownValueError:
            print("Não entendi")
            
        return Frase_Comando


def Testar_Integracao():
    
    try:  
        Mic_Rec = sr.Recognizer()
        with sr.Microphone() as Source:
            Mic_Rec.adjust_for_ambient_noise(Source)
            print("Teste o Microfone: ")
            Audio_Integracao = Mic_Rec.listen(Source)
            
        try:
            Frase_Integracao = Mic_Rec.recognize_google(Audio_Integracao, language='pt-BR')
            Comando_Integracao = Frase_Integracao.lower()
            print("Você disse: " + Frase_Integracao)
            
            if 'teste de integração' in Comando_Integracao:
                print('Teste de Integração com Sucesso.')
                Executar_Comando()

        except sr.UnkownValueError:
            print("Erro Comunicação")
            
        return Frase_Integracao
                
                
    except:
        print("Integração Perdida")
                
        


def Executar_Comando():
    Esperar_Comando()
    

Testar_Integracao()