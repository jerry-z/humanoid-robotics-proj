"""
<<<<<<< HEAD
import distutils.version
import logging
import os
import sys
sys.path.append("..")

from gym import error
from gym.configuration import logger_setup, undo_logger_setup
from gym.utils import reraise
from gym.version import VERSION as __version__

logger = logging.getLogger(__name__)

# Do this before importing any other gym modules, as most of them import some
# dependencies themselves.
def sanity_check_dependencies():
    import numpy
    import requests
    import six

    if distutils.version.LooseVersion(numpy.__version__) < distutils.version.LooseVersion('1.10.4'):
        logger.warn("You have 'numpy' version %s installed, but 'gym' requires at least 1.10.4. HINT: upgrade via 'pip install -U numpy'.", numpy.__version__)

    if distutils.version.LooseVersion(requests.__version__) < distutils.version.LooseVersion('2.0'):
        logger.warn("You have 'requests' version %s installed, but 'gym' requires at least 2.0. HINT: upgrade via 'pip install -U requests'.", requests.__version__)

# We automatically configure a logger with a simple stderr handler. If
# you'd rather customize logging yourself, run undo_logger_setup.
#
# (Note: this code runs before importing the rest of gym, since we may
# print a warning at load time.)
#
# It's generally not best practice to configure the logger in a
# library. We choose to do so because, empirically, many of our users
# are unfamiliar with Python's logging configuration, and never find
# their way to enabling our logging. Users who are aware of how to
# configure Python's logging do have to accept a bit of incovenience
# (generally by caling `gym.undo_logger_setup()`), but in exchange,
# the library becomes much more usable for the uninitiated.
#
# Gym's design goal generally is to be simple and intuitive, and while
# the tradeoff is definitely not obvious in this case, we've come down
# on the side of auto-configuring the logger.

if not os.environ.get('GYM_NO_LOGGER_SETUP'):
    logger_setup()
del logger_setup

sanity_check_dependencies()

from gym.core import Env, GoalEnv, Space, Wrapper, ObservationWrapper, ActionWrapper, RewardWrapper
from gym.benchmarks import benchmark_spec
from gym.envs import make, spec
from gym.scoreboard.api import upload
from gym import wrappers


__all__ = ["Env", "Space", "Wrapper", "make", "spec", "upload", "wrappers"]
"""
#=======
from gym.envs.registration import registry, register, make, spec

# Algorithmic
# ----------------------------------------

register(
    id='Copy-v0',
    entry_point='gym.envs.algorithmic:CopyEnv',
    max_episode_steps=200,
    reward_threshold=25.0,
)

register(
    id='RepeatCopy-v0',
    entry_point='gym.envs.algorithmic:RepeatCopyEnv',
    max_episode_steps=200,
    reward_threshold=75.0,
)

register(
    id='ReversedAddition-v0',
    entry_point='gym.envs.algorithmic:ReversedAdditionEnv',
    kwargs={'rows' : 2},
    max_episode_steps=200,
    reward_threshold=25.0,
)

register(
    id='ReversedAddition3-v0',
    entry_point='gym.envs.algorithmic:ReversedAdditionEnv',
    kwargs={'rows' : 3},
    max_episode_steps=200,
    reward_threshold=25.0,
)

register(
    id='DuplicatedInput-v0',
    entry_point='gym.envs.algorithmic:DuplicatedInputEnv',
    max_episode_steps=200,
    reward_threshold=9.0,
)

register(
    id='Reverse-v0',
    entry_point='gym.envs.algorithmic:ReverseEnv',
    max_episode_steps=200,
    reward_threshold=25.0,
)

# Classic
# ----------------------------------------
register(
    id='Ball-v0',
    entry_point='gym.envs.classic_control:BallContEnv',
    max_episode_steps=200,
)

register(
    id='CartPole-v0',
    entry_point='gym.envs.classic_control:CartPoleEnv',
    max_episode_steps=200,
    reward_threshold=195.0,
)

register(
    id='CartPoleCont-v0',
    entry_point='gym.envs.classic_control:CartPoleContEnv',
    max_episode_steps=200,
    reward_threshold=195.0,
)

register(
    id='CartPole-v1',
    entry_point='gym.envs.classic_control:CartPoleEnv',
    max_episode_steps=500,
    reward_threshold=475.0,
)

register(
    id='CartPoleCont-v1',
    entry_point='gym.envs.classic_control:CartPoleContEnv',
    max_episode_steps=500,
    reward_threshold=475.0,
)

register(
    id='MountainCar-v0',
    entry_point='gym.envs.classic_control:MountainCarEnv',
    max_episode_steps=200,
    reward_threshold=-110.0,
)

register(
    id='MountainCarCont-v0',
    entry_point='gym.envs.classic_control:MountainCarContEnv',
    max_episode_steps=200,
    reward_threshold=-110.0,
)

register(
    id='MountainCarContinuous-v0',
    entry_point='gym.envs.classic_control:Continuous_MountainCarEnv',
    max_episode_steps=999,
    reward_threshold=90.0,
)

register(
    id='Pendulum-v0',
    entry_point='gym.envs.classic_control:PendulumEnv',
    max_episode_steps=200,
)

register(
    id='Acrobot-v1',
    entry_point='gym.envs.classic_control:AcrobotEnv',
    max_episode_steps=500,
)

register(
    id='AcrobotCont-v1',
    entry_point='gym.envs.classic_control:AcrobotContEnv',
    max_episode_steps=500,
)

