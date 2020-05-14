import random 
from utils import Queue, Stack, Graph

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

  
    def populate_graph(self, num_users, avg_friendships):
        # Reset graph, last_id updates and increments by 1 everytime a user is generated
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i}")
        # Create Friendships
        # Generate all possible friendship combinations and save inside a list(possible_friendships)
        possible_friendships = []
        # Avoid duplicates by ensuring the first number is smaller than the second
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                # append tuple to possible_friendships
                possible_friendships.append((user_id, friend_id))
        # Shuffle the possible friendships
        random.shuffle(possible_friendships)
        # Create friendships for the first X pairs of the list
        # X is determined by the formula: num_users * avg_friendships // 2
        # Need to divide by 2 since each add_friendship() creates 2 friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # start a Queue for a breadthfirst approach to check all connections
        qq = Queue()
        visited = {} # a dictionary not a set
        # empty list with our user as the starting point
        path = [user_id]
        
        # load the path to back of the Queue
        qq.enqueue(path)
        
        while qq.size() > 0:
            # set the path removed from the FRONT of the Queue as the path
            path = qq.dequeue()
            # set  last item in the path which is a list as cur_id
            cur_id = path[-1]

            if cur_id not in visited:
                # set frienships as the value at friendships indexed at cur_id
                friendships = self.friendships[cur_id]
                visited[cur_id] = path
                
                for friend_id in friendships:
                    new_path = list(path) #copy of path
                    new_path.append(friend_id)
                    # add to back of queue and continues the while loop
                    qq.enqueue(new_path)

             
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(5, 3)
    print('friendships:',sg.friendships)
    connections = sg.get_all_social_paths(1)
    print('connections:',connections)
