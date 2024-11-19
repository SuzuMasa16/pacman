from item import Item
import random


class enemy(Item):
    """ エネミークラス
    Itemを継承して作成したエネミークラス.
    入力を受け取ってランダムな方向に移動したときの」計算するメソッドと
    マップから移動して良いと許可が出た時に呼び出される座標を更新するメソッド
    を追加.

    Attributes:
        self.icon(str) : 表示されるアイテムのアイコン
        self.now_x(int) : 現在のx座標
        self.now_y(int) : 現在のy座標
        self.next_x(int) : 次の時刻でのx座標
        self.next_y(int) : 次の時刻でのy座標
        self.status(bool) : アイテムの状態（Trueなら存在する、Falseなら存在しない消滅した）
    """
    def __init__(self, x, y) -> None:
        pass

        super().__init__(x, y)
        self.icon = "E"

    def get_next_pos(self) -> tuple[int, int]:
        """
        入力を受け取りランダムな方向に移動した方向を計算して次の座標を返すメソッド
        現在のプレイヤーの座標から次に移動したい座標を[num1,num2]で決めて戻り値として出力する.

        Args:

        Returns:
            tuple[int, int]: 次に移動したい座標(例:入力が(1,0)で現在のプレイヤーの座標が
            (2,3)だった時,戻り値は(3,3))

        Examples:
            >>> player = Player(2, 3)
            >>> player.get_next_pos((1, 0))
            (3, 3)
            >>> player = Player(2, 3)
            >>> player.get_next_pos((0, 1))
            (2, 4)

        """

        num1 = random.randint(-1, 1)
        num2 = random.randint(-1, 1)
        dir = (num1, num2)
        self.next_x = self.now_x + dir[0]
        self.next_y = self.now_y + dir[1]
        return (self.next_x, self.next_y)
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