# Box2d
# ----------------------------------------

register(
    id='LunarLander-v2',
    entry_point='gym.envs.box2d:LunarLander',
    max_episode_steps=1000,
    reward_threshold=200,
)

register(
    id='LunarLanderContinuous-v2',
    entry_point='gym.envs.box2d:LunarLanderContinuous',
    max_episode_steps=1000,
    reward_threshold=200,
)

register(
    id='BipedalWalker-v2',
    entry_point='gym.envs.box2d:BipedalWalker',
    max_episode_steps=1600,
    reward_threshold=300,
)

register(
    id='BipedalWalkerHardcore-v2',
    entry_point='gym.envs.box2d:BipedalWalkerHardcore',
    max_episode_steps=2000,
    reward_threshold=300,
)

register(
    id='CarRacing-v0',
    entry_point='gym.envs.box2d:CarRacing',
    max_episode_steps=1000,
    reward_threshold=900,
)

# Toy Text
# ----------------------------------------

register(
    id='Blackjack-v0',
    entry_point='gym.envs.toy_text:BlackjackEnv',
)

register(
    id='KellyCoinflip-v0',
    entry_point='gym.envs.toy_text:KellyCoinflipEnv',
    reward_threshold=246.61,
)
register(
    id='KellyCoinflipGeneralized-v0',
    entry_point='gym.envs.toy_text:KellyCoinflipGeneralizedEnv',
)

register(
    id='FrozenLake-v0',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name' : '4x4'},
    max_episode_steps=100,
    reward_threshold=0.78, # optimum = .8196
)

register(
    id='FrozenLake8x8-v0',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name' : '8x8'},
    max_episode_steps=200,
    reward_threshold=0.99, # optimum = 1
)

register(
    id='CliffWalking-v0',
    entry_point='gym.envs.toy_text:CliffWalkingEnv',
)

register(
    id='NChain-v0',
    entry_point='gym.envs.toy_text:NChainEnv',
    max_episode_steps=1000,
)

register(
    id='Roulette-v0',
    entry_point='gym.envs.toy_text:RouletteEnv',
    max_episode_steps=100,
)

register(
    id='Taxi-v2',
    entry_point='gym.envs.toy_text.taxi:TaxiEnv',
    reward_threshold=8, # optimum = 8.46
    max_episode_steps=200,
)

register(
    id='GuessingGame-v0',
    entry_point='gym.envs.toy_text.guessing_game:GuessingGame',
    max_episode_steps=200,
)

register(
    id='HotterColder-v0',
    entry_point='gym.envs.toy_text.hotter_colder:HotterColder',
    max_episode_steps=200,
)

# Mujoco
# ----------------------------------------

# 2D

register(
    id='Reacher-v1',
    entry_point='gym.envs.mujoco:ReacherEnv',
    max_episode_steps=50,
    reward_threshold=-3.75,
)

register(
    id='ReacherImage-v1',
    entry_point='gym.envs.mujoco:ReacherImageEnv',
    max_episode_steps=50,
    reward_threshold=-3.75,
)

register(
    id='ReacherLong-v1',
    entry_point='gym.envs.mujoco:ReacherLongEnv',
    max_episode_steps=500,
    reward_threshold=-3.75,
)

register(
    id='ReacherPOMDP-v1',
    entry_point='gym.envs.mujoco:ReacherPOMDPEnv',
    max_episode_steps=50,
    reward_threshold=-3.75,
)

register(
    id='ReacherMultigoal-v1',
    entry_point='gym.envs.mujoco:ReacherMultigoalEnv',
    max_episode_steps=50,
)

register(
    id='Pusher-v0',
    entry_point='gym.envs.mujoco:PusherEnv',
    max_episode_steps=100,
    reward_threshold=0.0,
)

register(
    id='PusherMultigoal-v0',
    entry_point='gym.envs.mujoco:PusherMultigoalEnv',
    max_episode_steps=100,
    #reward_threshold=0.0,
)

register(
    id='PusherMultigoalHard-v0',
    entry_point='gym.envs.mujoco:PusherMultigoalHardEnv',
    max_episode_steps=100,
    #reward_threshold=0.0,
)

register(
    id='Thrower-v0',
    entry_point='gym.envs.mujoco:ThrowerEnv',
    max_episode_steps=100,
    reward_threshold=0.0,
)

register(
    id='ThrowerMultigoal-v0',
    entry_point='gym.envs.mujoco:ThrowerMultigoalEnv',
    max_episode_steps=100,
    #reward_threshold=0.0,
)

register(
    id='Striker-v0',
    entry_point='gym.envs.mujoco:StrikerEnv',
    max_episode_steps=100,
    reward_threshold=0.0,
)

register(
    id='InvertedPendulum-v1',
    entry_point='gym.envs.mujoco:InvertedPendulumEnv',
    max_episode_steps=1000,
    reward_threshold=950.0,
)

register(
    id='InvertedPendulumPOMDP-v1',
    entry_point='gym.envs.mujoco:InvertedPendulumPOMDPEnv',
    max_episode_steps=1000,
    reward_threshold=950.0,
)

register(
    id='InvertedDoublePendulum-v1',
    entry_point='gym.envs.mujoco:InvertedDoublePendulumEnv',
    max_episode_steps=1000,
    reward_threshold=9100.0,
)

register(
    id='InvertedDoublePendulumPOMDP-v1',
    entry_point='gym.envs.mujoco:InvertedDoublePendulumPOMDPEnv',
    max_episode_steps=1000,
    reward_threshold=9100.0,
)

