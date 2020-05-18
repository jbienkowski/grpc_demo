using gRPC.Helpers;
using System;

namespace gRPC
{
    class Program
    {
        private static string _srvAddress = "http://127.0.0.1:50051";
        static void Main(string[] args)
        {
            /*
            Additional configuration is required to call insecure gRPC services with the .NET Core client.
            The gRPC client must set the System.Net.Http.SocketsHttpHandler.Http2UnencryptedSupport
            switch to true and use http in the server address:
            */
            AppContext.SetSwitch("System.Net.Http.SocketsHttpHandler.Http2UnencryptedSupport", true);
            var _grpcHelper = new GrpcHelper(_srvAddress);
            var _pingMsg = _grpcHelper.PingServer();
            Console.WriteLine(_pingMsg);
        }
    }
}
