import time
from player import Player
from enemy import Enemy
from food import Food
from block import Block
from field import Field
from user_input import UserInput
from config import Parameters
from random import randint
import logging
import os

class Game:
    """
    ゲームを実行するメインのクラス
    
    Attributes:
        players (list[Plyayer]): プレイヤーリスト
        enemies (list[Enermy]): エネミーのリスト
        field (Field): フィールド
        blocks (list[Block]) : ブロックのリスト
        foods (list[Food]): フィールドのリスト
    """

    def __init__(self, parameters:Parameters) -> None:
        """
        初期化関数

        Args:
            parameters (Parameters): configのパラメータ
        """

    def setup(self,parameters:Parameters) -> None:
        """
        ゲームの初期設定

        Args:
            parameters (Parameters): configから
        """

    def start(self) -> str:
        """
        ゲームのメイン部分
        ループとループの終了を判定

        Returns:
            str :GAME OVER(CLEAR)!!
        """