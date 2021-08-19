# -*- coding: utf-8 -*-
str  = 'QA完成了 08月05号Android&iOS版本的Smoke Test。版本block issue：修改模型根骨骼，导致序章和第一章相关剧情动画出错，剧情相关暂时不smoke；'
len_str = len(str)
#字符串拆分
head = str[:6]
# middle =
end = str[-(len_str - 12):]
print(head + end)