from google_trans_new import google_translator

# 实例化翻译对象
translator = google_translator()
# 进行第一次批量翻译，翻译目标是韩语
text = ["我爱中国","日本人都是没爹没妈的死人"]
ko_res = translator.translate(text,lang_src="zh_cn",lang_tgt="ko")
# 打印结果
print("中间翻译结果:",ko_res)
# 最后在翻译回中文，完成回译全部流程
cn_res=translator.translate(ko_res,lang_src="ko",lang_tgt="zh_cn")
print("回译得到的增强数据：",cn_res)