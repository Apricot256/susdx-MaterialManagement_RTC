# The Rules of Realtime Cam

## Caution
this program is only only supports json format
<br><br>
## MQTT Request
### MQTT Topic
project-name/id(%04d)
<br><br>
### MQTT Value
|   Key   |  D-type  |  Value  | example |
|  ----   |   ----   |   ----  |   ----  |
| command |  srting  | command |  'take' |
<br>
### Example
Topic: 
```
Kyoshin/0001
```
Value: 
```
{'command': 'take'}
```
<br><br>

## MQTT Response

### MQTT Topic
image
<br><br>
### MQTT Value
|   Key   |  D-type  |  Value  | example |
|  ----   |   ----   |   ----  |   ----  |
| fac  |string  |  企業名 | 'Kyoshin' |
|  id  | int    |識別番号(工場など) | 1|
| img |  srting  | based64-image |  '/4TDKRX...' |
<br>
### Example
Topic: 
```
image
```

Value:

```
{
    'command': 'take',
    'fac': 'Kyoshin',
    'id': 0001,
    'img': '/4TDKRX...'
}
```