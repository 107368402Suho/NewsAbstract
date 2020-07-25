import NewsAbstract
text0 = "蒋丽芸说，自己曾经与年轻人交谈过，很多人都不想“港独”，并表示支持“一国两制”，但经常会有人将“独立”加诸年轻人口中。她提到，有民调亦显示绝大多数年轻人是不支持“港独”的。"
text1 = '如李华一样，在疫情下焦灼等待的中国留学生还有很多。中国留学群体庞大，4月中国外交部副部长马朝旭曾引述教育部门统计数据称，中国海外留学人员总人数为160万人，尚在国外的约140万人'
text2 = '李华对BBC中文表示：“目前我和同学们都还在观望，如果到了澳大利亚还要上网课，那也划不来。”'
text3 = '美国联邦调查局认为，一名因隐瞒自己与中国军队关系、涉嫌签证欺诈的中国研究人员逃入中国驻旧金山领馆藏身。美国检控方说，这起案例只是中国隐蔽派遣军方科研人员进入美国计划的一部分'
result = NewsAbstract.main(text0)

result_dict = []
for i in range(len(result)):
    res = []
    for words in result[i][1:]:
        res.append(words[0])
    result_dict.append(res)
print(result_dict)
