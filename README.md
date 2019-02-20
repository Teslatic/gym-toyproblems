# gym-toyproblems
Streamlined openAi environments for toyproblems:
  - Cartpole
  - Pendulum
  - Acrobot

Setup:
1. clone repo to desired location
2. ``` cd gym-toyproblems/ ```
3. ``` pip install -e .```

Import in python script:

```
import gym
import gym_toyproblems
```

References:
General: https://github.com/openai/gym/tree/master/gym/envs
Example repo: https://github.com/openai/gym-soccer

Deinstallation:
```
pip uninstall gym-toyproblems
```

Also remove egg info directory in cloned repository (was created during installation)
```
rm -rf gym_toyproblems.egg-info/
```
