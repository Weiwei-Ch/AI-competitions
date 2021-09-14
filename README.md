# AI-competitions

为了积累模型实战经验，以下为本人近期参加的一些AI竞赛项目，目的只是达到设置的baseline即可，非追求最高竞赛排名。

1.新闻文本分类

比赛：天池赛，链接https://tianchi.aliyun.com/competition/entrance/531810/information

model: Bert模型。因提供的文本数据为脱敏后的字符串，因原始bert预训练模型通过文本数据训练而得，若使用原始bert预训练模型，效果不是很好。
       所以使用的预训练模型为自己根据所提供的字符串重新训练的模型，然后依托预训练所得结果，使用一个bert-mini模型对数据进行微调训练；
       
天池得分：长期赛:179 /0.9437， 共6071只队伍(baseline 0.93)；

代码：代码太多，未上传；



2.阿里云安全恶意程序检测

比赛：天池赛，链接https://tianchi.aliyun.com/competition/entrance/231694/information

model: 在常规的数据处理和特征工程后，依据所给的api字段的字符串，构建td-idf特征，再通过xgboost和lightgbm建模；

天池得分：274/0.489921，共2724队伍(baseline 0.49, 此为loss值评估，结果是越小越好)；

代码：上传了一个主要版本的代码；



3.点击反欺诈预测

比赛：百度飞浆赛，链接https://aistudio.baidu.com/aistudio/competition/detail/52

model: 在常规的数据处理和特征工程后,构建了关键的特征变量，再通过xgboost和ightbgm建模；

得分：89.01（baseline 0.89）；

代码：上传了一个主要版本的代码；



