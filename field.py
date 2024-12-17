from player import Player
from item import Item
from enemy import Enemy
from food import Food
from block import Block


class Field:
    """Fieldクラス
    Fieldクラスは、ゲームのフィールドを表すクラスです。
    プレイヤー、敵、アイテムの位置を更新し、Fieldを表示する機能を持ちます。
    位置を更新する際に衝突判定を行います。

    Attributes:
        players (list[Player]): プレイヤーのリスト
        f_size (int): フィールドのサイズ
        enemies (list[Enemy]): 敵のリスト
        foods (list[Food]]): アイテムのリスト
        blocks (list[Block]): アイテムのリスト
        field (list[list[str]]): フィールドの情報
    """

    def __init__(self, field_size: int, players: list[Player], 
                 enemies: list[Enemy], foods: list[Food],
                 blocks: list[Block]) -> None:
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
        self.players = players
        self.enemies = enemies
        self.foods = foods
        self.blocks = blocks
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

        for food in self.foods:
            self.field[food.now_y][food.now_x] = food.icon
        for enemy in self.enemies:
            self.field[enemy.now_y][enemy.now_x] = enemy.icon
        for block in self.blocks:
            self.field[block.now_y][block.now_x] = block.icon
        for player in self.players:
            self.field[player.next_x][player.next_y] = player.icon

        return self.field

    def check_bump(  # お手本のパクリ
            self,
            target: Item,
            items: list[Item]) -> Item | None:
        """
        2つのアイテムの位置が重なっているか判定する関数

        Args:
            target (Item): アイテム1
            items (list[Item]): アイテムのリスト2

        Returns:
            Item | None: 重なっているアイテムがあればそのアイテム、なければNone

        Examples:
            >>> p = Item(0, 0)
            >>> e = Item(1, 1)
            >>> field = Field([p], [e], [], [])
            >>> p.next_x = 1
            >>> r = field.check_bump(p, [e])
            >>> r is None
            True
            >>> p.next_y = 1
            >>> r = field.check_bump(p, [e])
            >>> r is e
            True
        """
        # 衝突判定を行う処理を記述
        for item in items:
            if item.next_x == target.next_x and item.next_y == target.next_y:
                return item
        return None

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
