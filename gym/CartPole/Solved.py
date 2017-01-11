class SolvedAgent(object):
    def __init__(self):
        self.name = 'solved'

    def act(self, observation, reward, done):

        # Guesses at observations are:
        # observation[0] = pole speed
        # observation[1] = pole top pos
        # observation[2] = pole angle
        # observation[3] = block speed

        if (observation[2] > 0 and observation[3] > -1) or observation[3] > 1:
            return 1

        return 0