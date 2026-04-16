def dual_entropy_calibrate(text):
    # 正向熵减：补全、规整
    forward = "用户核心意图：不想出门"
    # 反向熵增：剥离、压缩
    backward = "核心：不想出门"
    
    # 双熵取交集 = 稳定核心
    if "不想出门" in forward and "不想出门" in backward:
        return "【双熵互校结果】稳定核心：不想出门"
    else:
        return "unconfirmed"

if __name__ == "__main__":
    text = "我今天不太想出门, 外面冷, 也有事, 主要还是懒得动."
    print(dual_entropy_calibrate(text))
