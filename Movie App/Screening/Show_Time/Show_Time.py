from nameko.rpc import rpc


class Show_Time:
    name = 'show_time_service'

    @rpc
    def get(self, name):
        return(f'Movie Name: {name}')

    @rpc
    def put(self, name, times):
        return (f'Add movie {name}, completed!')
