我有一张excel食品成分数据表，里面有很多表格，其中一个名为“主食”的表格部分内容如下：

|                    | 可食部分 | 能量 | 水分        | 蛋白质      | 脂肪        |
| ------------------ | -------- | ---- | ----------- | ----------- | ----------- |
| 春卷               | 100      | 463  | 23.5        | 6.099999905 | 33.70000076 |
| 煎饼               | 100      | 333  | 6.800000191 | 7.599999905 | 0.699999988 |
| 烙饼（标准粉）     | 100      | 255  | 36.40000153 | 7.5         | 2.299999952 |
| 馒头（蒸，标粉）   | 100      | 233  | 40.5        | 7.800000191 | 1           |
| 馒头（蒸，富强粉） | 100      | 208  | 47.29999924 | 6.199999809 | 1.200000048 |
| 面条（标准粉）     | 100      | 280  | 29.70000076 | 8.5         | 1.600000024 |
| 米饭（蒸，籼米）   | 100      | 114  | 71.09999847 | 2.5         | 0.200000003 |
| 糯米（籼）         | 100      | 352  | 12.30000019 | 7.900000095 | 1.100000024 |
| 荞麦               | 100      | 324  | 13          | 9.300000191 | 2.299999952 |

我想将食物名称作为关键字，这种食物所含的营养成分作为值，存入MySQL数据库“food_composition”里，对所有的表格都分别作为这个数据库中单独的数据表存储。该怎么实现



对于这种表格

| 名 称              | 可食部分 | 能量 | 水分        | 蛋白质      | 脂肪        | 膳食纤维    | 碳水化物    |
| ------------------ | -------- | ---- | ----------- | ----------- | ----------- | ----------- | ----------- |
| 春卷               | 100      | 463  | 23.5        | 6.099999905 | 33.70000076 | 1           | 33.79999924 |
| 煎饼               | 100      | 333  | 6.800000191 | 7.599999905 | 0.699999988 | 9.100000381 | 74.69999695 |
| 烙饼（标准粉）     | 100      | 255  | 36.40000153 | 7.5         | 2.299999952 | 1.899999976 | 51          |
| 馒头（蒸，标粉）   | 100      | 233  | 40.5        | 7.800000191 | 1           | 1.5         | 48.29999924 |
| 馒头（蒸，富强粉） | 100      | 208  | 47.29999924 | 6.199999809 | 1.200000048 | 1           | 43.20000076 |
| 面条（标准粉）     | 100      | 280  | 29.70000076 | 8.5         | 1.600000024 | 1.5         | 58          |
| 米饭（蒸，籼米）   | 100      | 114  | 71.09999847 | 2.5         | 0.200000003 | 0.400000006 | 25.60000038 |
| 糯米（籼）         | 100      | 352  | 12.30000019 | 7.900000095 | 1.100000024 | 0.5         | 77.5        |
| 荞麦               | 100      | 324  | 13          | 9.300000191 | 2.299999952 | 6.5         | 66.5        |

怎么在将其存入MySQL后，再次从数据库里提取出来，并保留原信息不变



