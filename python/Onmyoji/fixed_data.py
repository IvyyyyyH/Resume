#!/usr/bin/env python
# -*- coding: utf-8 -*-
# fixed information

YUHUN_PROP_LIST = [u'御魂序号', u'御魂类型', u'位置', u'攻击',
                      u'攻击加成', u'防御', u'防御加成', u'暴击',
                      u'暴击伤害', u'生命', u'生命加成', u'效果命中',
                      u'效果抵抗', u'速度']

INCREASE_LIST = [u"攻击加成", u"防御加成", u"生命加成", u"效果抵抗", u"效果命中", u"暴击"]

YUHUN_INCREASE  = {u"珍珠": {u"加成类型": u"防御加成", u"加成数值": 30},
                  u"骰子鬼": {u"加成类型": u"效果抵抗", u"加成数值": 15},
                  u"蚌精": {u"加成类型": u"效果命中", u"加成数值": 15},
                  u"魅妖": {u"加成类型": u"防御加成", u"加成数值": 30},
                  u"针女": {u"加成类型": u"暴击", u"加成数值": 15},
                  u"返魂香": {u"加成类型": u"效果抵抗", u"加成数值": 15},
                  u"雪幽魂": {u"加成类型": u"防御加成", u"加成数值": 30},
                  u"地藏像": {u"加成类型": u"生命加成", u"加成数值": 15},
                  u"蝠翼": {u"加成类型": u"攻击加成", u"加成数值": 15},
                  u"涅槃之火": {u"加成类型": u"生命加成", u"加成数值": 15},
                  u"三味": {u"加成类型": u"暴击", u"加成数值": 15},
                  u"魍魉之匣": {u"加成类型": u"效果抵抗", u"加成数值": 15},
                  u"被服": {u"加成类型": u"生命加成", u"加成数值": 15},
                  u"招财猫": {u"加成类型": u"防御加成", u"加成数值": 30},
                  u"反枕": {u"加成类型": u"防御加成", u"加成数值": 30},
                  u"轮入道": {u"加成类型": u"攻击加成", u"加成数值": 15},
                  u"日女巳时": {u"加成类型": u"防御加成", u"加成数值": 30},
                  u"镜姬": {u"加成类型": u"生命加成", u"加成数值": 15},
                  u"钟灵": {u"加成类型": u"生命加成", u"加成数值": 15},
                  u"狰": {u"加成类型": u"攻击加成", u"加成数值": 15},
                  u"火灵": {u"加成类型": u"效果命中", u"加成数值": 15},
                  u"鸣屋": {u"加成类型": u"攻击加成", u"加成数值": 15},
                  u"薙魂": {u"加成类型": u"生命加成", u"加成数值": 15},
                  u"心眼": {u"加成类型": u"攻击加成", u"加成数值": 15},
                  u"木魅": {u"加成类型": u"防御加成", u"加成数值": 30},
                  u"树妖": {u"加成类型": u"生命加成", u"加成数值": 15},
                  u"网切": {u"加成类型": u"暴击", u"加成数值": 15},
                  u"阴摩罗": {u"加成类型": u"攻击加成", u"加成数值": 15},
                  u"伤魂鸟": {u"加成类型": u"暴击", u"加成数值": 15},
                  u"破势": {u"加成类型": u"暴击", u"加成数值": 15},
                  u"镇墓兽": {u"加成类型": u"暴击", u"加成数值": 15},
                  u"狂骨": {u"加成类型": u"攻击加成", u"加成数值": 15},
                  u"幽谷响": {u"加成类型": u"效果抵抗", u"加成数值": 15},
                  u"土蜘蛛": {u"加成类型": u"", u"加成数值": 0},
                  u"胧车": {u"加成类型": u"", u"加成数值": 0},
                  u"荒骷髅": {u"加成类型": u"", u"加成数值": 0},
                  u"地震鲶": {u"加成类型": u"", u"加成数值": 0},
                  u"蜃气楼": {u"加成类型": u"", u"加成数值": 0},
                  }


