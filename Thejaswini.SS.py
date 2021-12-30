import speedtest
st=speedtest.Speedtest()
option=int(input("what speed do you want to test:
1)Download speed
2)upload speed
3)ping
your choice:"))
if option == 1:
    print(st.download())
    elif option == 2:
        print(st.upload())
        elif option == 3:
            servernames=[]
            st.get_servers(servernames)
            print(st.results.ping())
            else:
                print("pls enter the correct choice !")
        
