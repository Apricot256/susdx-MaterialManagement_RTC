# -*- coding: utf-8 -*- 
import datetime
import paho.mqtt.client as mqtt
import cv2
import base64
import ssl
import json

# when conected with mqtt broker
def on_connect(client, userdata, flag, rc):
  print("Connected with result code " + str(rc))
  with open('./opt/config.json') as f:
    config = json.loads(f.read())
  Topic = config['projectName'] + '/' + config['deviceID']
  print('Topic :', Topic)
  client.subscribe(Topic)  # set topic to subscribe

# when disconected with mqtt broker
def on_disconnect(client, userdata, flag, rc):
  if  rc != 0:
    print("Unexpected disconnection.")
  
# when get message
def on_message(client, userdata, msg):

  print('[{}]'.format(datetime.datetime.now()), "topic:"+str(msg.topic), "payload:"+ str(msg.payload)[2:-1], "[QOS:{}]".format(msg.qos))
  
  # if the command is 'take'
  if json.loads(str(msg.payload)[2:-1])['command'] == 'take':
    
    # capture
    camid = int(json.loads(str(msg.payload)[2:-1])['camId'])
    cap = cv2.VideoCapture(camid-1)

    # set resolution 1920*1080
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    ret, frame = cap.read()
    print('capture result :', ret, '[', camid, ']')
    cap.release()
    ret, dst_data = cv2.imencode('.png', frame)
    print('converd result :',ret)

    # set elements to respons
    res = {
      'projectName': str(msg.topic).split('/')[0],
      'camId': json.loads(str(msg.payload)[2:-1])['camId'],
      'devId':  str(msg.topic).split('/')[1],
      'img': str(base64.b64encode(dst_data).decode('utf-8'))
    }

    # publish
    client.publish('image', json.dumps(res))
    print('Success in publishing!')


# main function
if __name__ == '__main__':
  client = mqtt.Client(transport = 'websockets')
  client.ws_set_options(path = '/')
  client.tls_set(tls_version=ssl.PROTOCOL_TLSv1_2)
  client.on_connect = on_connect
  client.on_disconnect = on_disconnect
  client.on_message = on_message

  client.connect("sus-dx.sora210.net", 8088, 60)  # connect
  client.loop_forever()