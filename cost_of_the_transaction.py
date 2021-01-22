"""
Depth first search
https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
"""

class Station:

    def __init__(self, value, power_loss=None, adj=None):
        self.value = value
        self.adj = adj
        self.power_loss = power_loss

        if self.adj is None:
            self.adj = {}


class Configuration:

    def __init__(self):
        self.stations = {}

    def build_connections(self, origin, destination):
        if destination not in self.stations[origin].adj:
            self.stations[origin].adj[destination] = destination
            self.stations[destination].adj[origin] = origin

    def insert_power_loss(self):
        for s in self.stations:
            loss = input(f"Type power loss to station{s}: ")
            self.stations[s].power_loss = loss

    def create_stations(self, n):
        for s in range(n):
            station = input("Type station and connection: ")
            origin, destination = station.split(",")

            origin = int(origin)
            destination = int(destination)

            if origin not in self.stations:
                self.stations[origin] = Station(value=origin)

            if destination not in self.stations:
                self.stations[destination] = Station(value=destination)

            self.build_connections(origin, destination)

        return self.stations


class Request:

    def __init__(self, n_requests, stations):
        self.stations = stations
        self.n_requests = n_requests
        self.requests = []

    def make_request(self):
        for r in range(self.n_requests):
            command = input(f"Type the stations and the power lost expected number {r}: ")
            self.requests.append(command)

    def return_result(self):
        for r in self.requests:
            origin, destination, exp_power_loss = r.split(",")
            origin = int(origin)
            destination = int(destination)
            exp_power_loss = float(exp_power_loss)
            self.check_connections_and_get_power_loss(origin=origin,
                                                      destination=destination,
                                                      current_station=origin,
                                                      exp_power_loss=exp_power_loss,
                                                      visited=[],
                                                      p_loss=0)

    def check_connections_and_get_power_loss(self, origin, destination, current_station, exp_power_loss, visited, p_loss):
        if current_station in visited:
            return 0

        visited.append(current_station)

        if current_station == destination:
            return self.stations[destination].power_loss

        if not self.stations[current_station].adj:
            return 0

        for s in self.stations[origin].adj:
            p_loss += self.check_connections_and_get_power_loss(origin,
                                                            destination,
                                                            s,
                                                            exp_power_loss,
                                                            visited,
                                                            p_loss)

        if current_station == origin:
            if exp_power_loss > p_loss:
                print("REJECTED")
            else:
                print("APPROVED")

        return self.stations[current_station].power_loss


def init_function():
    print("======Lets make the configuration of stations======")
    n_stations = int(input("How much stations"))
    configuration = Configuration()
    configuration.create_stations(n_stations)
    configuration.insert_power_loss()
    print("======Ok, great job, now we'll start the request of transfer power=====")
    n_requests = int(input("How much requests will you do?: "))
    request = Request(n_requests=n_requests, stations=configuration.stations)
    request.make_request()
    request.return_result()


if __name__ == "__main__":
    init_function()
