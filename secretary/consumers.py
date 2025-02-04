import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class MeetingConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data = json.loads(text_data)
        async_to_sync(self.channel_layer.group_send)(
            'meeting_notifications',
            {
                'type': 'meeting_message',
                'message': data['message']
            }
        )

    def meeting_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'message': message
        }))
