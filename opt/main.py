# -*- coding: utf-8 -*- 
import datetime
import paho.mqtt.client as mqtt
import cv2
import base64
import ssl

Topic = 'request/testProject'

# conected with mqtt broker
def on_connect(client, userdata, flag, rc):
  print("Connected with result code " + str(rc))
  client.subscribe(Topic)  # set topic to subscribe

# disconected with mqtt broker
def on_disconnect(client, userdata, flag, rc):
  if  rc != 0:
    print("Unexpected disconnection.")
  
# get message
def on_message(client, userdata, msg):
  print('S[{}]'.format(datetime.datetime.now()), "topic:"+str(msg.topic), "payload:"+str(msg.payload), "[QOS:{}]".format(msg.qos))
  if str(msg.payload) == "b'take'":
    # capture
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    print('capture result :',ret)
    cap.release()
    ret, dst_data = cv2.imencode('.png', frame)
    print('converd result :',ret)
    client.publish("image/testProject", str(base64.b64encode(dst_data).decode('utf-8')))



if __name__ == '__main__':
  client = mqtt.Client(transport = 'websockets')
  client.ws_set_options(path = '/')
  client.tls_set(tls_version=ssl.PROTOCOL_TLSv1_2)
  client.on_connect = on_connect
  client.on_disconnect = on_disconnect
  client.on_message = on_message

  client.connect("sus-dx.sora210.net", 8088, 60)  # connect
  client.loop_forever()