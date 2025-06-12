import rfcontrol_pb2   
import rfcontrol_pb2_grpc  
import time
import grpc

# Function to get client stream requests for Bulk RF Settings
def get_client_stream_requests():
    while True:
        frequency = input("Please enter frequency (or nothing to stop chatting): ")
        if frequency == "":
            break

        gain = input("Please enter gain: ")
        device_id = input("Please enter device ID: ")

        rf_config = rfcontrol_pb2.RFConfig(frequency=frequency, gain=gain, device_id=device_id)
        yield rf_config
        time.sleep(1)

def run():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = rfcontrol_pb2_grpc.RFControlStub(channel)

        print("1. SetRFSettings - Unary RPC")
        print("2. MonitorDeviceStatus - Server Side Streaming RPC")
        print("3. BulkSetRFSettings - Client Side Streaming RPC")
        print("4. InteractingRFControl - Both Streaming RPC")
        rpc_call = input("Which rpc would you like to make: ")

        if rpc_call == "1":
            
            frequency = input("Enter frequency (Hz): ")
            gain = input("Enter gain (dB): ")
            device_id = input("Enter device ID: ")

            rf_config = rfcontrol_pb2.RFConfig(frequency=frequency, gain=gain, device_id=device_id)
            rf_response = stub.SetRFSettings(rf_config)
            print("SetRFSettings Response Received:")
            print(rf_response)
        
        elif rpc_call == "2":
            
            device_id = input("Enter device ID to monitor: ")
            request = rfcontrol_pb2.DeviceStatusRequest(device_id=device_id)
            status_replies = stub.MonitorDeviceStatus(request)

            for status_reply in status_replies:
                print("MonitorDeviceStatus Response Received:")
                print(status_reply)

        elif rpc_call == "3":
            
            delayed_reply = stub.BulkSetRFSettings(get_client_stream_requests())
            print("BulkSetRFSettings Response Received:")
            print(delayed_reply)

        elif rpc_call == "4":
           
            responses = stub.InteractingRFControl(get_client_stream_requests())

            for response in responses:
                print("InteractingRFControl Response Received:")
                print(response)

if __name__ == "__main__":
    run()
