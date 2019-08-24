#!/usr/bin/env python

## Native library, does not need to be included at runtime
import json

## As specified in ./requirements.txt
import requests


def main( event, context ):
    """
            This largely does nothing with
        events or contexts, merely returns
        a remote resource from a non-provided
        library.
    """
    
    response = requests.get("http://rawr.sh/stuff.json")

    if response.status_code == 200:
        return json.dumps( response.json() )



if __name__ == '__main__':
    print( "Triggering event on localhost" )
    main('','')

