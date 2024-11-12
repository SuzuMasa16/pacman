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
        pass

    def update_field(self) -> list[list[str]]:
        """
        アイテムを配置、プレイヤーを配置、フィールドを更新

        Returns:


        Examples:
            >>> p = [1]
            >>> field = Field(2, p)
            >>> field.update_field()
            [['p', ' '], [' ', ' ']]
        """

        for i in range(self.field_size):
            for j in range(self.field_size):
                self.field[i][j] = " "

        for player in self.players:
            self.field[0][0] = "p"

        return self.field

        pass
        for player in self.players:
            if player.status:
                self.field[player.next_x][player.next_y] = player.icon

    def display_field(self) -> None:
        """
        フィールドを表示

        Returns:
            None

        Examples:
            >>>
        """

        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
