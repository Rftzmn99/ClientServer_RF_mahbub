# gRPC Client-Server Communication

## Introduction

This project involves the implementation of a **gRPC server** using **Python**, designed to interact with client applications. The server is capable of receiving and responding to requests via gRPC, and it handles various functionalities, such as setting **RF settings** (frequency, gain) and providing **device status** responses.

This document will guide you through the steps of setting up, deploying, and testing the server and client. Dockerization is included as part of the procedure but will not be used directly for deployment in this particular setup.

## Prerequisites

Before setting up the project, ensure that the following tools are installed:

- **Python 3.11+**
- **pip** (Python's package installer)
- **gRPC** tools for Python (for creating server and client communication)
- **Docker Desktop** or **Google Cloud Platform**, **AWS**, **Azure**, or any cloud provider (if deploying remotely)

## Project Structure

The project is organized as follows:

```
/ClientSserver_RF_mahbub
  /server
    server.py              # gRPC server code
  /client
    client.py              # gRPC client code
  Dockerfile               # Docker configuration (if      Dockerized)
  docker-compose.yml       # Docker Compose configuration (if using multiple services)
  requirements.txt         # Python dependencies
  README.md                # Project documentation

```

## Installation Steps

1. **Clone the Repository**:
   If you haven’t cloned the repository yet, do so by running:

   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Install Python Dependencies**:
   Navigate to the project directory and install the necessary Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up gRPC Server and Client**:

   - The **server.py** file contains the implementation of the gRPC server that handles requests such as setting **RF settings** and providing **device status**.
   - The **client.py** file sends requests to the server and handles responses.

4. **Run the Server**:
   Start the gRPC server by running:

   ```bash
   python server/server.py
   ```

5. **Run the Client**:
   The client sends requests to the server. Run the client:
   ```bash
   python client/client.py
   ```

## Dockerization (for Documentation Purpose)

### Dockerfile

For containerization, a **Dockerfile** has been created to build and run the **gRPC server** in a Docker container. (I have created a Dockerfile for the project; however, I am currently facing difficulties implementing it).

To run the project inside the docker user can use these command below:

### Docker Commands

1. **Build the Docker Image**:

   ```
   docker build -t grpc-server .
   ```

2. **Run the Docker Container**:
   ```
   docker run -p 50052:50052 grpc-server
   ```

## Testing the gRPC Server

1. **Test Server Locally**:

   - Run the server and client locally by executing `python server.py` and `python client.py` in separate terminals.
   - The client will communicate with the server over port `50052`.

2. **Outputs**:  
   **The RF control service definition**  
   **Unary (Request-Response)**: SetRFSettings (client sends a single request and gets a single response).

   Client

   ```
   1. SetRFSettings - Unary RPC
   2. MonitorDeviceStatus - Server Side Streaming RPC
   3. BulkSetRFSettings - Client Side Streaming RPC
   4. InteractingRFControl - Both Streaming RPC
   Which rpc would you like to make: 1
   Enter frequency (Hz): 1
   Enter gain (dB): 2
   Enter device ID: 2
   SetRFSettings Response Received:
   status: "Success"
   message: "RF settings applied: Frequency=1, Gain=2"
   ```

   Server

   ```
   Server started on port 50052...
   SetRFSettings Request Made: Frequency=1, Gain=2, Device ID=2
   ```

   **Server Streaming**: MonitorDeviceStatus (client sends a single request and gets multiple responses).

   Client

   ```
   Which rpc would you like to make: 2
   Enter device ID to monitor: 3
   MonitorDeviceStatus Response Received:
   status: "Active"
   message: "Device 3 status update 1"

   MonitorDeviceStatus Response Received:
   status: "Active"
   message: "Device 3 status update 2"

   MonitorDeviceStatus Response Received:
   status: "Active"
   message: "Device 3 status update 3"
   ```

   Server

   ```
   MonitorDeviceStatus Request Made: Device ID=3
   ```

   **Client Streaming**: BulkSetRFSettings (client sends multiple requests and gets a single response).

   Client

   ```
   Which rpc would you like to make: 3
   Please enter frequency (or nothing to stop chatting): 2
   Please enter gain: 2
   Please enter device ID: 1
   Please enter frequency (or nothing to stop chatting): 3
   Please enter gain: 1
   Please enter device ID: 1
   Please enter frequency (or nothing to stop chatting): 1
   Please enter gain: 2
   Please enter device ID: 1
   ```

   Server

   ```
   BulkSetRFSettings Request Made: Frequency=2, Gain=2, Device ID=1
   BulkSetRFSettings Request Made: Frequency=3, Gain=1, Device ID=1
   BulkSetRFSettings Request Made: Frequency=1, Gain=2, Device ID=1
   ```

   **Bidirectional Streaming**: InteractingRFControl (both client and server send and receive a stream of messages).

   Client

   ```
   Which rpc would you like to make: 4
   Please enter frequency (or nothing to stop chatting): 1
   Please enter gain: 2
   Please enter device ID: 3
   InteractingRFControl Response Received:
   status: "Success"
   message: "Processed RF configuration: Frequency=1, Gain=2"

   ```

   Server

   ```
   InteractingRFControl Request Made: Frequency=1, Gain=2, Device ID=3
   ```

## Conclusion

Here is the simple wrapper around powerful gRPC server based on Python and Docker for containerization. The Dockerization step is also optional but certainly very convenient as it opens the door for running the server smooth across different environments. I encountered challenges during the implementation phase, and unfortunately, I was unable to fully integrate Docker as planned.

Despite this, the process has been a valuable learning experience, helping me improve my skills in gRPC communication, Python development, and containerization. The project is functional and demonstrates key concepts, but the Docker integration remains a work in progress. I look forward to revisiting and refining the Docker setup in future iterations.
