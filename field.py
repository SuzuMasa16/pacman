from item import Item
from player improt Player
from enemy import Enemy
from food import Food
from block import Block


class Field:
    """
    ゲームのフィールドのためのクラス
    フィールドの更新と衝突判定

    Attributes:
        field_size (int): フィールドのサイズ
        players (list[Player]): プレイヤーの情報リスト
        enemies (list[Enemy]): 敵の情報リスト
        blocks (list[Block]): 壁の情報
        foods (list[Food])
        field (list[list[str]])
    """
    def _init_(self, 
               field_size: int, 
               players: list[Player], 
               enemies: list[Enemy], 
               blocks: list[Block], 
               foods: list[Food]) -> None:
        """"
        初期化関数

        Args:
            field_size (double): フィールドのサイズ
            foods (list[Food]): 落ちてるアイテムの情報リスト
            players (list[Player]): プレイヤーの情報リスト
            enemies (list[Enemy]): 敵の情報リスト
            Block (list[Block]): 壁の情報リスト
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