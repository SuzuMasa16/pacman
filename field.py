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

    def _init_(self, field_size: int, players: list[Player]) -> None:
        """"
        初期化関数

        Args:
            field_size (double): フィールドのサイズ
            players (list[Player]): プレイヤーのリスト
        """

        pass

    def update_field(self) -> None:
        """
        アイテムを配置、プレイヤーを配置、フィールドを更新

        Returns:

        Examples:
            >>>
        """
        pass

    def display_field(self) -> None:
        """
        フィールドを表示

        Returns:
            None

        Examples:
            >>>
        """

        pass
