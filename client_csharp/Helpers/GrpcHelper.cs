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
            var request = new SeismoPingRequest();
            request.Name = "C# Client";
            var reply = client.SeismoPing(request);
            return reply.Message;
        }
    }
}
