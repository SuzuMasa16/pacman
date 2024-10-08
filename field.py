from player improt Player
from block import Block


class Field:
    """
    ゲームのフィールドのためのクラス
    フィールドの更新と衝突判定

    Attributes:
        field_size (int): フィールドのサイズ
        players (list[Player]): プレイヤーの情報リスト
        field (list[list[str]])
    """
    def _init_(self, 
               field_size: int, 
               players: list[Player]) -> None:
        """"
        初期化関数

        Args:
            field_size (double): フィールドのサイズ
            players (list[Player]): プレイヤーの情報リスト
        """
    
    def update_field(self) -> list[str]:
        """
        アイテムを配置、プレイヤーを配置、フィールドを更新

        Returns:
            list[list[str]]: 更新されたフィールド
        
        Examples:
            >>>
        """
    
    def display_field(self) -> list[list[str]]:
        """
        フィールドを表示

        Returns:
            None
        
        Examples:
            >>>
        """
    
    def update_colision(self, target: Item, items: list[Item]) -> Item | None:
        """
        衝突を判定する

        Returns:
            衝突してなければNone:
            衝突していれば衝突したアイテムを返す

        Examples:
            >>>
        """