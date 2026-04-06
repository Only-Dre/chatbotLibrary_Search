import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionBuscarPorTitulo(Action):
    def name(self): return "action_buscar_titulo"

    def run(self, dispatcher, tracker, domain):
        titulo = tracker.get_slot("titulo")
        resp = requests.get(f"https://openlibrary.org/search.json?title={titulo}")
        livros = resp.json()
        if livros:
            msg = "\n".join([f"📖 {l['title']} — {l['author_name'][0]}" for l in livros])
        else:
            msg = f"Nenhum livro encontrado para '{titulo}'."
        dispatcher.utter_message(text=msg)
        return []

class ActionBuscarPorAutor(Action):
    def name(self): return "action_buscar_autor"

    def run(self, dispatcher, tracker, domain):
        autor = tracker.get_slot("autor")
        resp = requests.get(f"https://openlibrary.org/search.json?author={autor}")
        livros = resp.json()
        msg = "\n".join([f"📖 {l['title']} — {l['author_name'][0]}" for l in livros]) if livros else "Nenhum livro encontrado."
        dispatcher.utter_message(text=msg)
        return []