SHISHEN_INFO = {
                u"------SP------":{},
                u"炼狱茨木童子": {u"攻击": 3323.2,u"生命": 10253.8,u"防御": 379.26,u"速度": 112,u"暴击": 15,u"暴击伤害": 150,u"效果命中": 0,u"效果抵抗": 0},
                u"少羽大天狗": {u"攻击": 3484, u"生命": 9684.2, u"防御": 374.85, u"速度": 122, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"-----SSR------":{},
                u"八岐大蛇":{u"攻击": 4073.6, u"生命": 12418.28, u"防御": 480.69, u"速度": 118, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"桔梗": {u"攻击": 3108.8, u"生命": 10595.56, u"防御": 401.31, u"速度": 115, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"白藏主":{u"攻击": 1822.4, u"生命": 14241, u"防御": 471.87, u"速度": 111, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"杀生丸": {u"攻击": 3323.2, u"生命": 10025.96, u"防御": 388.08, u"速度": 118, u"暴击": 12, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"犬夜叉": {u"攻击": 2974.8, u"生命": 11393, u"防御": 392.49, u"速度": 114, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"鬼切": {u"攻击": 3350, u"生命": 10823.4, u"防御": 352.8, u"速度": 117, u"暴击": 11, u"暴击伤害": 160, u"效果命中": 0, u"效果抵抗": 0},
                u"面灵气": {u"攻击": 3242.8, u"生命": 10139.88, u"防御": 396.9, u"速度": 119, u"暴击": 8, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"鬼灯": {u"攻击": 3189.2, u"生命": 9228.52, u"防御": 441, u"速度": 110, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"卖药郎": {u"攻击": 3350, u"生命": 10253.8, u"防御": 392.49, u"速度": 112, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"御馔津": {u"攻击": 3001.6, u"生命": 12646.12, u"防御": 449.82, u"速度": 119, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"玉藻前": {u"攻击": 3350, u"生命": 12532.2, u"防御": 352.8, u"速度": 110, u"暴击": 12, u"暴击伤害": 160, u"效果命中": 0, u"效果抵抗": 0},
                u"山风": {u"攻击": 3403.6, u"生命": 11393, u"防御": 388.08, u"速度": 115, u"暴击": 1, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"奴良陆生": {u"攻击": 3028.4, u"生命": 11393, u"防御": 383.67, u"速度": 113, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 50},
                u"雪童子": {u"攻击": 3323.2, u"生命": 10025.96, u"防御": 388.08, u"速度": 121, u"暴击": 8, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"彼岸花": {u"攻击": 3001.6, u"生命": 11393, u"防御": 388.08, u"速度": 107, u"暴击": 8, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"荒": {u"攻击": 3323.2, u"生命": 10253.8, u"防御": 498.51, u"速度": 104, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"辉夜姬": {u"攻击": 2231.6, u"生命": 13785.32, u"防御": 405.72, u"速度": 108, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"花鸟卷": {u"攻击": 2304.8, u"生命": 14127.08, u"防御": 396.9, u"速度": 112, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"一目连": {u"攻击": 2385.2, u"生命": 13899.24, u"防御": 392.49, u"速度": 117, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"妖刀姬": {u"攻击": 3269.9, u"生命": 10025.96, u"防御": 396.9, u"速度": 111, u"暴击": 12, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"青行灯": {u"攻击": 2438.8, u"生命": 11620.84, u"防御": 471.87, u"速度": 119, u"暴击": 8, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"茨木童子": {u"攻击": 3216, u"生命": 10253.8, u"防御": 396.9, u"速度": 112, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"小鹿男": {u"攻击": 2814, u"生命": 11165.16, u"防御": 426.9, u"速度": 120, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"两面佛": {u"攻击": 3135.6, u"生命": 10381.64, u"防御": 401.31, u"速度": 109, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"阎魔": {u"攻击": 2465.6, u"生命": 11962.6, u"防御": 454.23, u"速度": 127, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"荒川之主": {u"攻击": 3001.6, u"生命": 11051.24, u"防御": 401.31, u"速度": 111, u"暴击": 20, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"酒吞童子": {u"攻击": 3135.6, u"生命": 11165.16, u"防御": 374.85, u"速度": 113, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"大天狗": {u"攻击": 3135.6,u"生命": 10025.96,u"防御": 418.95,u"速度": 110,u"暴击": 10,u"暴击伤害": 150,u"效果命中": 0,u"效果抵抗": 0},

                u"-----SR------":{},
                u"入殓师": {u"攻击": 3028.4, u"生命": 9342.44, u"防御": 463.05, u"速度": 104, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"一反木绵": {u"攻击": 2733.6, u"生命": 1174.76, u"防御": 418.95, u"速度": 118, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"於菊虫": {u"攻击": 2948, u"生命": 11962.6, u"防御": 374.85, u"速度": 109, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u'人面树': {u"攻击": 1795.6, u"生命": 12987.88, u"防御": 511.56, u"速度": 98, u"暴击": 8, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"阿香": {u"攻击": 3162.4, u"生命": 10595.56, u"防御": 401.31, u"速度": 114, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"猫掌柜": {u"攻击": 3001.6, u"生命": 10709.48, u"防御": 414.54, u"速度": 118, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"奕":{u"攻击": 3001.6, u"生命": 9912.04, u"防御": 445.41, u"速度": 106, u"暴击": 8, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"薰": {u"攻击": 2251.2, u"生命": 13899.24, u"防御": 396.9, u"速度": 111, u"暴击": 3, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"日和坊": {u"攻击": 2358.4, u"生命": 14013.16, u"防御": 392.49, u"速度": 112, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"追月神": {u"攻击": 2304.8, u"生命": 12760.04, u"防御": 449.82, u"速度": 109, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"百目鬼": {u"攻击": 2733.6, u"生命": 9456.36, u"防御": 507.15, u"速度": 118, u"暴击": 3, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"书翁": {u"攻击": 2680, u"生命": 11393, u"防御": 441, u"速度": 109, u"暴击": 8, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"小松丸": {u"攻击": 2921.2, u"生命": 10823.4, u"防御": 423.36, u"速度": 115, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"匣中少女": {u"攻击": 2438.8, u"生命": 13671.4, u"防御": 392.49, u"速度": 119, u"暴击": 3, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"以津真天": {u"攻击": 3269.9, u"生命": 10025.96, u"防御": 396.9, u"速度": 110, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"鸩": {u"攻击": 3001.6, u"生命": 11393, u"防御": 388.08, u"速度": 119, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"金鱼姬": {u"攻击": 2331.6, u"生命": 13671.4, u"防御": 410.13, u"速度": 116, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"烟烟罗": {u"攻击": 3162.4, u"生命": 10595.56, u"防御": 392.49, u"速度": 112, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"白童子": {u"攻击": 3189.2, u"生命": 10481.64, u"防御": 392.49, u"速度": 113, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"黑童子": {u"攻击": 3376.8, u"生命": 9912.04, u"防御": 383.67, u"速度": 109, u"暴击": 9, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"夜叉": {u"攻击": 3269.6, u"生命": 10139.88, u"防御": 392.49, u"速度": 110, u"暴击": 12, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"万年竹": {u"攻击": 3269.9, u"生命": 10139.88, u"防御": 392.49, u"速度": 115, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"青坊主": {u"攻击": 2385.2, u"生命": 13329.64, u"防御": 414.54, u"速度": 118, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"般若": {u"攻击": 3135.6, u"生命": 10595.56, u"防御": 396.9, u"速度": 114, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"络新妇": {u"攻击": 3216, u"生命": 10253.8, u"防御": 396.9, u"速度": 112, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"惠比寿": {u"攻击": 2358.4, u"生命": 12873.96, u"防御": 436.59, u"速度": 107, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"樱花妖": {u"攻击": 2385.2, u"生命": 13785.32, u"防御": 396.9, u"速度": 99, u"暴击": 3, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"白狼": {u"攻击": 3082, u"生命": 10823.4, u"防御": 396.9, u"速度": 112, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"二口女": {u"攻击": 2626.4, u"生命": 11506.92, u"防御": 445.41, u"速度": 116, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"姑获鸟": {u"攻击": 3082, u"生命": 10823.4, u"防御": 396.9, u"速度": 113, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"镰鼬": {u"攻击": 2680, u"生命": 11620.84, u"防御": 423.18, u"速度": 117, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"清姬": {u"攻击": 2412, u"生命": 11848.68, u"防御": 467.46, u"速度": 105, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"食梦貘": {u"攻击": 2412, u"生命": 11962.6, u"防御": 463.05, u"速度": 119, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"妖琴师": {u"攻击": 2572.8, u"生命": 12646.12, u"防御": 410.13, u"速度": 120, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"妖狐": {u"攻击": 3055.2, u"生命": 10367.72, u"防御": 418.95, u"速度": 115, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"吸血姬": {u"攻击": 3001.6, u"生命": 10937.32, u"防御": 405.72, u"速度": 115, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"凤凰火": {u"攻击": 2680, u"生命": 11393, u"防御": 441, u"速度": 106, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"判官": {u"攻击": 3028.4, u"生命": 10481.64, u"防御": 418.95, u"速度": 118, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"海坊主": {u"攻击": 3055.2, u"生命": 10139.88, u"防御": 427.77, u"速度": 109, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"傀儡师": {u"攻击": 2840.8, u"生命": 11734.76, u"防御": 401.31, u"速度": 108, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"跳跳哥哥": {u"攻击": 3055.2, u"生命": 10709.48, u"防御": 405.72, u"速度": 119, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"鬼女红叶": {u"攻击": 2974.8, u"生命": 10253.8, u"防御": 436.59, u"速度": 114, u"暴击": 8, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"骨女": {u"攻击": 2948, u"生命": 9912.04, u"防御": 454.23, u"速度": 107, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"犬神": {u"攻击": 3001.6, u"生命": 10253.8, u"防御": 432.18, u"速度": 109, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"孟婆": {u"攻击": 2921.2, u"生命": 10709.48, u"防御": 427.77, u"速度": 115, u"暴击": 8, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"鬼使黑": {u"攻击": 3108.8, u"生命": 10367.72, u"防御": 410.13, u"速度": 101, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"鬼使白": {u"攻击": 3055.2, u"生命": 10253.8, u"防御": 423.36, u"速度": 116, u"暴击": 8, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"雪女": {u"攻击": 3055.2, u"生命": 10481.64, u"防御": 414.54, u"速度": 109, u"暴击": 8, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"桃花妖": {u"攻击": 2385.2, u"生命": 11393, u"防御": 489.51, u"速度": 100, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},

                u"------R------":{},
                u"天井下": {u"攻击": 2251.2, u"生命": 11962.6, u"防御": 489.51, u"速度": 109, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"蜜桃&芥子":{u"攻击": 2063.6, u"生命": 12418.28, u"防御": 485.1, u"速度": 110, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"虫师": {u"攻击": 2385.2, u"生命": 14013.16, u"防御": 388.08, u"速度": 115, u"暴击": 3, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"小袖之手": {u"攻击": 2948, u"生命": 11051.24, u"防御": 401.31, u"速度": 116, u"暴击": 8, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"数珠": {u"攻击": 2251.2, u"生命": 11051.24, u"防御": 485.1, u"速度": 111, u"暴击": 3, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 25},
                u"兔丸": {u"攻击": 2412, u"生命": 13215.72, u"防御": 414.54, u"速度": 116, u"暴击": 3, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"古笼火": {u"攻击": 2519.2, u"生命": 13215.72, u"防御": 396.9, u"速度": 117, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"青蛙瓷器": {u"攻击": 2974.8, u"生命": 10595.56, u"防御": 423.36, u"速度": 107, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"觉": {u"攻击": 2599.6, u"生命": 11620.84, u"防御": 445.41, u"速度": 108, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"首无": {u"攻击": 2894.4, u"生命": 10937.32, u"防御": 423.36, u"速度": 110, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"山童": {u"攻击": 3001.6, u"生命": 10139.88, u"防御": 436.59, u"速度": 116, u"暴击": 8, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"蝴蝶精": {u"攻击": 2438.8, u"生命": 12076.52, u"防御": 454.23, u"速度": 115, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"萤草": {u"攻击": 2680, u"生命": 11393, u"防御": 441, u"速度": 103, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"山兔": {u"攻击": 2894.4, u"生命": 10709.48, u"防御": 432.18, u"速度": 115, u"暴击": 8, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"管狐": {u"攻击": 3001.6, u"生命": 10595.56, u"防御": 418.95, u"速度": 108, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"椒图": {u"攻击": 2304.8, u"生命": 12304.36, u"防御": 467.46, u"速度": 117, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"铁鼠": {u"攻击": 2921.2, u"生命": 10709.48, u"防御": 427.77, u"速度": 115, u"暴击": 8, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"独眼小僧": {u"攻击": 2519.2, u"生命": 11734.76, u"防御": 454.23, u"速度": 118, u"暴击": 8, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"丑时之女": {u"攻击": 2894.4, u"生命": 11165.16, u"防御": 414.54, u"速度": 117, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"兵俑": {u"攻击": 2385.2, u"生命": 13329.64, u"防御": 414.54, u"速度": 116, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"跳跳妹妹": {u"攻击": 3055.2, u"生命": 10937.32, u"防御": 396.9, u"速度": 108, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"跳跳弟弟": {u"攻击": 3028.4, u"生命": 10709.48, u"防御": 410.13, u"速度": 104, u"暴击": 8, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"雨女": {u"攻击": 2251.2, u"生命": 12304.36, u"防御": 476.28, u"速度": 103, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"武士之灵": {u"攻击": 3028.4, u"生命": 10481.64, u"防御": 418.95, u"速度": 110, u"暴击": 8, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"食发鬼": {u"攻击": 2894.4, u"生命": 10709.48, u"防御": 423.18, u"速度": 118, u"暴击": 8, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"鸦天狗": {u"攻击": 2974.8, u"生命": 10481.64, u"防御": 427.77, u"速度": 111, u"暴击": 8, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"巫蛊师": {u"攻击": 3055.2, u"生命": 10709.48, u"防御": 405.72, u"速度": 105, u"暴击": 8, u"暴击伤害": 150, u"效果命中": 20, u"效果抵抗": 0},
                u"饿鬼": {u"攻击": 2840.8, u"生命": 11393, u"防御": 414.54, u"速度": 105, u"暴击": 8, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"童女": {u"攻击": 2412, u"生命": 12987.88, u"防御": 423.36, u"速度": 109, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"童男": {u"攻击": 2438.8, u"生命": 12760.04, u"防御": 427.77, u"速度": 103, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"河童": {u"攻击": 3028.4, u"生命": 10139.88, u"防御": 432.18, u"速度": 113, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"狸猫": {u"攻击": 2358.4, u"生命": 12873.96, u"防御": 436.59, u"速度": 109, u"暴击": 8, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"九命猫": {u"攻击": 2974.8, u"生命": 9798.12, u"防御": 454.23, u"速度": 108, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"鲤鱼精": {u"攻击": 2734.6, u"生命": 11620.84, u"防御": 423.36, u"速度": 117, u"暴击": 5, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"座敷童子": {u"攻击": 2331.6, u"生命": 12418.28, u"防御": 458.64, u"速度": 102, u"暴击": 8, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
                u"三尾狐": {u"攻击": 2921.2, u"生命": 10367.72, u"防御": 441, u"速度": 122, u"暴击": 10, u"暴击伤害": 150, u"效果命中": 0, u"效果抵抗": 0},
}

ATTACK_YUHUN_TYPE = [t for t, e in YUHUN_INCREASE.items()
                      if e[u'加成类型'] in ['', u'攻击加成', u'暴击']]

HEALTH_YUHUN_TYPE = [t for t, e in YUHUN_INCREASE.items()
                      if e[u'加成类型'] in ['', u'生命加成', u'暴击', u'效果抵抗']]

EFFECT_YUHUN_TYPE = [t for t, e in YUHUN_INCREASE.items()
                      if e[u'加成类型'] in ['', u'效果命中', u'效果抵抗']]
