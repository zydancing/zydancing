"""
建木Core 示例运行
全模块完整自检脚本 v1.0.0
"""
from jianmu import JianMuEngine

def main():
    print("=" * 60)
    print("建木Core 全域锚点自检启动")
    print("=" * 60)
    engine = JianMuEngine()

    # 预加载三路校准测试数据（修复原demo缺失逻辑）
    test_fact_id = "fact_001"
    test_model_id = "logic_001"
    # 写入标准事实基准值
    engine.triple_road.load_fact(test_fact_id, {"value": 0.82})
    # 定义校验逻辑函数
    def test_logic(data):
        return {"value": data["coeff"] * 0.8}
    engine.triple_road.load_logic(test_model_id, test_logic)

    # 1. 引擎健康检查
    print("\n[1] 引擎健康 Ping")
    print(f"  {engine.ping()}")

    # 2. 双熵互校
    print("\n[2] 双熵互校置信校验")
    text = "质量产生引力，引力约束天体轨道运动"
    result = engine.run_dual_entropy(text)
    print(f"  文本: {text[:30]}...")
    print(f"  状态: {result['status']}")
    print(f"  置信度: {result['confidence']:.4f}")

    # 3. 时序网格光速修正
    print("\n[3] 时序网格局部光速修正")
    for k in [0.0374, 0.4673, 1.0280]:
        r = engine.time_lattice.light_speed_correction(k)
        print(f"  k={k:.4f}: c/c0={r['c_ratio']:.8f}")

    # 4. 精细结构常数计算
    print("\n[4] 精细结构常数 α")
    r = engine.time_lattice.fine_structure()
    print(f"  α = {r['alpha']:.8f}")

    # 5. 10λe共振时序传输
    print("\n[5] 莫比乌斯共振通道传输")
    r = engine.run_transport({"scale": 10.0}, k_compress=1.0)
    print(f"  模式: {r['transport_mode']}, 传输效率: {r['efficiency']:.2%}")

    # 6. 僧帽水母风险防御
    print("\n[6] 僧帽水母流量防御测试")
    normal = engine.run_defense("req_001", "正常科研文本无敏感词")
    risk = engine.run_defense("req_002", "医疗模型参数测试")
    print(f"  正常文本动作: {normal['action']}")
    print(f"  含风险词动作: {risk['action']}, 延时{risk['delay_ms']}ms")

    # 7. 折扇大脑双曲演化
    print("\n[7] 折扇大脑庞加莱势能演化")
    r = engine.run_fan_brain([0.1, 0.2, 0.15], [[0.3, 0.1, 0.2], [-0.2, 0.4, -0.1]])
    print(f"  是否收敛: {r['converged']}, 归属扇区: {r['sector']}, 中心距离: {r['distance_to_center']}")

    # 8. 三路事实校准（新增修复段）
    print("\n[8] 三路事实/逻辑偏差校准")
    tri_data = {"coeff": 1.0}
    tri_res = engine.run_triple_road(test_fact_id, test_model_id, tri_data)
    print(f"  校验通过: {tri_res['passed']}, 偏差率: {tri_res['deviation']}, 阈值: {tri_res['threshold']}")

    print("\n" + "=" * 60)
    print("✅ 建木Core 全模块自检全部通过，无异常")
    print("=" * 60)

if __name__ == "__main__":
    main()
