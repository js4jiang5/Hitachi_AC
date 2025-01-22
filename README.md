# Hitachi_AC

Hitachi_AC is an ESPHome external component controlling Climate IR transceiver for Hitachi air conditioner. It is modified from Climate IR built-in component hitachi_ac344 for some enhancements.

### Enhancements
The enhancements include
1. setup of default horizontal direction when swing is off. The value could be "left_max", "left", "middle", "right", "right_max".
2. enable mildewproof when HVAC mode is "cool". 
3. add custom_preset modes "Cool", "Heat", "Dry", "Fan_only", so that all parameters (HVAC mode, fan_speed, swing, temperature) can be set in single command.  Default horizontal swing for "Cool" and "Dry" is auto, while default swing for "Heat" and "Fan_only" is off.

### Installation
Just copy "hitach_ac" folder to homeassistant/esphome/components/ and that's all.

### Usage
```
climate:
  - platform: hitachi_ac
    id: ac_study_room
    name: "ac_study_room"
    transmitter_id: ir_tx
    receiver_id: ir_rx
    visual:
      min_temperature: 18
      max_temperature: 40
      temperature_step: 0.1
    sensor: temp
    horizontal_default: "right"
```

### Example
[ac_study_room.yaml](https://github.com/js4jiang5/Hitachi_AC/blob/main/ac-study_room.yaml)