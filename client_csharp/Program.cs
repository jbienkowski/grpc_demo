using gRPC.Helpers;
using System;
using System.Linq;

namespace gRPC
{
    class Program
    {
        private static string _srvAddress = "http://127.0.0.1:50051";
        static void Main(string[] args)
        {
            if (args.Length == 0)
            {
                Console.WriteLine("No arguments provided. Please run the program with --help parameter to see the possibilities");
                return;
            }

            if (args[0] == "--help")
            {
                printHelp();
                return;
            }

            if (args[0] == "--ping")
            {
                ping();
                return;
            }

            if (args[0] == "--past")
            {
                short daysBack = short.Parse(args[1]);
                past(daysBack);
                return;
            }

            if (args[0] == "--day")
            {
                short y = short.Parse(args[1]);
                short m = short.Parse(args[2]);
                short d = short.Parse(args[3]);
                day(y, m, d);
                return;
            }

            Console.WriteLine("No known arguments provided. Please run the program with --help parameter to see the possibilities");
        }

        static void ping()
        {
            var _grpcHelper = new GrpcHelper(_srvAddress);
            var _pingMsg = _grpcHelper.PingServer();
            Console.WriteLine(_pingMsg);
        }

        static void past(short daysBack)
        {
            var _grpcHelper = new GrpcHelper(_srvAddress);
            var _pingMsg = _grpcHelper.GetPast(daysBack);
            Console.WriteLine(_pingMsg);
        }

        static void day(short year, short month, short day)
        {
            var _grpcHelper = new GrpcHelper(_srvAddress);
            var _pingMsg = _grpcHelper.GetDay(year, month, day);
            Console.WriteLine(_pingMsg);
        }

        static void printHelp()
        {
            Console.WriteLine("----------------------");
            Console.WriteLine("To ping the server:");
            Console.WriteLine("dotnet gRPC.dll --ping");
            Console.WriteLine("----------------------");
            Console.WriteLine("To get biggest seismic event in past X days:");
            Console.WriteLine("dotnet gRPC.dll --past X");
            Console.WriteLine("----------------------");
            Console.WriteLine("To get biggest seismic event on given day:");
            Console.WriteLine("dotnet gRPC.dll --day YYYY-MM-DD");
            Console.WriteLine("----------------------");
        }
    }
}
