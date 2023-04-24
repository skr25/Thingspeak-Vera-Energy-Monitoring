import paho.mqtt.client as mqttClient
import time,datetime,json
import http.client,urllib.parse
from time import localtime, strftime




def logData(field,value):

       params = urllib.parse.urlencode({field: value,'key':'JW2YZ9M61EPMFJGY'})
       headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
       conn = http.client.HTTPConnection("api.thingspeak.com:80")

       try:
             conn.request("POST", "/update", params, headers)
             response = conn.getresponse()
             print(field)
             print(value)
             #print (strftime("%a, %d %b %Y %H:%M:%S", localtime()))
             print (response.status, response.reason)
             data = response.read()
             conn.close()
       except:
             print ("connection failed")

 
def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected                #Use global variable
        Connected = True                #Signal connection 
 
    else:
 
        print("Connection failed")
 
def on_message(client, userdata, message):
    global first_time
    print("Received message '" + message.payload.decode() + "' on topic '"
        + message.topic + "' with QoS " + str(message.qos))
    json_obj = json.loads(message.payload.decode())
    second_time =  datetime.datetime.now()
    delta = second_time - first_time
    diff = divmod(delta.days * 86400 + delta.seconds, 60)
    if diff[0] == 0  and diff[1] <17 and diff[1] >3 :
        pass
    else:
       
           if "Watts" in json_obj:
                 
                 logData('field1',json_obj["Watts"])
           else:
                 time.sleep(16)
                 logData('field2',json_obj["KWH"]) 
         
           first_time = datetime.datetime.now()


first_time =  datetime.datetime.now()

Connected = False   #global variable for the state of the connection
 
broker_address= "192.168.1.100"  #Broker address
port = 1884                         #Broker port
#user = "yourUser"                    #Connection username
#password = "yourPassword"            #Connection password
 
client = mqttClient.Client("Python_thingspeak")               #create new instance
#client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback
 
client.connect(broker_address, port=port)          #connect to broker
 
client.loop_start()        #start the loop
 
while Connected != True:    #Wait for connection
    time.sleep(0.1)
 
client.subscribe("Vera/Events/138")
 
try:
    while True:
        time.sleep(1)
 
except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()
