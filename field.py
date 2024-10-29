from player import Player


class Field:
    """Fieldクラス
    Fieldクラスは、ゲームのフィールドを表すクラスです。
    プレイヤー、敵、アイテムの位置を更新し、Fieldを表示する機能を持ちます。
    位置を更新する際に衝突判定を行います。

    Attributes:
        players (list[Player]): プレイヤーのリスト
        enemies (list[Enemy]): 敵のリスト
        foods (list[Food]]): アイテムのリスト
        blocks (list[Block]): アイテムのリスト
        field (list[list[str]]): フィールドの情報
        f_size (int): フィールドのサイズ
    """

    def __init__(self, field_size: int, players: list[Player]) -> None:
        """"
        初期化関数

        Args:
            field_size (double): フィールドのサイズ
            players (list[Player]): プレイヤーのリスト
        """

        self.field_size = field_size
        self.players = players
        self.field = [[" "for _ in range(field_size)]
                      for _ in range(field_size)]
        self.update_field()
        pass

    def update_field(self) -> list[list[str]]:
        """
        アイテムを配置、プレイヤーを配置、フィールドを更新

        Returns:


        Examples:
            >>> p = [Player(0,1)]
            >>> field = Field(2, p)
            >>> field.update_field()
            [[' ', '😶'], [' ', ' ']]
        """

        for i in range(self.field_size):  # 一旦すべてを空に
            for j in range(self.field_size):
                self.field[i][j] = " "

        for player in self.players:
            self.field[player.next_x][player.next_y] = player.icon

        return self.field

    def display_field(self) -> None:
        """
        フィールドを表示

        Returns:
            None

        Examples:
            >>> p=[Player(0,1)]
            >>> f = Field(2,p)
            >>> f.display_field()
             😶
            <BLANKLINE>
        """

        max_width = max(len(row) for row in self.field)

        for row in self.field:
            row_str = "".join(row)
            row_str = row_str.ljust(max_width)
            print(row_str)

        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
