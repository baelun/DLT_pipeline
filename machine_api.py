from flask import Flask, jsonify
import numpy as np
 
app = Flask(__name__)
 
# 假设这是你要提供的数据
data = []
 
 
 
# 設定參數
num_records = 10  # 總數據記錄數量
air_temp_mean = 300  # K
air_temp_std = 2  # K
process_temp_std = 1  # K
power = 2860  # W
torque_mean = 40  # Nm
torque_std = 10  # Nm
machine_name = "Machine_A"  # 使用單一機台名稱
 
 
def generate_data():
# 初始化數據列表
    data = []
 
    for uid in range(1, num_records + 1):
        # 生成唯一識別碼
        unique_id = uid
       
        # 生成空氣溫度
        air_temp = air_temp_mean + np.random.normal(0, air_temp_std)
       
        # 生成過程溫度
        process_temp = air_temp + 10 + np.random.normal(0, process_temp_std)
       
        # 計算轉速
        rotational_speed = (power / (2 * np.pi)) * 60  # 將功率轉換為RPM
        rotational_speed += np.random.normal(0, rotational_speed * 0.05)  # 添加噪音
 
        # 生成扭矩
        torque = np.random.normal(torque_mean, torque_std)
        torque = max(torque, 0)  # 確保不為負值
       
        # 隨機生成機器故障標籤
        machine_failure = bool(np.random.choice([True, False]))
       
        # 將數據添加到列表中
        data.append({
            'UID': unique_id,
            'MachineName': machine_name,
            'AirTemperature_K': air_temp,
            'ProcessTemperature_K': process_temp,
            'RotationalSpeed_rpm': rotational_speed,
            'Torque_Nm': torque,
            'MachineFailure': machine_failure
        })
    return data
 
@app.route('/data', methods=['GET'])
def get_data():
    data = generate_data()  # 在应用启动时生成数据
 
 
    print(data)
    print(jsonify(data))
    return jsonify(data)  # 返回当前的数据
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # 让应用在所有可用的 IP 上运行
