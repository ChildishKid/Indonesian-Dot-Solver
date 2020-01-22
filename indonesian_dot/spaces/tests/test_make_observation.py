from spaces.observation_space import ObservationSpace

state = "1100111011111111"

observe = ObservationSpace(state=state)
print(observe.sample())
