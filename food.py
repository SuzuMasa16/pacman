from item import Item


class food(Item):
    """フードクラス
    Itemを継承して作成したフードクラス
    初期座標をrandomで決めるメゾット

    Attributes:
        now_x (int): 現在のx座標
        now_y (int): 現在のy座標
        status (bool): アイテムの状態
        icon (str): 表示アイコン

    """
    def __init__(self, x, y) -> None:

        super().__init__(x, y)
        self.icon = "F"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
