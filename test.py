from pettingzoo.mpe import simple_push_v3
env = simple_push_v3.env(max_cycles=5, continuous_actions=False)

env.reset()
i = 0
for agent in env.agent_iter():
    obs, reward, termination, truncaction, info = env.last()
    print("agent{}obs:{}".format(i, obs))
    action = env.action_space(agent).sample()
    env.step(action)
    i += 1