register(
    id='HalfCheetah-v1',
    entry_point='gym.envs.mujoco:HalfCheetahEnv',
    max_episode_steps=1000,
    reward_threshold=4800.0,
)

register(
    id='HalfCheetahRllab-v1',
    entry_point='gym.envs.mujoco:HalfCheetahRllabEnv',
    max_episode_steps=1000,
    reward_threshold=4800.0,
)

register(
    id='HalfCheetahImage-v1',
    entry_point='gym.envs.mujoco:HalfCheetahImageEnv',
    max_episode_steps=1000,
    reward_threshold=4800.0,
)


register(
    id='HalfCheetahPOMDP-v1',
    entry_point='gym.envs.mujoco:HalfCheetahPOMDPEnv',
    max_episode_steps=1000,
    reward_threshold=4800.0,
)

register(
    id='HalfCheetahFinishLine-v1',
    entry_point='gym.envs.mujoco:HalfCheetahFinishLineEnv',
    max_episode_steps=1000,
    #reward_threshold=4800.0,
)

register(
    id='Hopper-v1',
    entry_point='gym.envs.mujoco:HopperEnv',
    max_episode_steps=1000,
    reward_threshold=3800.0,
)

register(
    id='HopperLargeMotor-v1',
    entry_point='gym.envs.mujoco:HopperLargeMotorEnv',
    max_episode_steps=1000,
    reward_threshold=3800.0,
)

register(
    id='HopperImage-v1',
    entry_point='gym.envs.mujoco:HopperImageEnv',
    max_episode_steps=1000,
    reward_threshold=3800.0,
)

register(
    id='HopperPOMDP-v1',
    entry_point='gym.envs.mujoco:HopperPOMDPEnv',
    max_episode_steps=1000,
    reward_threshold=3800.0,
)

register(
    id='Swimmer-v1',
    entry_point='gym.envs.mujoco:SwimmerEnv',
    max_episode_steps=1000,
    reward_threshold=360.0,
)

register(
    id='Swimmer3dRllab-v1',
    entry_point='gym.envs.mujoco:Swimmer3dRllabEnv',
    max_episode_steps=1000,
    reward_threshold=360.0,
)

register(
    id='SwimmerLong-v1',
    entry_point='gym.envs.mujoco:SwimmerLongEnv',
    max_episode_steps=1000,
    reward_threshold=1000.0,
)

register(
    id='SwimmerPOMDP-v1',
    entry_point='gym.envs.mujoco:SwimmerPOMDPEnv',
    max_episode_steps=1000,
    reward_threshold=360.0,
)

register(
    id='SwimmerBandits-v1',
    entry_point='gym.envs.mujoco:SwimmerBanditsEnv',
    max_episode_steps=1000,
)

register(
    id='SwimmerFinishLine-v1',
    entry_point='gym.envs.mujoco:SwimmerFinishLineEnv',
    max_episode_steps=1000,
    #reward_threshold=360.0,
)

register(
    id='Obstacles-v1',
    entry_point='gym.envs.mujoco:Obstacles',
    max_episode_steps=1000,
)

register(
    id='AntBandits-v1',
    entry_point='gym.envs.mujoco:AntBanditsEnv',
    max_episode_steps=1000,
)

register(
    id='AntMovement-v1',
    entry_point='gym.envs.mujoco:AntMovementEnv',
    max_episode_steps=600,
)

register(
    id='AntObstacles-v1',
    entry_point='gym.envs.mujoco:AntObstaclesEnv',
    max_episode_steps=1000,
)

register(
    id='AntObstaclesBig-v1',
    entry_point='gym.envs.mujoco:AntObstaclesBigEnv',
    max_episode_steps=3000,
)

register(
    id='AntObstaclesGen-v1',
    entry_point='gym.envs.mujoco:AntObstaclesGenEnv',
    max_episode_steps=1000,
)

register(
    id='AntFourgoals-v1',
    entry_point='gym.envs.mujoco:AntFourgoalsEnv',
    max_episode_steps=500,
)

register(
    id='AntSmallFourgoals-v1',
    entry_point='gym.envs.mujoco:AntSmallFourgoalsEnv',
    max_episode_steps=500,
)

register(
    id='AntGoalForward-v1',
    entry_point='gym.envs.mujoco:AntGoalForwardEnv',
    max_episode_steps=500,
)

register(
    id='AntGoalUpward-v1',
    entry_point='gym.envs.mujoco:AntGoalUpwardEnv',
    max_episode_steps=500,
)

register(
    id='AntGoalDownward-v1',
    entry_point='gym.envs.mujoco:AntGoalDownwardEnv',
    max_episode_steps=500,
)

register(
    id='AntGoalBackward-v1',
    entry_point='gym.envs.mujoco:AntGoalBackwardEnv',
    max_episode_steps=500,
)

register(
    id='AntFinishLine-v1',
    entry_point='gym.envs.mujoco:AntFinishLineEnv',
    max_episode_steps=1000,
)

register(
    id='AntFinishLineBonus-v1',
    entry_point='gym.envs.mujoco:AntFinishLineBonusEnv',
    max_episode_steps=500,
)

register(
    id='AntFinishLineBonusWall-v1',
    entry_point='gym.envs.mujoco:AntFinishLineBonusWallEnv',
    max_episode_steps=500,
)

register(
    id='AntFinishLineVertical-v1',
    entry_point='gym.envs.mujoco:AntFinishLineVerticalEnv',
    max_episode_steps=1000,
)

