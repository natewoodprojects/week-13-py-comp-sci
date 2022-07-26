class Node():
    """Node in a graph representing a person."""

    def __init__(self, name, adjacent=None):
        """Create a person node with friends adjacent"""

        if adjacent is None:
            adjacent = set()

        assert isinstance(adjacent, set), \
            "adjacent must be a set!"

        self.name = name
        self.adjacent = adjacent

    def __repr__(self):
        """Debugging-friendly representation"""

        return f"<Node: {self.name}>"


class FriendGraph():
    """Graph holding people and their friendships."""

    def __init__(self):
        """Create an empty graph"""

        self.nodes = set()

    def __repr__(self):
        return f"<FriendGraph: { {n.name for n in self.nodes} }>"

    def add_person(self, person):
        """Add a person to our graph"""

        self.nodes.add(person)

    def set_friends(self, person1, person2):
        """Set two people as friends"""

        person1.adjacent.add(person2)
        person2.adjacent.add(person1)

    def add_people(self, people_list):
        """Add a list of people to our graph"""

        for person in people_list:
            self.add_person(person)

    def are_connected(self, person1, person2):
        """Are two people connected? Breadth-first search."""

        possible_nodes = Queue()
        seen = set()
        possible_nodes.enqueue(person1)
        seen.add(person1)

        while not possible_nodes.is_empty():
            person = possible_nodes.dequeue()
            print("checking", person)
            if person is person2:
                return True
            else:
                for friend in person.adjacent - seen:
                    possible_nodes.enqueue(friend)
                    seen.add(friend)
                    print("added to queue:", friend)
        return False

def make_simple_friendship(name1, name2, name3):
    first = Node(name1)
    second = Node(name2)
    third = Node(name3)
    click = FriendGraph()
    click.set_friends(first, second)
    click.set_friends(second, third)
    return 


harry = Node("Harry")
hermione = Node("Hermione")
ron = Node("Ron")
neville = Node("Neville")
trevor = Node("Trevor")
fred = Node("Fred")
draco = Node("Draco")
crabbe = Node("Crabbe")
goyle = Node("Goyle")

friends = FriendGraph()
friends.add_people([harry, hermione, ron, neville, fred, draco, crabbe, goyle])

friends.set_friends(harry, hermione)
friends.set_friends(harry, ron)
friends.set_friends(harry, neville)
friends.set_friends(hermione, ron)
friends.set_friends(neville, hermione)
friends.set_friends(neville, trevor)
friends.set_friends(ron, fred)
friends.set_friends(draco, crabbe)
friends.set_friends(draco, goyle)

print(friends)