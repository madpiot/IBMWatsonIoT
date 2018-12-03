import ibmiotf.device
import random
import time
#import ibmiotf.application
organization = "5pnarz" #add organisation from the IoT platform service
deviceType = "iotsensor" #add device type from the IoT platform service
deviceId = "iotsensor" #add device ID from the IoT platform service
authMethod = "token"
authToken = "suryaiot" #add authentication token from the IoT platform service


temp = 0
hum = 0

# Initialize the device client.
deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
client = ibmiotf.device.Client(deviceOptions)
client.connect()
print(client)
#client = ibmiotf.application.Client(options)
print("init successful")


# get temperature and humidity from the sensor
def getTempHum():
    global temp
    global hum
    temp = random.randint(15,40)
    hum =  random.randint(50,90)


def myCommandCallback(cmd):
    print("Command received: %s\n" % cmd.data)

    
def myOnPublishCallback():
    print("Confirmed event received by IoTF")

# Connect and send a datapoint 
def send(data):
    print(data)
    success = client.publishEvent("data", "json", data, qos=0, on_publish=myOnPublishCallback)
    if not success:
        print("Not connected to IoTF")

    

if __name__=='__main__':
    while True:
        try:
            getTempHum()
            send({"temp":temp, "hum": hum})
            client.commandCallback = myCommandCallback
            time.sleep(2)
        except KeyboardInterrupt:
            client.disconnect()
            break

