# Sensor_Controller

### Introduction
從serial接收0～15的數字，控制多工器切換到指定的channel。

### main.py
主邏輯

### mux.py
多工器定義

### config.json
設定檔
```
{
    "port":"/dev/ttyUSB0", //不用動
    "baud":9600,           //不用動

    "mux_top_A": 17,       //上多工器的A腳
    "mux_top_B": 27,       //上多工器的B腳

    "mux_bottom_A": 23,    //下面四個多工器的A腳（接一起）
    "mux_bottom_B": 24     //下面四個多工器的B腳（接一起）
}
```