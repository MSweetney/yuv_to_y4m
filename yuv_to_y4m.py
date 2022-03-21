import os
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='This script converts yuv input to y4m output')
    parser.add_argument('-o', type=str, help='Specify output yuv file path.')
    parser.add_argument('-i', type=str, help='Specify input y4m file path.')
    parser.add_argument('-w', type=str, help='Specify width')
    # FLAG 'e' PLEASE NOTICE!
    parser.add_argument('-e', type=str, help='Specify height')
    parser.add_argument('-n', type=str, help='Specify numerator of framerate')
    parser.add_argument('-d', type=str,
                        help='Specify denominator of framerate')
    parser.add_argument('-f', type=str, help='Specify interlacing type')
    parser.add_argument('-C', type=str, help='Specify colour space')
    args = parser.parse_args()

    if args.i is None:
        print("input file must be provided")

    if args.o is None:
        print("Output file must be provided")

    # open out file
    out_file = open(args.o, 'wb')
    in_file = open(args.i, 'rb')

    # write header
    header = f"YUV4MPEG2 W{args.w} H{args.e} F{args.n}:{args.d} {args.f} A0:0 C{args.C}\n".encode()
    out_file.write(header)

    if args.C[:3] == '420':
        framesize = int(args.w) * int(args.e) * 3 / 2
    elif args.C[:3] == '422':
        framesize = int(args.w) * int(args.e) * 2
    elif args.C[:3] == '444':
        framesize = int(args.w) * int(args.e) * 3

    for _ in range(int(os.path.getsize(args.i) / framesize)):
        frame = in_file.read(int(framesize))
        out_file.write(b'FRAME\n')
        out_file.write(frame)

    in_file.close()
    out_file.close()
