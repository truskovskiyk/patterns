import random

class RobotBombDefuser(object):

    def __init__(self, robot_conf=41):
        self.random = random
        self.robot_conf = robot_conf
        self._connected = False

    def walk_forward(self, steps):
        print("forward {} steps".format(steps))

    def turn_right(self):
        print("turn_right")

    def turn_left(self):
        print("turn_left")

    def defuse_bomb(self):
        print("defuse_bomb")

    def try_connect(self):
        return self.random.randint(0, 10) < 3

    def is_connected(self):
        # self._connected = self.try_connect()
        return self._connected

    def connet_wireless(self, communication_wireless):
        if communication_wireless == self.robot_conf:
            self._connected = self.try_connect()

class RobotBombDefuserProxy(RobotBombDefuser):
    def __init__(self, communication_conf, conn_attemts=6):
        self.robot_bomd_defuser = RobotBombDefuser()
        self.communication_conf = communication_conf
        self.conn_attemts = conn_attemts

    def ensure_connection_with_robot(self):
        for i in range(self.conn_attemts):
            if not self.robot_bomd_defuser.is_connected():
                self.robot_bomd_defuser.connet_wireless(self.communication_conf)

            else:
                break
        if not self.robot_bomd_defuser.is_connected():
            raise ValueError("No connection")

    def walk_forward(self, steps):
        self.ensure_connection_with_robot()
        self.robot_bomd_defuser.walk_forward(steps)

    def turn_right(self):
        self.ensure_connection_with_robot()
        self.robot_bomd_defuser.turn_right()

    def turn_left(self):
        self.ensure_connection_with_robot()
        self.robot_bomd_defuser.turn_left()

    def defuse_bomb(self):
        self.ensure_connection_with_robot()
        self.robot_bomd_defuser.defuse_bomb()

if __name__ == '__main__':
    robot_proxy = RobotBombDefuserProxy(communication_conf=41, conn_attemts=10)
    robot_proxy.walk_forward(10)
    robot_proxy.turn_right()
    robot_proxy.turn_left()
    robot_proxy.defuse_bomb()
