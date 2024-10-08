from input_without_enter import InputWithoutEnter


class UserInput:
    """
    ユーザの入力を受け取るクラス
    """

    def get_input() -> move[int, int]:
        """
        ユーザの入力からx,y座標を返す

        Returns:
            move[x,y]: 移動先のx,y座標
        """