def ToxicGasDectection():
    print("Flow Line :  Toxic Gas Dectection ........")
    try:
        ToxicGas="No"
        print("Flow Line :  MQ-2 Value get")
        return ToxicGas;
    except KeyboardInterrupt:
        print("Flow Line :  MQ-2 Measurement stopped by User")
    except:
        print("Flow Line :  error occurred!")
    finally:
        print("Flow Line :  Toxic Gas Dectection Complected..")
        
#if __name__ == "__main__":
#    var1 = ToxicGasDectection();
#    print(var1)