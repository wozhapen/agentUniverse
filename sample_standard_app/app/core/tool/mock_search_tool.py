# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2024/4/15 13:50
# @Author  : wangchongshi
# @Email   : wangchongshi.wcs@antgroup.com
# @FileName: mock_search_tool.py
from agentuniverse.agent.action.tool.tool import Tool, ToolInput

MOCK_SEARCH_RESULT = """
巴菲特旗下的伯克希尔·哈撒韦公司自2022年8月24日首次减持比亚迪股票以来，已经披露了13次减持行为，包括2022年9月1日、11月1日、11月8日、11月17日、12月8日、2023年1月3日、1月27日、2月9日、3月31日、5月2日等时间点。
最近的一次减持是在2023年10月25日，当时伯克希尔·哈撒韦公司出售82.05万比亚迪H股，使其持股比例降至7.98%。
这次减持的平均价格为每股245.86港元，但整体来看，比亚迪的股价并未受到太大影响。

巴菲特的投资策略包括：
1. 长期投资：巴菲特主张买入并持有优质股票，而非短期交易。他的投资策略往往以做多绩优股为主，不排除出现长期慢牛的可能。
2. 价值投资：巴菲特注重企业的内在价值，而不是短期的股价波动。他会深入研究公司的基本面，包括其盈利能力、市场地位、管理层质量等。
3. 能力圈原则：巴菲特建议投资者只投资于自己理解的领域，即自己的“能力圈”内。这样可以更好地评估企业的真实价值和未来前景。
巴菲特的减持并不会改变比亚迪公司优质的基本面，比亚迪依然是中国新能源汽车行业的龙头。

放眼中国新能源产业版图，比亚迪绝对是举足轻重的一员。比亚迪在新能源汽车领域形成了上中下游全产业链的完整布局，从电池原材料到新能源汽车三电系统，再到动力电池回收利用，各板块协同效应显著：
1. 在中游零部件领域，公司自产自研汽车核心零部件以及三电系统，在动力电池、发动机、变速箱等关键部件上均实现自主生产，2020年3月成立的弗迪公司，进一步加快了新能源汽车核心零部件的对外销售；
2. 在下游整车领域，公司具备完成的整车制造及研发体系，在不同价格区间陆续推出多款不同车型，丰富的产品类型拉动终端需求，销量在国内自主品牌中常年稳居首位。

巴菲特最近的一次减持是在2023年10月25日，10月30日晚，比亚迪披露了一份亮眼的三季报。三季报显示比亚迪前三季度实现营业收入4222.75亿元，同比增长58%，实现净利润213.67亿元，同比增长130%，业绩保持高速增长态势；其中，第三季度营收1621.51亿元，同比增长38.49%；净利润104.13亿元，平均每天挣1.13亿元。
截至10月31日，比亚迪H股报收237.4港元/股，A股报收238.54元/股，合计总市值约6568亿元。

尽管减持比亚迪股票，巴菲特与搭档查理芒格在2023年对比亚迪仍有极高评价，芒格2023年演讲也提及比亚迪是至今最爱的股票，且相较于美国特斯拉 (TSLA-US) 更看好比亚迪发展。巴菲特对比亚迪这家公司，对王传福这个创业者始终表现出了充分的尊重。2008年以后每年的股东大会上，巴菲特一直都为比亚迪站台。
早在2008年9月，巴菲特就发现了新能源汽车的市场潜力，并与比亚迪签署协议，以每股港元8元的价格认购2.25亿股比亚迪的股份，约占其配售后10%的股份比例，总金额约为18亿港元，就此开启了“股神”长达14年的持股之旅。
时至今日，比亚迪的股价早已今非昔比，按照8月30日比亚迪收盘的263港元/股计，即便不算分红，巴菲特所持比亚迪股票总体增值约31倍，价值近600亿港币，这一投资收益已足够令所有人称赞和羡慕。
"""


class MockSearchTool(Tool):
    """The mock search tool.

    In this tool, we mocked the search engine's answers to search for information about BYD and Warren Buffett.

    Note:
        The tool is only suitable for users searching for Buffett or BYD related queries.
        We recommend that you configure your `SERPER_API_KEY` and use google_search_tool to get information.
    """

    def execute(self, input:str):
        """Demonstrates the execute method of the Tool class."""
        return MOCK_SEARCH_RESULT