register(
    id='AntTrial-v1',
    entry_point='gym.envs.mujoco:AntTrialEnv',
    max_episode_steps=500,
)

register(
    id='AntBackward-v1',
    entry_point='gym.envs.mujoco:AntBackwardEnv',
    max_episode_steps=1000,
)

register(
    id='AntUpward-v1',
    entry_point='gym.envs.mujoco:AntUpwardEnv',
    max_episode_steps=1000,
)

register(
    id='AntDownward-v1',
    entry_point='gym.envs.mujoco:AntDownwardEnv',
    max_episode_steps=1000,
)

register(
    id='AntRunning-v1',
    entry_point='gym.envs.mujoco:AntRunEnv',
    max_episode_steps=1000,
)

register(
    id='AntRunningFull-v1',
    entry_point='gym.envs.mujoco:AntRunFullEnv',
    max_episode_steps=500,
)

register(
    id='AntRunningFixedInit-v1',
    entry_point='gym.envs.mujoco:AntRunFixedInitEnv',
    max_episode_steps=500,
)

register(
    id='AntRunningNarrowHallway-v1',
    entry_point='gym.envs.mujoco:AntRunNarrowHallwayEnv',
    max_episode_steps=500,
)

register(
    id='AntRunningWideHallway-v1',
    entry_point='gym.envs.mujoco:AntRunWideHallwayEnv',
    max_episode_steps=500,
)

register(
    id='AntRunningUMaze-v1',
    entry_point='gym.envs.mujoco:AntRunUMazeEnv',
    max_episode_steps=500,
)

register(
    id='AntTargetImage-v1',
    entry_point='gym.envs.mujoco:AntTargetImageEnv',
    max_episode_steps=500,
)

register(
    id='Walker2d-v1',
    max_episode_steps=1000,
    entry_point='gym.envs.mujoco:Walker2dEnv',
)

register(
    id='Walker2dPOMDP-v1',
    max_episode_steps=1000,
    entry_point='gym.envs.mujoco:Walker2dPOMDPEnv',
)

register(
    id='Ant-v1',
    entry_point='gym.envs.mujoco:AntEnv',
    max_episode_steps=1000,
    reward_threshold=6000.0,
)

register(
    id='AntRllab-v1',
    entry_point='gym.envs.mujoco:AntRllabEnv',
    max_episode_steps=1000,
    reward_threshold=6000.0,
)

register(
    id='AntHindSight-v1',
    entry_point='gym.envs.mujoco:AntHindSightEnv',
    max_episode_steps=1000,
    reward_threshold=6000.0,
)

register(
    id='AntPOMDP-v1',
    entry_point='gym.envs.mujoco:AntPOMDPEnv',
    max_episode_steps=1000,
    reward_threshold=6000.0,
)

register(
    id='AntFourMasses-v1',
    entry_point='gym.envs.mujoco:AntFourMassesEnv',
    max_episode_steps=1000,
    reward_threshold=6000.0,
)


register(
    id='Humanoid-v1',
    entry_point='gym.envs.mujoco:HumanoidEnv',
    max_episode_steps=1000,
)

register(
    id='HumanoidPOMDP-v1',
    entry_point='gym.envs.mujoco:HumanoidPOMDPEnv',
    max_episode_steps=1000,
)

register(
    id='HumanoidCourse-v1',
    entry_point='gym.envs.mujoco:HumanoidCourseEnv',
    max_episode_steps=3000,
)

register(
    id='HumanoidSeq-v1',
    entry_point='gym.envs.mujoco:HumanoidSeqEnv',
    max_episode_steps=1000,
)

register(
    id='HumanoidStandup-v1',
    entry_point='gym.envs.mujoco:HumanoidStandupEnv',
    max_episode_steps=1000,
)

register(
    id='HumanoidStandupPOMDP-v1',
    entry_point='gym.envs.mujoco:HumanoidStandupPOMDPEnv',
    max_episode_steps=1000,
)

register(
    id='SimpleHumanoidRllab-v1',
    entry_point='gym.envs.mujoco:SimpleHumanoidRllabEnv',
    max_episode_steps=1000,
)

register(
    id='SimpleHumanoidRllabPOMDP-v1',
    entry_point='gym.envs.mujoco:SimpleHumanoidRllabPOMDPEnv',
    max_episode_steps=1000,
)

register(
    id='SimpleHumanoidRllabImage-v1',
    entry_point='gym.envs.mujoco:SimpleHumanoidRllabImageEnv',
    max_episode_steps=1000,
)

register(
    id='HumanoidRllab-v1',
    entry_point='gym.envs.mujoco:HumanoidRllabEnv',
    max_episode_steps=1000,
)

register(
    id='HumanoidRllabPOMDP-v1',
    entry_point='gym.envs.mujoco:HumanoidRllabPOMDPEnv',
    max_episode_steps=1000,
)

# Robotics
# ----------------------------------------

def _merge(a, b):
    a.update(b)
    return a

