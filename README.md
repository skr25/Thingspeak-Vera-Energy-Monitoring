# Thingspeak-Vera-Energy-Monitoring
This project captures watts and Kwatts from Vera for the connected devices and updates the Thingspeak charts with all data received. You can see the graphs of energy uses daily, weekly, and monthly and understand the trend.

Vera has an Energy Monitoring device that publishes Watts and kWh to my local MQTT server. This program reads MQTT published values for KWH and Watts and logs to the Thinkspeak chart using Thingspeak API and Key.

