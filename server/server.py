from concurrent import futures
import time

import grpc
import rfcontrol_pb2   
import rfcontrol_pb2_grpc  

class RFControlServicer(rfcontrol_pb2_grpc.RFControlServicer):
    
    def SetRFSettings(self, request, context):
        """Unary RPC to set RF settings."""
        print(f"SetRFSettings Request Made: Frequency={request.frequency}, Gain={request.gain}, Device ID={request.device_id}")
        response = rfcontrol_pb2.RFResponse()
        response.status = "Success"
        response.message = f"RF settings applied: Frequency={request.frequency}, Gain={request.gain}"
        return response
    
    def MonitorDeviceStatus(self, request, context):
        """Server Streaming RPC to monitor device status."""
        print(f"MonitorDeviceStatus Request Made: Device ID={request.device_id}")
        
       
        for i in range(3):
            status_reply = rfcontrol_pb2.DeviceStatusReply()
            status_reply.status = "Active" 
            status_reply.message = f"Device {request.device_id} status update {i + 1}"
            yield status_reply
            time.sleep(2) 

    def BulkSetRFSettings(self, request_iterator, context):
        """Client Streaming RPC for bulk setting of RF configurations."""
        delayed_reply = rfcontrol_pb2.DelayedResponse()
        for request in request_iterator:
            print(f"BulkSetRFSettings Request Made: Frequency={request.frequency}, Gain={request.gain}, Device ID={request.device_id}")
            delayed_reply.request.append(request)

        delayed_reply.message = f"Received {len(delayed_reply.request)} RF configuration requests. Delayed response provided."
        return delayed_reply

    def InteractingRFControl(self, request_iterator, context):
        """Bi-directional Streaming RPC for continuous interaction."""
        for request in request_iterator:
            print(f"InteractingRFControl Request Made: Frequency={request.frequency}, Gain={request.gain}, Device ID={request.device_id}")
            
            response = rfcontrol_pb2.RFResponse()
            response.status = "Success"
            response.message = f"Processed RF configuration: Frequency={request.frequency}, Gain={request.gain}"
            yield response  

def serve():
    """Start the server to handle incoming requests."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rfcontrol_pb2_grpc.add_RFControlServicer_to_server(RFControlServicer(), server)
    server.add_insecure_port("localhost:50052")
    print("Server started on port 50052...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
