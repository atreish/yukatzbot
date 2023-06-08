from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionProvideDegreesOffered(Action):
    def name(self) -> Text:
        return "action_provide_degrees_offered"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Response message
        response = "The Katz school offers the following degrees:\n\n" \
                   "- Artificial Intelligence (AI)\n" \
                   "- Data Analytics and Visualization (DAV)\n" \
                   "- Biotechnology Management and Entrepreneurship (BME or BTM)\n" \
                   "- Cybersecurity (Cyber)\n" \
                   "- Digital Marketing and Media (DMM)\n" \
                   "- Mathematics (MAT)\n" \
                   "- Physics (PHY)\n" \
                   "- Occupational Therapy (OTD)\n" \
                   "- Physician Assistant Studies (PAS)\n" \
                   "- Speech-Language Pathology (SLP)\n\n" \
                   "Some of these degrees are available online and others are offered on-campus."

        dispatcher.utter_message(text=response)

        return []

class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Your fallback logic
        response = "Sorry, I didn't understand. Can you please rephrase your question?"

        dispatcher.utter_message(text=response)

        return []       
