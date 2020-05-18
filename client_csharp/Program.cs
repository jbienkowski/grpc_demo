using gRPC.Helpers;
using System;

namespace gRPC
{
    class Program
    {
        private static string _srvAddress = "127.0.0.1:50051";

        static void Main(string[] args)
        {
            var _grpcHelper = new GrpcHelper(_srvAddress);
            var _pingMsg = _grpcHelper.PingServer();
            Console.WriteLine(_pingMsg);
        }
    }
}
