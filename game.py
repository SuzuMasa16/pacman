import time
import os
from player import Player
from field import Field
from config import Parameters
from input import UserInput


class Game:
    """
    ゲームクラス
    ゲームのメインループ部分を実行するクラス

    Attributes:
        Players (list[Player]) : Playerのリスト
        field (Field) : Fieldのインスタンス
    """

    def __init__(self, params: Parameters) -> None:
        """
        ゲームクラスの初期化関数

        Args:
            params (Parameters): configパラメータのインスタンス
        """

        self.players: list[Player] = []
        self.field: Field
        self.setup(params)
        self.start()

    def setup(self, params: Parameters) -> None:
        """
        初期設定を行うメソッド

        Args:
          params : configパラメータのインスタンス
        """

        field_size: int = params.field_size
        self.players = [Player(1, 1)]
        self.field = Field(field_size, self.players)

    def start(self) -> None:
        """
        メインループのメソッド
        """

        while True:

            os.system("cls" if os.name == "nt" else "clear")  # ターミナルをクリア
            print("aaa")
            self.field.display_field()

            for player in self.players:
                key = UserInput.get_user_input()
                player.get_next_pos(key)

            for item in self.players:
                item.update_pos()

            self.field.update_field()

            time.sleep(0.3)
