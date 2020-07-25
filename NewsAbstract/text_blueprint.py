# -*- coding: UTF-8 -*-

import os
import json
from flask import request, render_template, Flask
import NewsAbstract
from conf.logConf import logger


app = Flask('News_Extract',static_folder='static', template_folder='templates')


# setting up template directory
ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

@app.route('/', methods=["GET"])
def index():
    logger.info("run app_summarization")
    return render_template('pro2.html')


# 信息内容提取
@app.route('/show', methods=['POST'])
def extract_summarization():
    try:
        data = request.json
        text = data['text']

        # 判断文本的类型，如果是bytes，则转换为utf-8
        if isinstance(text, bytes):
            text = text.decode('utf-8')
        # 去掉文本中的全角空白符，不间断空白符 &nbsp;，字节顺序标记，换行
        text = text.replace('\u3000', '').replace('\xa0', '').replace('\ufeff', '').replace('\n', '').replace('\\n', '')
        result = NewsAbstract.main(text)
        # print(result)

        # 封装为字典
        '''
            需要修改的地方，result_dict【0：3】储存了：主语、动词、宾语
{0: '蒋丽芸', 1: '说', 2: '自己曾经与年轻人交谈过，很多人都不想“港独”，并表示支持“一国两制”，但经常会有人将“独立”加诸年轻人口中。'}
        '''
        result_dict = []
        print(len(result_dict))
        for i in range(len(result)):
            res = {}
            for id,words in enumerate(result[i][1:]):
                res[id] = words[0]
            result_dict.append(res)
        print(result_dict)


        res = {'code': 1, 'message': '数据获取成功', 'summarization': result_dict }
        logger.info('/show接口数据获取成功')

    except Exception as e:
        logger.error(e)
        res = {'code': 0, 'message': '系统内部错误，请联系管理员', 'data': ''}

    return json.dumps(res, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    # main run
    app.run(debug=True)
