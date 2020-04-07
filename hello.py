from nameko.rpc import rpc
from time import sleep

class GreetingService:
    name = "greeting_service"

    @rpc
    def hello(self, name):
        sleep(5)
        return "Hello, {}!".format(name)
