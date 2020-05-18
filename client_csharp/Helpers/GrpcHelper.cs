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
            var channel = GrpcChannel.ForAddress(ServerAddress);
            var client = new SeismoService.SeismoServiceClient(channel);
            var reply = client.SeismoPing(new SeismoPingRequest() { Name = "C# Client" });
            return reply.Message;
        }
    }
}