for reward_type in ['sparse', 'dense']:
    suffix = 'Dense' if reward_type == 'dense' else ''
    kwargs = {
        'reward_type': reward_type,
    }

    # Fetch
    register(
        id='FetchSlide{}-v1'.format(suffix),
        entry_point='gym.envs.robotics:FetchSlideEnv',
        kwargs=kwargs,
        max_episode_steps=50,
    )

    register(
        id='FetchPickAndPlace{}-v1'.format(suffix),
        entry_point='gym.envs.robotics:FetchPickAndPlaceEnv',
        kwargs=kwargs,
        max_episode_steps=50,
    )

    register(
        id='FetchReach{}-v1'.format(suffix),
        entry_point='gym.envs.robotics:FetchReachEnv',
        kwargs=kwargs,
        max_episode_steps=50,
    )

    register(
        id='H_FetchReach{}-v1'.format(suffix),
        entry_point='gym.envs.humanoid_robotics:FetchReachEnv',
        kwargs=kwargs,
        max_episode_steps=50,
    )

    register(
        id='H_FetchPush{}-v1'.format(suffix),
        entry_point='gym.envs.humanoid_robotics:FetchPushEnv',
        kwargs=kwargs,
        max_episode_steps=50,
    )

    register(
        id='H_FetchPickAndPlace{}-v1'.format(suffix),
        entry_point='gym.envs.humanoid_robotics:FetchPickAndPlaceEnv',
        kwargs=kwargs,
        max_episode_steps=50,

    )
    
    register(
        id='H_FetchPickAndPlaceObs{}-v1'.format(suffix),
        entry_point='gym.envs.humanoid_robotics:FetchPickAndPlaceObsEnv',
        kwargs=kwargs,
        max_episode_steps=50,

    )


    register(
        id='H_FetchPushObs{}-v1'.format(suffix),
        entry_point='gym.envs.humanoid_robotics:FetchPushObsEnv',
        kwargs=kwargs,
        max_episode_steps=50,

    )

    register(
        id='H_FetchReachObs{}-v1'.format(suffix),
        entry_point='gym.envs.humanoid_robotics:FetchReachObsEnv',
        kwargs=kwargs,
        max_episode_steps=50,

    )


    register(
        id='FetchPush{}-v1'.format(suffix),
        entry_point='gym.envs.robotics:FetchPushEnv',
        kwargs=kwargs,
        max_episode_steps=50,
    )

    # Hand
    register(
        id='HandReach{}-v0'.format(suffix),
        entry_point='gym.envs.robotics:HandReachEnv',
        kwargs=kwargs,
        max_episode_steps=50,
    )

    register(
        id='HandManipulateBlockRotateZ{}-v0'.format(suffix),
        entry_point='gym.envs.robotics:HandBlockEnv',
        kwargs=_merge({'target_position': 'ignore', 'target_rotation': 'z'}, kwargs),
        max_episode_steps=100,
    )

    register(
        id='HandManipulateBlockRotateParallel{}-v0'.format(suffix),
        entry_point='gym.envs.robotics:HandBlockEnv',
        kwargs=_merge({'target_position': 'ignore', 'target_rotation': 'parallel'}, kwargs),
        max_episode_steps=100,
    )

    register(
        id='HandManipulateBlockRotateXYZ{}-v0'.format(suffix),
        entry_point='gym.envs.robotics:HandBlockEnv',
        kwargs=_merge({'target_position': 'ignore', 'target_rotation': 'xyz'}, kwargs),
        max_episode_steps=100,
    )

    register(
        id='HandManipulateBlockFull{}-v0'.format(suffix),
        entry_point='gym.envs.robotics:HandBlockEnv',
        kwargs=_merge({'target_position': 'random', 'target_rotation': 'xyz'}, kwargs),
        max_episode_steps=100,
    )

    # Alias for "Full"
    register(
        id='HandManipulateBlock{}-v0'.format(suffix),
        entry_point='gym.envs.robotics:HandBlockEnv',
        kwargs=_merge({'target_position': 'random', 'target_rotation': 'xyz'}, kwargs),
        max_episode_steps=100,
    )

    register(
        id='HandManipulateEggRotate{}-v0'.format(suffix),
        entry_point='gym.envs.robotics:HandEggEnv',
        kwargs=_merge({'target_position': 'ignore', 'target_rotation': 'xyz'}, kwargs),
        max_episode_steps=100,
    )

    register(
        id='HandManipulateEggFull{}-v0'.format(suffix),
        entry_point='gym.envs.robotics:HandEggEnv',
        kwargs=_merge({'target_position': 'random', 'target_rotation': 'xyz'}, kwargs),
        max_episode_steps=100,
    )

    # Alias for "Full"
    register(
        id='HandManipulateEgg{}-v0'.format(suffix),
        entry_point='gym.envs.robotics:HandEggEnv',
        kwargs=_merge({'target_position': 'random', 'target_rotation': 'xyz'}, kwargs),
        max_episode_steps=100,
    )

    register(
        id='HandManipulatePenRotate{}-v0'.format(suffix),
        entry_point='gym.envs.robotics:HandPenEnv',
        kwargs=_merge({'target_position': 'ignore', 'target_rotation': 'xyz'}, kwargs),
        max_episode_steps=100,
    )

    register(
        id='HandManipulatePenFull{}-v0'.format(suffix),
        entry_point='gym.envs.robotics:HandPenEnv',
        kwargs=_merge({'target_position': 'random', 'target_rotation': 'xyz'}, kwargs),
        max_episode_steps=100,
    )

    # Alias for "Full"
    register(
        id='HandManipulatePen{}-v0'.format(suffix),
        entry_point='gym.envs.robotics:HandPenEnv',
        kwargs=_merge({'target_position': 'random', 'target_rotation': 'xyz'}, kwargs),
        max_episode_steps=100,
    )

# pathplan
register(
    id='PathHallway-v0',
    entry_point='gym.envs.pathplan:PathFindingHallwayEnv',
    max_episode_steps=3000,
)

