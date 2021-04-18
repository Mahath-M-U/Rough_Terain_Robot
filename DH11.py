import Adafruit_DHT
sensor = Adafruit_DHT.DHT11

def humidity_temperature(Pin_Number):
    print("Flow Line :  Checking Temperature & Humidity ........")
    try:
        #initialization
        DHT11_pin = Pin_Number
        humidity, temperature = Adafruit_DHT.read_retry(sensor, DHT11_pin)
        if humidity is not None and temperature is not None:
            print("Flow Line :  DH11 Sensor value Passed...")
        else:
            print('Failed to get reading from the DH11 sensor....')
        return humidity,temperature;
    except KeyboardInterrupt:
        print("Flow Line :  Measurement stopped by User")
    except:
        print("Flow Line :  error occurred!")
    finally:
        print("Flow Line :  Checking Temperature & Humidity Complected..")



#if __name__ == "__main__":
#    var1,var2 = humidity_temperature(18)
#    print(var1,var2)

    