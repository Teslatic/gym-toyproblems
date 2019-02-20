from gym.envs.registration import register

register(
    id='gym-toy-cartpole-v0',
    entry_point='gym_toyproblems.envs:Cartpole')

register(
    id='gym-toy-pendulum-v0',
    entry_point='gym_toyproblems.envs:Pendulum')

register(
    id='gym-toy-acrobot-v0',
    entry_point='gym_toyproblems.envs:Acrobot')