# SimpleRobotics

register(
    id='ROAMHandGraspCube-v0',
    entry_point='gym.envs.simple_robotics:ROAM_GraspCubeEnv',
    max_episode_steps=1000,
)

register(
    id='ROAMHandGraspCube-v1',
    entry_point='gym.envs.roam_robotics:ROAM_GraspCubeEnv',
    max_episode_steps=1000,
)


register(
    id='SeaHandGraspCubeLift-v0',
    entry_point='gym.envs.simple_robotics:GraspCubeLiftEnv',
    max_episode_steps=3000,
)

register(
    id='SeaHandGraspCube-v0',
    entry_point='gym.envs.simple_robotics:GraspCubeEnv',
    max_episode_steps=1000,
)

register(
    id='SeaHandGraspEgg-v0',
    entry_point='gym.envs.simple_robotics:GraspEggEnv',
    max_episode_steps=1000,
)

register(
    id='SeaHandGraspPen-v0',
    entry_point='gym.envs.simple_robotics:GraspPenEnv',
    max_episode_steps=1000,
)

register(
    id='SeaHandGraspBall-v0',
    entry_point='gym.envs.simple_robotics:GraspBallEnv',
    max_episode_steps=1000,
)

register(
    id='SeaHandGraspCylinder-v0',
    entry_point='gym.envs.simple_robotics:GraspCylinderEnv',
    max_episode_steps=1000,
)

register(
    id='SeaHandGraspCube-v1',
    entry_point='gym.envs.simple_robotics:GraspCube2Env',
    max_episode_steps=1000,
)

register(
    id='SeaHandGraspEgg-v1',
    entry_point='gym.envs.simple_robotics:GraspEgg2Env',
    max_episode_steps=1000,
)

register(
    id='SeaHandGraspPen-v1',
    entry_point='gym.envs.simple_robotics:GraspPen2Env',
    max_episode_steps=1000,
)

register(
    id='SeaHandGraspBall-v1',
    entry_point='gym.envs.simple_robotics:GraspBall2Env',
    max_episode_steps=1000,
)

register(
    id='SeaHandGraspCylinder-v1',
    entry_point='gym.envs.simple_robotics:GraspCylinder2Env',
    max_episode_steps=1000,
)


register(
    id='SeaHandGraspCube-v2',
    entry_point='gym.envs.simple_robotics:GraspCube3Env',
    max_episode_steps=1000,
)

register(
    id='SeaHandGraspEgg-v2',
    entry_point='gym.envs.simple_robotics:GraspEgg3Env',
    max_episode_steps=1000,
)

register(
    id='SeaHandGraspPen-v2',
    entry_point='gym.envs.simple_robotics:GraspPen3Env',
    max_episode_steps=1000,
)

register(
    id='SeaHandGraspBall-v2',
    entry_point='gym.envs.simple_robotics:GraspBall3Env',
    max_episode_steps=1000,
)

register(
    id='SeaHandGraspCylinder-v2',
    entry_point='gym.envs.simple_robotics:GraspCylinder3Env',
    max_episode_steps=1000,
)

register(
    id='SeaHandGraspCubeRelative-v0',
    entry_point='gym.envs.simple_robotics:GraspCubeRelativeEnv',
    max_episode_steps=1000,
)

register(
    id='SeaHandGraspEggRelative-v0',
    entry_point='gym.envs.simple_robotics:GraspEggRelativeEnv',
    max_episode_steps=1000,
)

register(
    id='SeaHandGraspPenRelative-v0',
    entry_point='gym.envs.simple_robotics:GraspPenRelativeEnv',
    max_episode_steps=1000,
)

register(
    id='SeaHandGraspBallRelative-v0',
    entry_point='gym.envs.simple_robotics:GraspBallRelativeEnv',
    max_episode_steps=1000,
)

register(
    id='SeaHandGraspCylinderRelative-v0',
    entry_point='gym.envs.simple_robotics:GraspCylinderRelativeEnv',
    max_episode_steps=1000,
)

register(
    id='SeaHandGraspCubeRelativeSafe-v0',
    entry_point='gym.envs.simple_robotics:GraspCubeRelativeSafeEnv',
    max_episode_steps=3000,
)

register(
    id='SeaHandGraspCubeRelativeSafeEasy-v0',
    entry_point='gym.envs.simple_robotics:GraspCubeRelativeSafeEasyEnv',
    max_episode_steps=3000,
)

register(
    id='SeaHandGraspCubeRelativeSafeThree-v0',
    entry_point='gym.envs.simple_robotics:GraspCubeRelativeSafeThreeEnv',
    max_episode_steps=3000,
)
register(
    id='SeaHandGraspCubeRelativeSafeOne-v0',
    entry_point='gym.envs.simple_robotics:GraspCubeRelativeSafeOneEnv',
    max_episode_steps=3000,
)

register(
    id='SeaHandGraspEggRelativeSafe-v0',
    entry_point='gym.envs.simple_robotics:GraspEggRelativeSafeEnv',
    max_episode_steps=3000,
)

register(
    id='SeaHandGraspPenRelativeSafe-v0',
    entry_point='gym.envs.simple_robotics:GraspPenRelativeSafeEnv',
    max_episode_steps=3000,
)

register(
    id='SeaHandGraspBallRelativeSafe-v0',
    entry_point='gym.envs.simple_robotics:GraspBallRelativeSafeEnv',
    max_episode_steps=3000,
)

