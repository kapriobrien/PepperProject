#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Use say Method"""

import qi
import argparse
import sys
import ballin

def main(session):
    """
    This example uses the say method.
    It makes the robot say some text using the module.
    """
    # Get the service ALTextToSpeech.
    tts = session.service("ALTextToSpeech")
    postureService = session.service("ALRobotPosture")

    card1 = ballin.drawCard()
    card2 = ballin.drawCard()

    tts.say("Your cards are " + card1 + " and " + card2)
    tts.say("Would you like to hit?")
    

    postureService.goToPosture("StandZero", 1.0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="172.18.5.223",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)