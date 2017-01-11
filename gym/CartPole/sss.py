import logging
import gym
from gym import wrappers

from CartPole.Solved import SolvedAgent

def main():

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    env = gym.make('CartPole-v0')
    agent = SolvedAgent()

    outdir = '/tmp/' + agent.name + '-results'
    env = wrappers.Monitor(env, outdir, force=True)

    episode_count = 200
    max_steps = 200
    reward = 0
    done = False

    for i in range(episode_count):
        ob = env.reset()

        for j in range(max_steps):
            action = agent.act(ob, reward, done)
            ob, reward, done, _ = env.step(action)
            if done:
                break

    env.monitor.close()

if __name__ == '__main__':
    main()
