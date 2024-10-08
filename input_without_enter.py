import sys
import termios


class InputWithoutEnter:
    """
    エンターキーを押さなくても入力を受けてくれるようにする
    """

    def input_without_enter():
        """
        エンターキーを押さないで入力

        returns:
            str: wasd
        """