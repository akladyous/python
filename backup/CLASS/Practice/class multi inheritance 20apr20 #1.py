class clients:
    def __init__(self, client):
        self.client = client

class ethnicities:
    def __init__(self, ethnicity):
        self.ethnicity = ethnicity

class destinations(clients, ethnicities):
    def __init__(self, client, ethnicity, destination):
        clients.__init__(self, client)
        ethnicities.__init__(self, ethnicity)
        self.destination = destination

c1=destinations('paolo','italia','milano')

print(c1.client, c1.ethnicity, c1.destination)
print(clients.__mro__)
print(ethnicities.__mro__)
print(destinations.__mro__)