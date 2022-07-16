# The Rules of Realtime Cam

## Caution
this program is only only supports json format
<br><br>
## MQTT Request
### MQTT Topic
会社名/社内番号(%04d)

### MQTT Value
|   Key   |  D-type  |  Value  | example |
|  ----   |   ----   |   ----  |   ----  |
| command |  srting  | コマンド |  'take' |

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

### MQTT Value
|   Key   |  D-type  |  Value  | example |
|  ----   |   ----   |   ----  |   ----  |
| fac  |string  |  企業名 | 'Kyoshin' |
|  id  | int    |識別番号(工場など) | 1|
| img |  srting  | based64-image |  '/4TDKRX...' |

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
    'if': 0001,
    'img': '/4TDKRX...'
}
```