register(
    id='SeaHandGraspCylinderRelativeSafe-v0',
    entry_point='gym.envs.simple_robotics:GraspCylinderRelativeSafeEnv',
    max_episode_steps=1000,
)

register(
    id='SeaHandGraspCubeRelativeSafeSmallObject-v0',
    entry_point='gym.envs.simple_robotics:GraspCubeRelativeSafeSmallObjectEnv',
    max_episode_steps=3000,
)

register(
    id='SeaHandGraspCubeRelativeSafeTimeSmall-v0',
    entry_point='gym.envs.simple_robotics:GraspCubeRelativeSafeTimeSmallEnv',
    max_episode_steps=3000,
)

register(
    id='SeaHandGraspCubeRelativeSafeRender-v0',
    entry_point='gym.envs.simple_robotics:GraspCubeRelativeSafeRenderEnv',
    max_episode_steps=6000,
)

register(
    id='SeaHandGraspCubeRelativeSafeRenderBig-v0',
    entry_point='gym.envs.simple_robotics:GraspCubeRelativeSafeRenderBigEnv',
    max_episode_steps=6000,
)

register(
    id='SeaHandGraspCubeSingle-v0',
    entry_point='gym.envs.simple_robotics:GraspSingleCubeEnv',
    max_episode_steps=3000,
)

register(
    id='SeaHandGraspCubeSmooth-v0',
    entry_point='gym.envs.simple_robotics:GraspCubeSmoothEnv',
    max_episode_steps=3000,
)

register(
    id='SeaHandGraspCubeActContext-v0',
    entry_point='gym.envs.simple_robotics:GraspCubeActContextEnv',
    max_episode_steps=3000,
)

register(
    id='SeaHandGraspCubeImageContext-v0',
    entry_point='gym.envs.simple_robotics:GraspCubeImageContextEnv',
    max_episode_steps=3000,
)

# Atari
# ----------------------------------------

# # print ', '.join(["'{}'".format(name.split('.')[0]) for name in atari_py.list_games()])
for game in ['air_raid', 'alien', 'amidar', 'assault', 'asterix', 'asteroids', 'atlantis',
    'bank_heist', 'battle_zone', 'beam_rider', 'berzerk', 'bowling', 'boxing', 'breakout', 'carnival',
    'centipede', 'chopper_command', 'crazy_climber', 'demon_attack', 'double_dunk',
    'elevator_action', 'enduro', 'fishing_derby', 'freeway', 'frostbite', 'gopher', 'gravitar',
    'hero', 'ice_hockey', 'jamesbond', 'journey_escape', 'kangaroo', 'krull', 'kung_fu_master',
    'montezuma_revenge', 'ms_pacman', 'name_this_game', 'phoenix', 'pitfall', 'pong', 'pooyan',
    'private_eye', 'qbert', 'riverraid', 'road_runner', 'robotank', 'seaquest', 'skiing',
    'solaris', 'space_invaders', 'star_gunner', 'tennis', 'time_pilot', 'tutankham', 'up_n_down',
    'venture', 'video_pinball', 'wizard_of_wor', 'yars_revenge', 'zaxxon']:
    for obs_type in ['image', 'ram']:
        # space_invaders should yield SpaceInvaders-v0 and SpaceInvaders-ram-v0
        name = ''.join([g.capitalize() for g in game.split('_')])
        if obs_type == 'ram':
            name = '{}-ram'.format(name)

        nondeterministic = False
        if game == 'elevator_action' and obs_type == 'ram':
            # ElevatorAction-ram-v0 seems to yield slightly
            # non-deterministic observations about 10% of the time. We
            # should track this down eventually, but for now we just
            # mark it as nondeterministic.
            nondeterministic = True

        register(
            id='{}-v0'.format(name),
            entry_point='gym.envs.atari:AtariEnv',
            kwargs={'game': game, 'obs_type': obs_type, 'repeat_action_probability': 0.25},
            max_episode_steps=10000,
            nondeterministic=nondeterministic,
        )

        register(
            id='{}-v4'.format(name),
            entry_point='gym.envs.atari:AtariEnv',
            kwargs={'game': game, 'obs_type': obs_type},
            max_episode_steps=100000,
            nondeterministic=nondeterministic,
        )

        # Standard Deterministic (as in the original DeepMind paper)
        if game == 'space_invaders':
            frameskip = 3
        else:
            frameskip = 4

        # Use a deterministic frame skip.
        register(
            id='{}Deterministic-v0'.format(name),
            entry_point='gym.envs.atari:AtariEnv',
            kwargs={'game': game, 'obs_type': obs_type, 'frameskip': frameskip, 'repeat_action_probability': 0.25},
            max_episode_steps=100000,
            nondeterministic=nondeterministic,
        )

        register(
            id='{}Deterministic-v4'.format(name),
            entry_point='gym.envs.atari:AtariEnv',
            kwargs={'game': game, 'obs_type': obs_type, 'frameskip': frameskip},
            max_episode_steps=100000,
            nondeterministic=nondeterministic,
        )

        register(
            id='{}NoFrameskip-v0'.format(name),
            entry_point='gym.envs.atari:AtariEnv',
            kwargs={'game': game, 'obs_type': obs_type, 'frameskip': 1, 'repeat_action_probability': 0.25}, # A frameskip of 1 means we get every frame
            max_episode_steps=frameskip * 100000,
            nondeterministic=nondeterministic,
        )

        # No frameskip. (Atari has no entropy source, so these are
        # deterministic environments.)
        register(
            id='{}NoFrameskip-v4'.format(name),
            entry_point='gym.envs.atari:AtariEnv',
            kwargs={'game': game, 'obs_type': obs_type, 'frameskip': 1}, # A frameskip of 1 means we get every frame
            max_episode_steps=frameskip * 100000,
            nondeterministic=nondeterministic,
        )

