# The Rules of Realtime Cam
## MQTT Request
### MQTT Topic
**"projectName/deviceID"**
### MQTT Value
|   Key   |  D-type  |  Value  | example |
|  ----   |   ----   |   ----  |   ----  |
|  camId  |  srting  | command |  "0001" |
| command |  srting  | command |  "take" |

### Example
Topic: 
~~~
Kyoshin/0001
~~~
Value: 
~~~json
{
    "camId": "0001",
    "command": "take"
}
~~~

## MQTT Response

### MQTT Topic
**"image"**
### MQTT Value
|   Key   |  D-type  |  Value  | example |
|  ----   |   ----   |   ----  |   ----  |
| projectName | string |   projectName |   "Kyoshin"   |
|    camId    | string |    cameraID   |     "0001"    |
|    devId    | string |    deviceID   |     "0001"    |
|     img     | srting | based64-image |  "/4TDKRX..." |

### Example
Topic: 
~~~
image
~~~

Value:
~~~json
{
    "command": "take",
    "fac": "Kyoshin",
    "camId": "0001",
    "devId": "0001",
    "img": "/4TDKRX..."
}
~~~
