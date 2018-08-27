#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
Nukeの作業効率化のためのスクリプト

makePostageStamp()
ReadNodeを選択肢実行（複数可）、dotをはさみPostageStampを生成する。生成する際にLabelにファイル名を記載するスクリプトを追加する。

alineNodes()
選択したノードを横に並べる
"""

"""
FX Nuke Utilities
Nuke作業効率化の為のスクリプト群（になる予定）

Make Postage Stamp
ReadNodeを選択肢実行（複数可）、dotをはさみPostageStampを生成する。生成する際にLabelにファイル名を記載するスクリプトを追加する。

ytanaka@ppi.co.jp
2015/10/27
"""

import nuke

def makePostageStamp():
    nodes = nuke.selectedNodes()

    for n in nodes:
        #ノードの位置を取得
        x = n.xpos()
        y = n.ypos()

        #dotノードを生成、設置
        dot = nuke.createNode("Dot")
        dot.setXpos(x + 34)
        dot.setYpos(y + 110)
        dot.setInput(0, n)

        #PostageStampノードを生成、設置、設定
        ps = nuke.createNode("PostageStamp")
        ps.setXpos(x)
        ps.setYpos(y + 150)
        ps.setInput(0, dot)
        ps["label"].setValue("[file tail [metadata input/filename]]")
        ps["hide_input"].setValue(1)

def alineNodes():
    nodes = nuke.selectedNodes()

    # 基準になるノードのx,yを取得
    basenode = nodes[0]
    x = basenode.xpos()
    y = basenode.ypos()

    #　リストから基準となるノードをぬいて更新
    nodes = nodes[1:]

    # リストのノードの位置を調整
    for n in nodes:
        x += 100
        n.setXpos(x)
        n.setYpos(y)