# Board games
# ----------------------------------------

register(
    id='Go9x9-v0',
    entry_point='gym.envs.board_game:GoEnv',
    kwargs={
        'player_color': 'black',
        'opponent': 'pachi:uct:_2400',
        'observation_type': 'image3c',
        'illegal_move_mode': 'lose',
        'board_size': 9,
    },
    # The pachi player seems not to be determistic given a fixed seed.
    # (Reproduce by running 'import gym; h = gym.make('Go9x9-v0'); h.seed(1); h.reset(); h.step(15); h.step(16); h.step(17)' a few times.)
    #
    # This is probably due to a computation time limit.
    nondeterministic=True,
)

register(
    id='Go19x19-v0',
    entry_point='gym.envs.board_game:GoEnv',
    kwargs={
        'player_color': 'black',
        'opponent': 'pachi:uct:_2400',
        'observation_type': 'image3c',
        'illegal_move_mode': 'lose',
        'board_size': 19,
    },
    nondeterministic=True,
)

register(
    id='Hex9x9-v0',
    entry_point='gym.envs.board_game:HexEnv',
    kwargs={
        'player_color': 'black',
        'opponent': 'random',
        'observation_type': 'numpy3c',
        'illegal_move_mode': 'lose',
        'board_size': 9,
    },
)

# Debugging
# ----------------------------------------

register(
    id='OneRoundDeterministicReward-v0',
    entry_point='gym.envs.debugging:OneRoundDeterministicRewardEnv',
    local_only=True
)

register(
    id='TwoRoundDeterministicReward-v0',
    entry_point='gym.envs.debugging:TwoRoundDeterministicRewardEnv',
    local_only=True
)

register(
    id='OneRoundNondeterministicReward-v0',
    entry_point='gym.envs.debugging:OneRoundNondeterministicRewardEnv',
    local_only=True
)

register(
    id='TwoRoundNondeterministicReward-v0',
    entry_point='gym.envs.debugging:TwoRoundNondeterministicRewardEnv',
    local_only=True,
)

# Parameter tuning
# ----------------------------------------
register(
    id='ConvergenceControl-v0',
    entry_point='gym.envs.parameter_tuning:ConvergenceControl',
)

register(
    id='CNNClassifierTraining-v0',
    entry_point='gym.envs.parameter_tuning:CNNClassifierTraining',
)


#gazebo

register(
    id='mobilebaselidar-v0',
    entry_point='gym.envs.gazebo:GazeboMobileLidarEnv',
)


# Safety
# ----------------------------------------

# interpretability envs
register(
    id='PredictActionsCartpole-v0',
    entry_point='gym.envs.safety:PredictActionsCartpoleEnv',
    max_episode_steps=200,
)

register(
    id='PredictObsCartpole-v0',
    entry_point='gym.envs.safety:PredictObsCartpoleEnv',
    max_episode_steps=200,
)

# semi_supervised envs
    # probably the easiest:
register(
    id='SemisuperPendulumNoise-v0',
    entry_point='gym.envs.safety:SemisuperPendulumNoiseEnv',
    max_episode_steps=200,
)
    # somewhat harder because of higher variance:
register(
    id='SemisuperPendulumRandom-v0',
    entry_point='gym.envs.safety:SemisuperPendulumRandomEnv',
    max_episode_steps=200,
)
    # probably the hardest because you only get a constant number of rewards in total:
register(
    id='SemisuperPendulumDecay-v0',
    entry_point='gym.envs.safety:SemisuperPendulumDecayEnv',
    max_episode_steps=200,
)

# off_switch envs
register(
    id='OffSwitchCartpole-v0',
    entry_point='gym.envs.safety:OffSwitchCartpoleEnv',
    max_episode_steps=200,
)

register(
    id='OffSwitchCartpoleProb-v0',
    entry_point='gym.envs.safety:OffSwitchCartpoleProbEnv',
    max_episode_steps=200,
)


# RL^2
# ----------------------------------------

# Bandits

for n_arms in [5, 10, 50]:
    for n_episodes in [10, 100, 500, 1000]:
        register(
            id='BernoulliBandit-{k}.arms-{n}.episodes-v0'.format(k=n_arms, n=n_episodes),
            entry_point='gym.envs.rl2:BernoulliBanditEnv',
            kwargs={'n_arms': n_arms, 'n_episodes': n_episodes},
            timestep_limit=n_episodes,
        )

# Tabular MDPs

for n_states in [10]:
    for n_actions in [5]:
        for episode_length in [10]:
            for n_episodes in [10, 25, 50, 75, 100, 200, 400]:
                register(
                    id='RandomTabularMDP-{s}.states-{a}.actions-{t}.timesteps-{n}.episodes-v0'.format(
                        s=n_states, a=n_actions, t=episode_length, n=n_episodes),
                    entry_point='gym.envs.rl2:RandomTabularMDPEnv',
                    kwargs={'n_states': n_states, 'n_actions': n_actions, 'episode_length': episode_length,
                            'n_episodes': n_episodes},
                    timestep_limit=n_episodes * episode_length,
                )
#>>>>>>> 44c77177a09363660f47cedaa7ed66e3b833f57b
