import io
import sys

from sakordekar_mangesh.TrafficSimulator import *

if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            filename = sys.argv[1]
            input = "".join(open(filename, "r").readlines())
            sys.stdin = io.StringIO(input)
        else:
            name = input("Input file for redirection (c for none):")
            if name.upper() != 'C':
                input = "".join( open( name, "r" ).readlines( ) )
                sys.stdin = io.StringIO( input )


    except:
        print("could not find text file from command line....continuing with console input")

    s = Simulator()