using System;
using Grpc.Net.Client;
using SeismoSrv;

namespace gRPC.Helpers
{
    class GrpcHelper
    {
        public string ServerAddress { get; private set; }

        public GrpcHelper(string serverAddress)
        {
            ServerAddress = serverAddress;
        }

        public string PingServer()
        {
            /*
            Additional configuration is required to call insecure gRPC services with the .NET Core client.
            The gRPC client must set the System.Net.Http.SocketsHttpHandler.Http2UnencryptedSupport
            switch to true and use http in the server address:
            */
            AppContext.SetSwitch("System.Net.Http.SocketsHttpHandler.Http2UnencryptedSupport", true);
            var channel = GrpcChannel.ForAddress(ServerAddress);
            var client = new SeismoService.SeismoServiceClient(channel);
            var request = new SeismoPingRequest();
            request.Name = "C# Client";
            var reply = client.SeismoPing(request);
            return reply.Message;
        }

        public string GetPast(short daysBack)
        {
            /*
            Additional configuration is required to call insecure gRPC services with the .NET Core client.
            The gRPC client must set the System.Net.Http.SocketsHttpHandler.Http2UnencryptedSupport
            switch to true and use http in the server address:
            */
            AppContext.SetSwitch("System.Net.Http.SocketsHttpHandler.Http2UnencryptedSupport", true);
            var channel = GrpcChannel.ForAddress(ServerAddress);
            var client = new SeismoService.SeismoServiceClient(channel);
            var request = new BiggestEventInDaysRequest();
            request.Days = daysBack;
            var reply = client.BiggestEventInDays(request);
            return $"Biggest event in last {daysBack} days had magnitude of {reply.Magnitude}, latitude {reply.Latitude} and longitude {reply.Longitude}";
        }

        public string GetDay(short year, short month, short day)
        {
            /*
            Additional configuration is required to call insecure gRPC services with the .NET Core client.
            The gRPC client must set the System.Net.Http.SocketsHttpHandler.Http2UnencryptedSupport
            switch to true and use http in the server address:
            */
            AppContext.SetSwitch("System.Net.Http.SocketsHttpHandler.Http2UnencryptedSupport", true);
            var channel = GrpcChannel.ForAddress(ServerAddress);
            var client = new SeismoService.SeismoServiceClient(channel);
            var request = new BiggestEventOnRequest();
            request.Year = year;
            request.Month = month;
            request.Day = day;
            var reply = client.BiggestEventOn(request);
            return $"Biggest event on {year}-{month}-{day} had magnitude of {reply.Magnitude}, latitude {reply.Latitude} and longitude {reply.Longitude}";
        }
    }
}
