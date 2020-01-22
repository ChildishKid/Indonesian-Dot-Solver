from spaces.action_space import ActionSpace

dimension = 4

action_space = ActionSpace(dimension=dimension)

for i in range(dimension**2):
    print(action_space.sample(i))
