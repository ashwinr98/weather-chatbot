# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher



import requests

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city = tracker.get_slot('location')
        API_key = "3f246bb8fd69f938490d4a23736ae822"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
        Final_url = base_url + "appid=" + API_key + "&q=" + city + "&units=metric"
        weather_data = requests.get(Final_url).json()
        temperature=weather_data['main']['temp']
        response = "The current temperature at {} is {} degree Celsius.".format(city,temperature)
        dispatcher.utter_message(text=response)

        return []