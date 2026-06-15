from services.database import client

try:
    print(client.server_info())
    print("CONNECTED SUCCESSFULLY")

except Exception as e:
    print("ERROR:")
    print(e)