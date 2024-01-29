import pygame

class Text:
    def __init__(self, currentLanguage:dict):
        self.allLanguages = {
            "PTBR":{
                "menu":{'Iniciar':(50, 50), 'Opções':(50, 100), '[ Sair ]':(50, 200)},
                "config":{'Tela':(50, 80), 'Resolução:':(50, 130), 'Linguagem:':(50, 180), 'Aceitar':(50, 230), '[ Voltar ]':(50, 400)},
                "window":{"< Tela Cheia >":(150, 80), "<    Janela    >":(150, 80)},
                "resolutions":{"< 1920 x 1080 >":(150, 130), "< 1366 x 768   >":(150, 130), "<   640 x 480   >":(150, 130)},
                "langSelection":{"<    Inglês    >":(150, 180), "< Português  >":(150, 180)}
            },

            "EN":{
                "menu":{'Start':(50, 50), 'Options':(50, 100), '[ Exit ]':(50, 200)},
                "config":{'Screen':(50, 80), 'Resolution:':(50, 130), 'Language:':(50, 180), 'Accept':(50, 230), '[ Back ]':(50, 400)},
                "window":{"< Full Screen >":(150, 80), "<    Window    >":(150, 80)},
                "resolutions":{"< 1920 x 1080 >":(150, 130), "< 1366 x 768   >":(150, 130), "<   640 x 480   >":(150, 130)},
                "langSelection":{"<    English    >":(150, 180), "< Portugues  >":(150, 180)}
            }
        }
        
        self.currentLanguage = currentLanguage
        self.language = self.allLanguages[self.currentLanguage]

    
    def names(self, menu:str=None):
        return tuple(self.language[menu].keys())
    

    def positions(self, menu:str=None):
        return tuple(self.language[menu].values())
    

    def items(self, menu:str=None, name:str=None):
        return tuple(self.language[menu].items())
    

    def length(self, menu:str=None):
        return len(self.language[menu])