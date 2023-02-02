import speedtest

speed = speedtest.Speedtest()

def Test():
    while True:
        print('\a')
        choice = int(input("""Check your internet connection...
        1)Download Speed
        2)Upload Speed
        3)Exit
        Choice >>> """))
        print('\a')

        if choice == 1:
            print("testing your dowload speed...")
            print(f"your download speed: { '{:.2f}'.format(speed.download()/1024/1024)} Mb/s")
        elif choice == 2:
            print("testing your upload speed...")
            print(f"your upload speed: {'{:.2f}'.format(speed.upload()/1024/1024)} Mb/s")
        elif choice == 3:
            print("exit")
            break
        else:
            print("error, please try again")

Test()
#neganwashere


