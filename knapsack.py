import itertools


# goods[][0]: 品物
# goods[][1]: 容量
# goods[][2]: 値段
# CAPACITY: ナップサックの容量
# combinates: CAPACITYを満たすgoods[]の組み合わせ
# total_fees: CAPACITYを満たすgoods[]の組み合わせにおける金額
# result_combinate: answer
goods = [[1,4,6],[2,8,12],[3,3,4],[4,5,3],[5,9,7],[6,2,1],[7,3,3],[8,1,2],
[9,5,7],[10,2,3],[11,4,4],[12,2,2],[13,7,10],[14,10,13],[15,3,5],[16,13,16],[17,11,14,],[18,8,9]]
CAPACITY = 45
combinates = []
total_fees = []
result_combinate = []

# CAPACITYを満たすgoods[]の組み合わせを求める
for i, _ in enumerate(goods,1):
        for j in itertools.combinations(goods, r=i):
                contents = 0
                for k in j:
                        contents += k[1]
                if contents <= CAPACITY:
                        combinates.append(j)
# CAPACITYを満たすgoods[]の組み合わせにおける合計金額(total_fee)を求める
for i in combinates:
        total_fee = 0
        for j in i:
                total_fee += j[2]
        total_fees.append(total_fee)

res = combinates[total_fees.index(max(total_fees))]
for i in res:
        result_combinate.append(i[0])
print("組み合わせ: {}\n合計金額: {}".format(result_combinate, max(total_fees)))
